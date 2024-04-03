from lib.fizzbuzz import *
# when number divisible by 3 return "fizz"
# when number divisible by 5 return "buzz"
# when number divisible by 3 and 5 return "fizzbuzz"
# if neither, return the number

def test_fizzbuzz_with_3_returns_fizz():
    expected = "fizz"

    actual = fizzbuzz(3)

    assert expected == actual