# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    cnt = {p:0 for p in points}
    pointset = set(points)
    All = [(l,-1) for l in starts] + [(r,1) for r in ends] + [(p,0) for p in pointset]
    #write your code here
    All.sort()
    c = 0
    #print(All)
    for i in range(len(All)):
        p, id = All[i][0], All[i][1]
        if id != 0 :
            c += -id
        elif id == 0:
            cnt[p] += c
        
    #print(segments[index], p, i)
    return [cnt[i] for i in points]


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
