# Detection Standard

Every provider-native detection must contain a `metadata.yml` file and the query file declared by that metadata.

## Required Metadata

- `id`
- `title`
- `platform`
- `service`
- `status`
- `severity`
- `description`
- `data_sources`
- `mitre_attack`
- `query_file`
- `test_scenario`
- `false_positives`
- `triage`
- `response`
- `limitations`

## Allowed Status Values

- `implemented`
- `tested`
- `validated`
- `deprecated`

A rule may advance only when evidence supports the new state.

## Severity

Severity represents the likely security importance of a true positive, not certainty that the event is malicious.

Allowed values: `low`, `medium`, `high`, `critical`.

## Query Design

Queries should preserve analyst-useful entities, avoid hard-coded tenant identifiers, avoid destructive actions, be readable enough for peer review and document thresholds that may need tuning.

## False Positives

Every detection must document plausible benign explanations. “None” is not an acceptable default.

## Validation

A detection is not validated by syntax checking alone. See `validation-methodology.md`.