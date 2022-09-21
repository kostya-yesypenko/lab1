import argparse
import operator


def main():
    # parse arguments
    parser = argparse.ArgumentParser(description='doc')
    parser.add_argument("function", help="Python function to run.")
    parser.add_argument('integer1', metavar='N', type=int, help='an integer for the accumulator')
    parser.add_argument('integer2', metavar='N', type=int, help='an integer for the accumulator')
    args = parser.parse_args()

    # try to get the function from the operator module
    try:
        func = getattr(operator, args.function)
    except:
        print('not correct function')

    # run the function and pass in the args, print the output to stdout
    print(func(args.integer1, args.integer2))


main()