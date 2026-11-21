---
name: domain-probe-observability
description: Add or improve business-oriented observability by exposing domain-language probes and encapsulating logging, metrics, analytics, and other instrumentation details.
---

# Domain Probe observability

Use this skill when product or business behavior needs observability and low-level instrumentation is cluttering domain logic, or when observability behavior is difficult to test. The approach follows Pete Hodgson's [Domain-Oriented Observability](https://martinfowler.com/articles/domain-oriented-observability.html) article hosted by Martin Fowler.

## Choose observations that matter

- Start from product questions and operational decisions: what business outcome, transition, or failure should the team be able to understand?
- Name observations in the domain's language, such as `paymentAuthorized`, `invoiceDeliveryFailed`, or `subscriptionRenewed`, rather than exposing logger, metric, or vendor operations to domain code.
- Distinguish business observations from infrastructure health telemetry. A Domain Probe is useful for hand-authored, domain-specific signals; it does not replace platform metrics, traces, or standard runtime instrumentation.
- Define the context and meaning of each observation, including outcome and useful domain identifiers. Avoid collecting sensitive data or high-cardinality values without an explicit need and safe handling.

## Encapsulate the instrumentation

- Give domain logic a focused probe dependency with methods or events that express meaningful domain observations.
- Implement the probe behind that API. Translate observations into the required logs, metrics, traces, analytics, or event systems there, keeping vendor names, metric strings, and payload formats out of the domain model.
- Inject the probe or a factory at a composition boundary. Add shared technical context such as request or trace identifiers there when available, rather than threading unrelated metadata through domain method signatures.
- Keep the domain call site honest about meaningful moments in the workflow. The probe should remove plumbing noise, not hide important business behavior behind magic instrumentation.
- Choose direct probe calls for simple, explicit flows. Consider an event announcer with separate observers only when multiple independent consumers or stronger decoupling justify the added indirection.

## Test both responsibilities

- In domain tests, use a spy or recording probe to assert that the right domain observation and context are emitted for success and relevant failure paths. Avoid coupling these tests to exact log text or vendor payload schemas.
- In adapter tests, verify that the probe maps domain observations to the required instrumentation calls and fields. Keep these tests focused on the low-level translation.
- Preserve business behavior if an observability backend is unavailable; define and test the failure policy at the adapter boundary when delivery reliability is part of the requirement.
- Avoid duplicate or contradictory signals. Check naming, units, dimensions, and event meaning against existing instrumentation conventions.

## Introduce it incrementally

- Apply the pattern where code is already changing or where an observability gap has practical value. Do not retrofit every domain operation without a concrete question to answer.
- Review the resulting code and tests for clarity. If the probe merely renames low-level calls without improving domain meaning, responsibility, or testability, keep the simpler implementation.
- Report which domain questions the observations support, where the instrumentation is implemented, and what is verified.
