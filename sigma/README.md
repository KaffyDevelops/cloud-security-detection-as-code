# Sigma Coverage

Sigma rules are included where a cloud event can be represented without losing essential platform context.

Provider-native queries remain the primary implementation because Azure, AWS and Google Cloud expose different schemas, thresholds and investigation fields.

Sigma contributions should map cleanly to a provider-native detection and should not claim portability that has not been tested.