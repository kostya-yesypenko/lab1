import argparse
import operator
import math

arg = argparse.ArgumentParser()
arg.add_argument('operator', type=str)
arg.add_argument('values', nargs="*", type=int)
args = arg.parse_args()

def main(oper, *num):
    try:
        if hasattr(operator, oper):
            calc = getattr(operator, oper)
            return calc(*num)
        elif hasattr(math, oper):
            calc = getattr(operator, oper)
            return calc(*num)
        else:
            print('Wrong input')
    except ZeroDivisionError:
        pass



print(main(args.operator, *args.values))