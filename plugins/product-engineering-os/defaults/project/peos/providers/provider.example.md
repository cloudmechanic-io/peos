# Client provider adapter example

## Capability

Name exactly one stable PEOS capability and its contract version.

## When selected

Describe explicit client configuration and prerequisites. Select a client adapter with `file:peos/providers/<adapter>.md`. The user continues to invoke the PEOS capability, never this provider name.

## Provider invocation

Describe the external skill, tool, methodology, or internal procedure. Keep provider-native temporary files outside the normalized change artifact set when practical.

## Normalization

Map provider output to every required field in the PEOS capability contract. Preserve lifecycle states, approval semantics, provenance, and current/target or delta requirements.

## Failure behavior

Fail visibly when prerequisites or authorization are absent. Never claim success, approval, publication, deployment, or verification without evidence.

## Compatibility and migration

Describe how in-flight artifacts created by the previous provider are resumed or migrated and how to roll back provider selection.
