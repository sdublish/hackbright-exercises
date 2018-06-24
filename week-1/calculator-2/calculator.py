"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

while True:
    user_input = input("> ")
    if user_input == "q":
        break

    numbers = user_input.split(" ")
    func = numbers[0]
    float_num = []

    for i in numbers[1:]:
        float_num.append(float(i))


    if func == "+":
        print(add(float_num))
    elif func == "-":
        print(subtract(float_num))
    elif func == "*":
        print(multiply(float_num))
    elif func == "/":
        print(divide(float_num))
    elif func == "square":
        print(square(float_num))
    elif func == "cube":
        print(cube(float_num))
    elif func == "pow":
        print(power(float_num))
    elif func == "mod":
        print(mod(float_num))


# Your code goes here
