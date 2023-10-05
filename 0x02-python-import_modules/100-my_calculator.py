#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, div, sub, mul

    if (len(sys.argv) - 1) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    oper = sys.argv[2]
    if oper != '+' and oper != '-' and oper != '*' and oper != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if sys.argv[2] == '+':
        print(f"{a} + {b} = {add(a, b)}")

    elif sys.argv[2] == '-':
        print(f"{a} - {b} = {sub(a, b)}")

    elif sys.argv[2] == '*':
        print(f"{a} * {b} = {mul(a, b)}")

    else:
        print(f"{a} / {b} = {div(a, b)}")
