#Uses python3

import sys

def largest_number(a):
    #write your code here
    res = ""
    while a!=[]:
        maxNum = ""
        for num in a:
            if IsGreaterOrEqual(num, maxNum):
                maxNum = num
        #print(num, maxNum)
        maxNum = maxNum
        res += maxNum
        #print(maxNum)
        a.remove(maxNum)
    return int(res)

def IsGreaterOrEqual(num, maxNum):
    if int(num+maxNum)>=int(maxNum+num):return True
    else: return False

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
