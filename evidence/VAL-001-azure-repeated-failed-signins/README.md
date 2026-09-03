# VAL-001: Azure Repeated Failed Sign-ins

**Detection:** AZ-001  
**Platform:** Microsoft Entra ID / Microsoft Sentinel  
**Status:** Validation prepared, tenant evidence pending  
**Related lab:** [`KaffyDevelops/azure-soc-lab`](https://github.com/KaffyDevelops/azure-soc-lab)

## Objective

Validate AZ-001 against controlled Microsoft Entra ID sign-in telemetry and reconcile the observed result with the repeated-failed-sign-in activity generated in the authorised lab.

This validation is intentionally shared with the Sentinel SOC lab so the same controlled exercise can support both repositories without duplicating or fabricating evidence.

## Detection Under Test

```kusto
SigninLogs
| where ResultType == "50126"
| summarize FailedAttempts = count() by IPAddress, UserPrincipalName
| where FailedAttempts > 5
| project IPAddress, UserPrincipalName, FailedAttempts
| order by FailedAttempts desc
```

## Controlled Test Plan

1. Use a dedicated, non-privileged Microsoft Entra lab identity.
2. Confirm `SigninLogs` is being ingested into the Sentinel workspace.
3. Record the UTC test start time.
4. From one controlled browser/device/network path, submit six invalid-password attempts for the lab identity.
5. Stop immediately if the account begins to lock or any unexpected protection control activates.
6. Wait for sign-in telemetry to reach the workspace.
7. Execute AZ-001 and capture the matching row.
8. Open the resulting Sentinel incident if the corresponding analytics rule is enabled.
9. Run the chronological sign-in investigation query from the Sentinel lab.
10. Reconcile the observed failure count, source context and event times with the controlled activity.

## Required Evidence

### E01 — Detection result

Capture the AZ-001 result showing:

- lab identity, redacted where appropriate
- source IP, redacted where appropriate
- failure count
- query context

### E02 — Sentinel incident

Capture the Sentinel incident showing:

- incident title
- severity
- relevant entity information
- incident time

### E03 — Investigation timeline

Capture the chronological sign-in timeline showing:

- controlled failure events
- timestamps
- source context
- any subsequent successful sign-in, if intentionally performed

## Analyst Questions

- Does the returned failure count reconcile with the controlled activity?
- Were all events associated with the expected lab identity?
- Was the source context consistent with the planned test?
- Did any unrelated user activity enter the result set?
- Would the current threshold generate expected noise in a real tenant?
- Did a success occur after the failure burst?
- Is the activity clearly attributable to the authorised lab exercise?

## Expected Disposition

If the evidence matches the controlled activity, the incident disposition should be documented as **authorised test activity / benign true positive**.

The detection may move from `implemented` to `tested` once the controlled telemetry proves the query behaves as expected. Promotion to `validated` should additionally document analyst usefulness, limitations and any tuning decision supported by the observed data.

## Safety and Disclosure

- Do not use a privileged identity.
- Do not use another person's account.
- Do not publish raw tenant identifiers, unrestricted sign-in exports or personal data.
- Redact account identifiers and IP addresses where public evidence does not require them.
- A controlled match proves the query can detect the tested behaviour. It does not prove the threshold is optimal for every environment.

## Evidence Status

- [x] Validation method documented
- [x] Detection query linked to the Sentinel lab workflow
- [ ] Controlled sign-in activity generated
- [ ] E01 detection result captured
- [ ] E02 Sentinel incident captured
- [ ] E03 investigation timeline captured
- [ ] Analyst findings documented
- [ ] False-positive/tuning assessment completed
- [ ] Detection status reviewed for promotion
