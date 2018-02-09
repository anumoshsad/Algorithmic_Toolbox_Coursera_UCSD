# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    if n==1: return [n]
    q = {1:[1]}
    for i in range(2,n+1):
        #print(i)
        m = len(q[i-1])
        s = q[i-1][:]
        if i % 2 == 0 and len(q[i//2]) < m:
            m = len(q[i//2])
            s = q[i//2][:]
        if i % 3 == 0 and i>=3 and len(q[i//3]) < m:
            m = len(q[i//3])
            s = q[i//3][:]
        s.append(i)
        q[i] = s
    #print(q)
    return q[n]

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
