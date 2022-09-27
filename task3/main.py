import argparse

parser=argparse.ArgumentParser()
parser.add_argument('expression',type=str, nargs='?', const='')
args=parser.parse_args()

def is_correct(str):
    if str=='':
        print("False, None")
        return False
    counter=0
    for i in str:
        if counter>1:
            print("False, None")
            return False
        if i.isdigit()==0 and (i!='+' or i!='-'):
            print("False, None")
            return False
        elif i.isdigit()==0:
            counter += 1
        else:
            counter=0
    print("True, {0}".format(eval(str)))


if __name__=='__main__':
    try:
        is_correct(args.expression)
    except:
        print("False, None")



