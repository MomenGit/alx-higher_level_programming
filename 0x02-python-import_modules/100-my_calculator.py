#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    from sys import argv
    ops_dic = {'+': calc.add, '-': calc.sub, '*': calc.mul, '/': calc.div}
    ops = ['+', '-', '*', '/']
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    try:
        ops.index(argv[2])
    except ValueError:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{0} {1} {2} = {3}".format(argv[1], argv[2],
          argv[3], ops_dic[argv[2]](int(argv[1]), int(argv[3]))))
