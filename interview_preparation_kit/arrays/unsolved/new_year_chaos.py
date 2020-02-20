def minimumBribes(q):
    n = len(q)
    sumBribe = 0
    i = 0

    while(i < n and i >= q[i]-1-2):
        if(i <= q[i]-1):
            sumBribe = sumBribe + q[i] - i - 1
        
        i = i+1
    if(i == n):
        print(sumBribe)
    else:
        print("Too chaotic")