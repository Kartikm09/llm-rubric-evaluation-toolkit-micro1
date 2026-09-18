# Verified repair scope

The starting source was `ee6b696dc37d116010e2dde6265dabca6f5f586d`. The bundled example commands completed,
but there was no automated assertion suite. Bounded synthetic input probes
exposed the defect addressed here.

Enforce declared1–5 dimensions across reports; preserve bundled defaults and accept optional CSV fixture.

New regression tests failed before the repair. After the change, `make verify`
passed 3 test methods, including independent result oracles and negative
command-line cases. Every original documented sample command was rerun. Test
counts are methods; parameterized inputs are not inflated into separate tests.

The tests use the standard library and synthetic fixtures. They do not claim
comprehensive schema validation, real model quality, external evidence quality,
or production readiness. CI repeats the discoverable verification command.
