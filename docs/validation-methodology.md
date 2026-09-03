# Validation Methodology

## Objective

Move detections from plausible query logic to defensible engineering evidence.

## Validation Record

For each rule, record:

1. **Hypothesis**: the activity the rule should detect.
2. **Authorised test scenario**: how controlled telemetry will be generated.
3. **Expected telemetry**: fields and events expected to appear.
4. **Expected detection result**: what the query should return.
5. **Observed result**: what actually happened.
6. **False-positive review**: benign conditions discovered during testing.
7. **Tuning decision**: threshold, exclusions or correlation changes.
8. **Conclusion**: pass, partial, fail or inconclusive.
9. **Limitations**: licensing, retention, schema or environment constraints.
10. **Evidence**: redacted screenshots, query results or fixture data.

## Status Promotion

`implemented → tested` requires execution against controlled or representative telemetry.

`tested → validated` requires evidence that the rule identifies the intended behaviour and that documented limitations are acceptable for the stated use case.

## Safety

Do not generate malicious activity against systems you do not own. Prefer low-risk administrative or authentication actions in dedicated lab identities and scopes.