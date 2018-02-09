# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    value_per_weight = [x/y for (x,y) in zip( values, weights)]
    weights = [ x for (y,x) in sorted(zip(value_per_weight, weights))][::-1]
    values = [ x for (y,x) in sorted(zip(value_per_weight, values))][::-1]
    value_per_weight = value_per_weight[::-1]
    
    curr_weight = 0;
    
    for i in range(len(weights)):
        if curr_weight + weights[i] > capacity:
            value += (capacity - curr_weight)/ weights[i] * values[i]
            break
        else:
            value = value + values[i]
            curr_weight += weights[i]
    return value



if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))

