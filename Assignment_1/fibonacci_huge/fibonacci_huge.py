# Uses python3
import sys

def get_fibonacci_huge(n, m):
    previous = 0
    current  = 1
    memo = [0]
    while True:
        previous, current = current%m , (previous + current)% m
        if (previous, current) == (0, 1):
            return memo[n%(len(memo))]
        memo.append(previous)

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
