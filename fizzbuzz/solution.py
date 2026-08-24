"""
Kata:
URL:
Kyu:
"""


def solve(num):
    if num % 5 == 0 and num % 3 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)


if __name__ == "__main__":
    pass
