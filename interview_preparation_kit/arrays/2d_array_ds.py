def hourglassSum(arr):

    maxSum = -sys.maxsize-1

    for i in range(0, len(arr)-2):
        for j in range(0, len(arr[i])-2):
            tmpSum = arr[i][j] + arr[i][j+1] + arr[i][j+2]+ arr[i+1][j+1] + arr[i+2][j]+arr[i+2][j+1] + arr[i+2][j+2]
            
            if(maxSum < tmpSum):
                maxSum = tmpSum

    return maxSum