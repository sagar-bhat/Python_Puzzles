def maxSubArraySum(arr, size):
    '''
    Returns the maximum sum of
    the subArrays found in the
    given array.
 
    '''

    max_sum = arr[0]
    summ = 0
      
    for i in range(size):
        summ = summ + arr[i]
        if (max_sum < summ):
            max_sum = summ
 
        if summ < 0:
            summ = 0
  
    return max_sum

if __name__ == '__main__':

    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    #arr = [-2, -5, -3, -1, -4]
    print maxSubArraySum(arr,len(arr))
