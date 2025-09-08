#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):  # creates sequence
        if i % 3 == 0 and i % 5 == 0:  # divisible by 3 and 5, two conditions
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:  # divisible by 3 only
            print("Fizz", end=" ")
        elif i % 5 == 0:  # divisible by 5 only
            print("Buzz", end=" ")
        else:  # not divisible by 3 or 5, print the number
            print(i, end=" ")
