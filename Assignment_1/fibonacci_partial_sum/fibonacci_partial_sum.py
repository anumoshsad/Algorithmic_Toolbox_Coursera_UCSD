# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    n2, n1, m = from_ + 1 , to + 2, 10
    previous = 0
    current  = 1
    memo = [0]
    while True:
        previous, current = current%m , (previous + current)% m
        if (previous, current) == (0, 1):
            return (memo[n1%(len(memo))]-memo[n2%(len(memo))])%m
        memo.append(previous)


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
