#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    from calculator_1 import add, sub, mul, div
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = ["+", "-", "*", "/"]
    for i in operator:
        if sys.argv[2] not in operator:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            if sys.argv[2] == "+":
                print(a, sys.argv[2], b, "=", add(a, b))
                exit(0)
            elif sys.argv[2] == "-":
                print(a, sys.argv[2], b, "=", sub(a, b))
                exit(0)
            elif sys.argv[2] == '*':
                print(a, sys.argv[2], b, "=", mul(a, b))
                exit(0)
            elif sys.argv[2] == "/":
                print(a, sys.argv[2], b, "=", div(a, b))
                exit(0)
