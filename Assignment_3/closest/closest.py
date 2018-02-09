#Uses python3
import sys
from math import sqrt

def minimum_distance(points_x, points_y):
    #write your code here
    N = len(points_x)
    if N <= 4:
        ans, ans_x1, ans_y1, ans_y1, ans_y2 = sqrt((points_x[0][0]-points_x[1][0])**2 + (points_x[0][1]-points_x[1][1])**2), points_x[0][0],points_x[0][1],points_x[1][0],points_x[1][1]
        for i in range(N-1):
            x1, y1 = points_x[i][0], points_x[i][1]
            for j in range(i+1,N):
                x2, y2 = points_x[j][0], points_x[j][1]
                new_d = sqrt((points_x[i][0]-points_x[j][0])**2 + (points_x[i][1]-points_x[j][1])**2)
                if ans > new_d :
                    ans, ans_x1, ans_y1, ans_y1, ans_y2 = new_d, points_x[i][0], points_x[i][1], points_x[j][0], points_x[j][1]
        return (ans, ans_x1, ans_y1, ans_y1, ans_y2)

    else:
        left_x = points_x[:N//2+1]
        right_x = points_x[N//2+1:]
        mid_x = points_x[N//2+1][0]

        left_y = [point for point in points_y if point[0]<= mid_x]
        right_y = [point for point in points_y if point[0] > mid_x]
        (left_d, lx1,ly1,lx2,ly2) = minimum_distance(left_x, left_y)
        (right_d, rx1,ry1,rx2,ry2) = minimum_distance(right_x, right_y)
        (min_d, min_x1, min_y1, min_x2, min_y2) = (right_d, rx1,ry1,rx2,ry2)

        if left_d < right_d:
            (min_d, min_x1, min_y1, min_x2, min_y2) = (left_d, lx1,ly1,lx2,ly2)
        
        near_y = [point for point in points_y if abs(point[0]-mid_x) < min_d]
        num = len(near_y)
        
        (ans, ans_x1, ans_y1, ans_x2, ans_y2) = (min_d, min_x1, min_y1, min_x2, min_y2)

        for i in range(num - 1):
            k = i+1
            while k<= num-1 and near_y[k][1] - near_y[i][1] < min_d:
                new = sqrt((near_y[k][1] - near_y[i][1])**2 + (near_y[k][0] - near_y[i][0])**2)
                if new < ans:
                    (ans, ans_x1, ans_y1, ans_x2, ans_y2) = (new , near_y[k][0], near_y[k][1],near_y[i][0], near_y[i][1])
                k += 1
        return (ans, ans_x1, ans_y1, ans_x2, ans_y2)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    points = list(zip(x,y))
    points_x = sorted(points, key = lambda tuple: tuple[0])
    points_y = sorted(points, key = lambda tuple: tuple[1])
    print("{0:.9f}".format(minimum_distance(points_x, points_y)[0]))
