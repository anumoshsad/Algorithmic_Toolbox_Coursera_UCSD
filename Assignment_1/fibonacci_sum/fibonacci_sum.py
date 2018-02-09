# Uses python3
import sys

def fibonacci_sum(n):
    n, m = n +2 , 10
    previous = 0
    current  = 1
    memo = [0]
    while True:
        previous, current = current%m , (previous + current)% m
        if (previous, current) == (0, 1):
            return (memo[n%(len(memo))]-1)%10
        memo.append(previous)

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))
