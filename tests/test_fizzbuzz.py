from lib.fizzbuzz import *
# when number divisible by 3 return "fizz" DONE
# when number divisible by 5 return "buzz" DONE
# when number divisible by 3 and 5 return "fizzbuzz" DONE
# if neither, return the number 

def test_fizzbuzz_with_3_returns_fizz():
    expected = "fizz"

    actual = fizzbuzz(3)

    assert expected == actual

def test_fizzbuzz_with_5_returns_buzz():
    expected = "buzz"

    actual = fizzbuzz(5)

    assert expected == actual

def test_fizzbuzz_with_30_returns_fizzbuzz():
    expected = "fizzbuzz"

    actual = fizzbuzz(30)

    assert expected == actual

def test_fizzbuzz_with_7_returns_7():
    expected = 7

    actual = fizzbuzz(7)

    assert expected == actual

