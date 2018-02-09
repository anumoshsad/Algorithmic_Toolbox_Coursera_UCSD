# Uses python3
import sys

def gcd(a, b):
    x, y = max(a,b), min(a,b)
    if y == 0: return x
    else :return gcd(y, x%y)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
