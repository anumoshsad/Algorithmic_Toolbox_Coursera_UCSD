# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    #write your code here
        (D, op) = pp(dataset)
        n = len(D)-1
        MIN = [[0 for i in range(n+1)] for j in range(n+1)]
        MAX = [[0 for i in range(n+1)] for j in range(n+1)]
        
        for i in range(1,n+1):
            MIN[i][i],MAX[i][i] = D[i],D[i]
        for s in range(1,n):
            for i in range(1,n-s+1):
                j = i+s
                m, M = float('inf'),-float('inf')
                for k in range(i, j):
                    a = evalt(MAX[i][k], MAX[k+1][j],op[k])
                    b = evalt(MAX[i][k], MIN[k+1][j],op[k])
                    c = evalt(MIN[i][k], MAX[k+1][j],op[k])
                    d = evalt(MIN[i][k], MIN[k+1][j],op[k])
                    m = min(m,a,b,c,d)
                    M = max(M,a,b,c,d)
                MIN[i][j],MAX[i][j] = m, M
        return MAX[1][n]

def pp(string):
        d = [0]
        op = ['']
        start = 0
        for i in range(len(string)):
                if string[i] == '+':
                    op.append('+')
                    d.append(int(string[start:i]))
                    start = i+1
                if string[i] == '*':
                    op.append('*')
                    d.append(int(string[start:i]))
                    start = i+1
                if string[i] == '-':
                    op.append('-')
                    d.append(int(string[start:i]))
                    start = i+1
        d.append(int(string[start:]))
        return (d,op)


if __name__ == "__main__":
    print(get_maximum_value(input()))
