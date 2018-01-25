

def tripleStep(n):
    array = [-1] * (n + 1)
    return countWays(n, array)

def countWays(n, array):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif array[n] > -1:
        return array[n]
    else:
        array[n] = countWays(n-1,array) + countWays(n-2,array) + countWays(n-3,array)
        return array[n]

print(tripleStep(4))