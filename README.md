# MLOps Lab 1

DADS7305, Northeastern University
Jaiyashree Vinaitheertha Kumaravelu

A small calculator module used to practice the basics of a reproducible Python workflow: isolated environments, unit testing with pytest and unittest, and CI through GitHub Actions.

## Layout

```
.github/workflows/    CI workflows (pytest, unittest)
data/                 placeholder, unused in this lab
src/calculator.py     fun1 to fun4: add, subtract, multiply, and their sum
test/                 test_pytest.py, test_unittest.py
requirements.txt
```

## Running locally

```
python -m venv lab_01
lab_01\Scripts\activate
pip install -r requirements.txt
python -m pytest
python -m unittest test.test_unittest
```

Run from the repo root so `src` resolves as a package. Note that pytest also collects the unittest cases, so it reports 11 tests rather than 7.

## CI

Both workflows trigger on push to `main`. The pytest workflow writes a JUnit XML report and uploads it as the `test-results` artifact, so results can be inspected even if the run fails.

## Changes from the lab handout

- Updated `actions/checkout`, `actions/setup-python`, and `actions/upload-artifact` to current major versions. `upload-artifact@v2` is no longer supported and fails outright.
- Python 3.11 in CI instead of 3.8, which is end of life and not available on current Ubuntu runners.
- Added `__init__.py` to `src/` and `test/` so imports work the same under pytest, unittest, and CI.
- Artifact upload uses `if: always()` so the report is kept on failing runs too.