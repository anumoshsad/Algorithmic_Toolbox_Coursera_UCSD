# Uses python3
import sys

def get_change(m):
    #write your code here
    n = m//10
    m = m-n*10
    n += m//5
    m = m- (m//5)*5
    n += m
    return n

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
