# Uses python3
import sys

def optimal_weight(W, w, n):
    # write your code here
    q = []
    for i in range(W+1):
        q.append(0)
    
    for j in range(n):
        temp = [0]*(W+1)
        for i in range(W+1):
            if w[j] > i: temp[i] = q[i]
            else:
                temp[i] = max(q[i], q[i-w[j]]+w[j])
        q = temp
    return q[W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w, n))
