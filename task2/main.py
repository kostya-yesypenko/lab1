import argparse
import operator
import math

arg = argparse.ArgumentParser()
arg.add_argument('operator', type=str)
arg.add_argument('values', nargs="*", type=int)
args = arg.parse_args()

def main(oper, *num):
    if hasattr(operator, oper):
        calc = getattr(operator, oper)
        return calc(*num)
    elif hasattr(math, oper):
        calc = getattr(operator, oper)
        return calc(*num)
    else:
        print('Wrong input')



print(main(args.operator, *args.values))