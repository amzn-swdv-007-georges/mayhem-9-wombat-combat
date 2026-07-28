# AutoDirector

AutoDirector is a stunt coordination system for high-budget action
films.  It manages vehicle dispatch, weather integration, hardware
actuation, and insurance workflows across multiple stunt units.

---

## Project Overview

The software coordinates the climax stunt sequence of *Mayhem 9:
Wombat Combat*, an action film featuring four stunt vehicles:

- **Monster Truck** ("Grave Digger") — ramp-to-ramp launch on the
  Bonneville Salt Flats.
- **Attack Helicopter** ("Apache-1") — low-altitude rotor
  manoeuvres in variable wind conditions.
- **Megayacht** — water-ramp jump triggered by an on-board thruster.
- **Pursuit Interceptor** ("Pursuit-1") — high-speed chase vehicle
  running a vendor-supplied engine control unit.

The system also integrates with the Australian Bureau of Meteorology
for live wind data, a hardware thruster actuator, and an automated
insurance-liquidity pipeline.

---

## Installation

Create a virtual environment and install the project in editable mode:

```bash
python3 -m venv .venv
source .venv/bin/activate   # Linux / macOS
# .venv\Scripts\activate    # Windows

pip install -e .
pip install -r requirements.txt
```

---

## Running Tests

Execute the full test suite from the repository root:

```bash
python -m pytest tests/ -v
```

To run a single activity file:

```bash
python -m pytest tests/test_salt_flat.py -v
```

---

## Repository Structure

```
mayhem-9-wombat-combat/
├── README.md
├── INSTRUCTOR_NOTES.md
├── TEST_STATUS.md
├── requirements.txt
├── pyproject.toml
├── .gitignore
│
├── src/                        # Production code
│   ├── __init__.py
│   ├── environment.py          # Track surface conditions
│   ├── weather_api.py          # External weather service client
│   ├── finance.py              # Insurance transfers & telemetry
│   ├── hardware.py             # Physical thruster actuator
│   ├── legacy.py               # Vendor-supplied ECU driver
│   ├── vehicles/
│   │   ├── __init__.py
│   │   ├── truck.py
│   │   ├── helicopter.py
│   │   ├── megayacht.py
│   │   └── interceptor.py
│   └── stunts/
│       ├── __init__.py
│       └── orchestrator.py     # Climax sequence coordinator
│
└── tests/                      # Test suite
    ├── __init__.py
    ├── test_salt_flat.py
    ├── test_helicopter.py
    ├── test_megayacht.py
    ├── test_canyon_chase.py
    └── test_interceptor.py
```

---

## Safety Warning

This repository is used for **software-testing education**.  Some
tests contain deliberate architectural flaws that serve as lesson
objectives.  Do not deploy this code to a production environment.  If
you are a student, read `INSTRUCTOR_NOTES.md` for activity details.
