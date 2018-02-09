# Uses python3
import sys

#def get_majority_element(a, left, right):
#    if left == right:
#       return -1
#   if left + 1 == right:
#       return a[left]
#   #write your code here
#   return -1

def get_majority_element(a):
    a = sorted(a)
    from collections import Counter
    d = Counter(a)
    if max([d[i] for i in d])> len(a)//2: return 1
    else: return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_majority_element(a))

