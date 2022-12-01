#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    cal = argv[2]
    if cal != '+' and cal != '-' and cal != '*' and cal != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if cal == '+':
        print("{} {} {} = {}" .format(a, cal, b, add(a, b)))
    elif cal == '-':
        print("{} {} {} = {}" .format(a, cal, b, sub(a, b)))
    elif cal == '*':
        print("{} {} {} = {}" .format(a, cal, b, mul(a, b)))
    else:
        print("{} {} {} = {}" .format(a, cal, b, div(a, b)))
