def fizz_buzz(n):
        numbers = list(range(1, n + 1))
        for number in numbers:
                if (number % 3 == 0) and (number % 5 == 0):
                        print("FizzBuzz")
                else:
                        if (number % 3 == 0):
                                print("Fizz")
                        else:
                                if (number % 5 == 0):
                                        print("Buzz")
                                else:
                                        print(number)


fizz_buzz(30)