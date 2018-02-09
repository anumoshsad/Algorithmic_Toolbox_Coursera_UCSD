# Uses python3
def edit_distance(s, t):
        #write your code here
        m, n = len(s), len(t)
        E = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(m+1):
            E[i][0]=i
        for j in range(1,n+1):
            E[0][j] = j
        for i in range(1,m+1):
            for j in range(1,n+1):
                E[i][j] = min(1+E[i-1][j], 1+E[i][j-1], diff(s[i-1],t[j-1])+E[i-1][j-1])
        return E[m][n]

def diff(i, j):
        return i != j

if __name__ == "__main__":
        print(edit_distance(input(), input()))
