import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-W", type=int)
parser.add_argument("-w", type=int, nargs="+")
args = parser.parse_args()

capacity = args.W
weight = args.w

num = []

def knapsack(capacity, weight, inside=[]):
    s = sum(inside)
    if s <= capacity:
        num.append(s)
    for i in range(len(weight)):
        n = weight[i]
        left = weight[i+1:]
        knapsack(capacity, left, inside+[n])

knapsack(args.W, args.w)
print(max(num))