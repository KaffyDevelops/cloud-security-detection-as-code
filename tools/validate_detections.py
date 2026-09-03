from pathlib import Path
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
DETECTIONS = ROOT / "detections"

REQUIRED = {
    "id", "title", "platform", "service", "status", "severity", "description",
    "data_sources", "mitre_attack", "query_file", "test_scenario",
    "false_positives", "triage", "response", "limitations"
}
ALLOWED_PLATFORMS = {"azure", "aws", "gcp"}
ALLOWED_STATUS = {"implemented", "tested", "validated", "deprecated"}
ALLOWED_SEVERITY = {"low", "medium", "high", "critical"}
ID_RE = re.compile(r"^(AZ|AWS|GCP)-\d{3}$")
MITRE_RE = re.compile(r"^T\d{4}(?:\.\d{3})?$")

errors = []
seen_ids = set()
metadata_files = sorted(DETECTIONS.glob("*/*/metadata.yml"))

if not metadata_files:
    errors.append("No detection metadata files found.")

for path in metadata_files:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{path}: YAML parse error: {exc}")
        continue

    if not isinstance(data, dict):
        errors.append(f"{path}: metadata must be a mapping")
        continue

    missing = REQUIRED - set(data)
    if missing:
        errors.append(f"{path}: missing fields: {', '.join(sorted(missing))}")
        continue

    detection_id = str(data["id"])
    if not ID_RE.match(detection_id):
        errors.append(f"{path}: invalid id {detection_id}")
    if detection_id in seen_ids:
        errors.append(f"{path}: duplicate id {detection_id}")
    seen_ids.add(detection_id)

    if data["platform"] not in ALLOWED_PLATFORMS:
        errors.append(f"{path}: unsupported platform {data['platform']}")
    if data["status"] not in ALLOWED_STATUS:
        errors.append(f"{path}: invalid status {data['status']}")
    if data["severity"] not in ALLOWED_SEVERITY:
        errors.append(f"{path}: invalid severity {data['severity']}")

    for field in ("data_sources", "mitre_attack", "test_scenario", "false_positives", "triage", "response", "limitations"):
        if not isinstance(data[field], list) or not data[field]:
            errors.append(f"{path}: {field} must be a non-empty list")

    if isinstance(data["mitre_attack"], list):
        for item in data["mitre_attack"]:
            if not isinstance(item, dict) or "technique_id" not in item or "name" not in item:
                errors.append(f"{path}: each mitre_attack item needs technique_id and name")
                continue
            if not MITRE_RE.match(str(item["technique_id"])):
                errors.append(f"{path}: invalid MITRE technique {item['technique_id']}")

    query_path = path.parent / str(data["query_file"])
    if not query_path.is_file() or not query_path.read_text(encoding="utf-8").strip():
        errors.append(f"{path}: query file missing or empty: {data['query_file']}")

for path in sorted((ROOT / "sigma").glob("*.yml")):
    try:
        parsed = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(parsed, dict):
            errors.append(f"{path}: Sigma file must parse to a mapping")
    except Exception as exc:
        errors.append(f"{path}: Sigma YAML parse error: {exc}")

if errors:
    print("Detection validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"Validated {len(metadata_files)} provider-native detections.")
