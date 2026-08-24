"""
test_solution.py

A pytest primer, since you're learning it as you go:

- pytest finds any function in a file named test_*.py whose name starts
  with `test_` and treats it as a test. No test-class or registration
  needed - it's all just discovery by naming convention.
- Use plain `assert <expression>`. No special assertion methods required -
  pytest rewrites asserts so a failure shows you both sides, e.g.
  "assert 3 == 4" rather than just "AssertionError".
- Run everything for this kata:        cw run
- Run this file directly:              pytest -v test_solution.py
- Run only tests matching a name:      pytest -v -k edge_case
- Stop at the first failure:           pytest -x

Replace the example tests below with real cases from the kata description
(and a few edge cases of your own) before you start implementing.
"""

from solution import solve


def test_example_case():
    # Copy the example(s) given in the kata description first.
    assert solve(1) == "1"
    assert solve(3) == "Fizz"
    assert solve(5) == "Buzz"


def test_edge_case():
    # Then think about what could break it: 0, negatives, empty input,
    # duplicates, very large input, etc.
    assert solve(15) == "FizzBuzz"


# --- Parametrized tests -----------------------------------------------
# pytest.mark.parametrize runs the same test body once per (input,
# expected) pair, instead of you writing a near-identical test function
# for each case. Handy once you've got a handful of example cases from
# the kata description. Uncomment and adapt:
#
# import pytest
#
# @pytest.mark.parametrize("args,expected", [
#     ((1, 2), 3),
#     ((0, 0), 0),
#     ((-1, 1), 0),
# ])
# def test_parametrized(args, expected):
#     assert solve(*args) == expected


# --- Fixtures ------------------------------------------------------------
# A fixture is a function decorated with @pytest.fixture that sets up
# something a test needs (data, an object, a temp file...) and hands it
# to the test as an argument matching the fixture's name. pytest wires
# this up automatically - no imports of the fixture needed in the test.
# Most katas won't need one, but here's the shape for when a kata takes
# a more complex input object:
#
# @pytest.fixture
# def sample_grid():
#     return [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
#
# def test_with_fixture(sample_grid):
#     assert solve(sample_grid) == 5
