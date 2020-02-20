def rotLeft(a, d):
    n = len(a)
    tmp = [-1] * n

    for i in range(0, n):
        index = (i-d)%n
        tmp[index] = a[i]

    return tmp