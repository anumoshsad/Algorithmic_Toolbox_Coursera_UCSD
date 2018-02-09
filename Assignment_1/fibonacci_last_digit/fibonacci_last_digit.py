# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    previous = 0
    current  = 1

    for _ in range(n):
        previous, current = current%10, (previous + current)%10

    return previous % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
