def fizzbuzz(number):
    if (number % 3 == 0) and (number % 5 == 0):
        return "fizzbuzz"
    elif number % 5 == 0:
        return "buzz"
    elif number % 3 == 0:
        return "fizz"
    else:
        return number