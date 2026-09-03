# Cloud Security Detection as Code

[![Detection Quality](https://github.com/KaffyDevelops/cloud-security-detection-as-code/actions/workflows/detection-quality.yml/badge.svg)](https://github.com/KaffyDevelops/cloud-security-detection-as-code/actions/workflows/detection-quality.yml)

> **Open-source multi-cloud detection engineering repository**  
> **Platforms:** Microsoft Azure · AWS · Google Cloud  
> **Author:** Kafayat “Kaffy” Faniran  
> **Status:** Initial catalogue implemented, controlled validation pending

## Purpose

Cloud detections should be reviewable, testable and maintainable like code.

This repository turns cloud-security detection logic into a structured engineering artefact:

**security objective → telemetry → query → MITRE ATT&CK mapping → test scenario → false positives → triage → response → validation status**

It is designed for cloud security engineers, SOC analysts, detection engineers, learners building defensible portfolios and open-source contributors.

## Evidence Standard

The repository separates three states:

- **Implemented:** detection logic and documentation exist.
- **Tested:** the rule has been exercised against controlled or representative telemetry.
- **Validated:** observed evidence demonstrates the rule identifies the intended activity with documented limitations.

No rule is labelled **validated** simply because the query parses or looks reasonable.

## Initial Detection Catalogue

| ID | Platform | Detection | MITRE ATT&CK | Severity | Status |
|---|---|---|---|---|---|
| AZ-001 | Azure | Repeated failed Microsoft Entra sign-ins | T1110 Brute Force | Medium | Implemented |
| AZ-002 | Azure | Privileged Microsoft Entra role assignment | T1098 Account Manipulation | High | Implemented |
| AWS-001 | AWS | Successful console sign-in without MFA | T1078 Valid Accounts | High | Implemented |
| AWS-002 | AWS | IAM permission or trust-policy change | T1098 Account Manipulation | High | Implemented |
| GCP-001 | Google Cloud | IAM policy change | T1098 Account Manipulation | High | Implemented |
| GCP-002 | Google Cloud | Service account key creation | T1098 Account Manipulation | High | Implemented |

The catalogue begins intentionally small. The goal is **quality, validation and contribution value**, not inflated rule count.

## Repository Structure

```text
cloud-security-detection-as-code/
├── README.md
├── CONTRIBUTING.md
├── SECURITY.md
├── LICENSE
├── docs/
│   ├── detection-standard.md
│   ├── validation-methodology.md
│   └── mitre-mapping.md
├── tools/
│   └── validate_detections.py
├── detections/
│   ├── azure/
│   ├── aws/
│   └── gcp/
├── sigma/
└── .github/workflows/
    └── detection-quality.yml
```

Each provider-native detection contains `metadata.yml` plus its query file.

## Platform Query Formats

- **Azure:** KQL for Microsoft Sentinel / Log Analytics.
- **AWS:** CloudWatch Logs Insights for CloudTrail events delivered to CloudWatch Logs.
- **Google Cloud:** Cloud Logging query language against Cloud Audit Logs.
- **Sigma:** included where portability is technically sound. Provider-native rules remain the source of truth for platform-specific fields and triage guidance.

## Detection Review Questions

A reviewer should be able to answer:

1. What risky or adversary behaviour is the rule trying to identify?
2. Which telemetry must exist?
3. What exact query implements the detection?
4. Which MITRE ATT&CK behaviour does it map to?
5. How can it be tested safely?
6. Which benign activities could trigger it?
7. What should an analyst investigate next?
8. What response is proportionate?
9. Has the rule actually been tested or validated?
10. What limitations remain?

## Automated Quality Controls

The `Detection Quality` workflow checks metadata structure, unique IDs, allowed states and severities, ATT&CK technique format, query-file presence, required triage/response/false-positive content, Sigma YAML parsing and tracked sensitive-file hygiene.

Passing CI proves **repository quality**, not runtime detection effectiveness.

## Roadmap

1. validate AZ-001 using controlled Microsoft Entra sign-in failures
2. validate AWS-001 using an authorised AWS lab sign-in scenario
3. validate GCP-002 using authorised service-account-key creation activity
4. add sanitised telemetry fixtures where appropriate
5. expand Sigma coverage where portability is defensible
6. accept external issues and pull requests
7. publish release notes for meaningful detection changes

## Responsible Use

Use these rules only in environments you own or are authorised to monitor. Do not publish credentials, unrestricted tenant data or private production telemetry.

## Portfolio

**https://kaffy.thecloudforge.app**

---

This is an open-source technical portfolio project. Detection effectiveness depends on telemetry availability, environment context and validation.