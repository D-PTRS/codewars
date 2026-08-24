import solution as s


def test_example_case():
    assert s.solve(1) == "1"
    assert s.solve(3) == "Fizz"
    assert s.solve(5) == "Buzz"
    assert s.solve(15) == "FizzBuzz"
