# TEST_STATUS.md

Test-suite smoke-test results.  Run with `python -m pytest tests/ -v`.

**Total tests:** 11  
**Passing:** 7  
**Failing:** 4

---

## test_salt_flat.py

| Test | Status |
|---|---|
| `test_truck_launches_on_dry_surface` | PASSING |
| `test_oil_spill_makes_launch_unsafe` | PASSING |
| `test_crew_repairs_truck_and_re_checks_track` | FAILING |

**Failing reason:** One test mutates `TrackEnvironment.friction_coefficient` to `0.1` and never restores it.  A subsequent test that expects the default value (`0.85`) runs with the contaminated value, so `can_launch()` returns `False` and the assertion fails.  The failure is order-dependent — the test passes when run in isolation.

---

## test_helicopter.py

| Test | Status |
|---|---|
| `test_rotor_pitch_baseline_in_calm_wind` | FAILING |
| `test_rotor_pitch_increases_with_headwind` | FAILING |
| `test_severe_crosswind_requires_aggressive_pitch` | FAILING |

**Failing reason:** All three tests call `AttackHelicopter.calculate_rotor_pitch()`, which delegates to `get_live_wind_speed()`.  The production implementation raises `ConnectionError` because the external weather service (bom.gov.au) is unreachable.

---

## test_megayacht.py

| Test | Status |
|---|---|
| `test_megayacht_clears_the_ramp` | PASSING |

**Note:** This test passes despite a production bug.  It only asserts on the return value (`"SUCCESS"`) and never inspects how many times the thruster fired.  The production function `trigger_ramp_jump()` fires the thruster 28 times due to a retry loop instead of the expected single firing.

---

## test_canyon_chase.py

| Test | Status |
|---|---|
| `test_canyon_chase_insurance_processed` | PASSING |

**Note:** This test verifies that `get_engine_temperature` was called once, but never checks whether `wire_insurance_funds` was called with the correct arguments.  The test verifies telemetry behaviour while ignoring the insurance payment that it is supposed to protect.

---

## test_interceptor.py

| Test | Status |
|---|---|
| `test_interceptor_cuts_ignition_on_shutdown` | PASSING |
| `test_interceptor_engages_supercharger_for_pursuit` | PASSING |
| `test_shutdown_sequence_fires_both_ecu_methods` | PASSING |

**Note:** All three tests directly mock `LegacyECUDriver`, replacing the vendor-supplied binary with a `MagicMock`.  The real ECU behaviour is never exercised.  The third test verifies that both methods were called but cannot check the order in which they fired.  If the vendor firmware changes its interface the mocks will remain green while the real code breaks.
