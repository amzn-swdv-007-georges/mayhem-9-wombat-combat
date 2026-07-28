# INSTRUCTOR_NOTES.md

## Activity Verification Matrix

The five activities form a progressive lesson in test architecture.
Each activity targets exactly one testing concept.  Students solve
every activity by refactoring the test file — they must not modify
production code.

| # | Activity | Learning Objective | Intentional Flaw | Expected Student Fix | Prod Files | Test File |
|---|---|---|---|---|---|---|---|
| 1 | Salt Flat | Test isolation via fixtures | Shared global state leaks between tests — one test mutates `TrackEnvironment.friction_coefficient` and never restores it, causing an order-dependent failure | Introduce a pytest fixture that calls `TrackEnvironment.reset()` before or after each test | `environment.py`, `vehicles/truck.py` | `test_salt_flat.py` |
| 2 | Helicopter | Stubbing external dependencies | Tests call the live `get_live_wind_speed()` function, which raises `ConnectionError` — no stub is provided | Patch `get_live_wind_speed` with a stub that returns a deterministic wind-speed value | `weather_api.py`, `vehicles/helicopter.py` | `test_helicopter.py` |
| 3 | Megayacht | Behaviour verification with mocks | Test only asserts on the return value (`"SUCCESS"`) and never inspects how many times `fire_thruster()` was called, masking a production bug that fires the thruster 28 times | Assert that `HardwareActuator.firing_count()` equals 1 after `trigger_ramp_jump()` completes | `hardware.py`, `vehicles/megayacht.py` | `test_megayacht.py` |
| 4 | Canyon Chase | Correct selection of mock vs stub | Test mocks `get_engine_temperature` (verifies it was called) and stubs `wire_insurance_funds` (never verifies the payment command) — the test-double roles are inverted | Swap the doubles: stub `get_engine_temperature` with a plain return value and mock `wire_insurance_funds`, asserting it was called with the correct amount, recipient, and reference | `finance.py` | `test_canyon_chase.py` |
| 5 | Interceptor | Spies for recording interactions | Test directly mocks `LegacyECUDriver` (a vendor binary), replacing the real ECU entirely — the mock can count calls but cannot verify call chronology | Replace the mock with a spy that wraps the real `LegacyECUDriver`, delegates every call through to the real implementation, and records the execution timeline | `legacy.py`, `vehicles/interceptor.py` | `test_interceptor.py` |

---

## Lesson Progression

The activities are designed to be completed in order:

1. **Fixture** (Activity 1) — Students learn to isolate test state.
2. **Stub** (Activity 2) — Students learn to replace an unavailable external dependency.
3. **Mock** (Activity 3) — Students learn to verify side effects, not just return values.
4. **Mock vs Stub** (Activity 4) — Students learn when to use each test double.
5. **Spy** (Activity 5) — Students learn to record interactions with real objects.

Each activity introduces a new concept while reinforcing earlier ones.

---

## Instructor Delivery Notes

- Students should fork or clone the repository.  Do not hand out solutions.
- The production code in `src/` is **off-limits for modification**.  All fixes go in `tests/`.
- Activity 1 (order-dependent failure) may pass or fail depending on test-execution order.  Explain that `pytest` runs tests in definition order by default but may shuffle them with plugins.  The point is that the test is fragile, not that it always fails.
- Activity 2 requires an internet-free environment.  The production `weather_api.py` deliberately raises `ConnectionError` to simulate an offline service.
- Activity 3 is the subtle one — the test **passes**.  Students must read the production code in `megayacht.py` to discover the 28-firings bug, then write an assertion that reveals it.
- The `pytest-mock` package is listed in `requirements.txt` so students have access to the `mocker` fixture, `mocker.spy`, and `mocker.patch`.
