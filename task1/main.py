import argparse


parser=argparse.ArgumentParser()
parser.add_argument('first', type=int)
parser.add_argument('operation', type=str)
parser.add_argument('second', type=int)

args=parser.parse_args()

def easy_math(first,operation,second):
    if operation =="+":
        print(first + second)
    elif operation =="-":
        print(first - second)
    elif operation =="*":
        print(first * second)
    elif operation =="/":
        if second==0:
            print("Can't divide by zero")
            return False
        print(first / second)

if __name__=='__main__':
    easy_math(args.first,args.operation,args.second)