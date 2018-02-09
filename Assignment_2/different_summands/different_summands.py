# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    if n<=2: summands.append(n)
    else:
        summands.append(1)
        n = n - 1
        s = sum(summands)
        l = 2
        while l<=n:
            if n<=2*l :
                summands.append(n)
                break
            else:
                summands.append(l)
                n,l = n-l, l+1
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
