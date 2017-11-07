def is_sum_possible_unsorted(arr, k):

    pair = []
    prevset = []

    for i in range(len(arr)):
        if prevset is not None:
            if (k - arr[i]) in prevset:
                pair.append([k - arr[i], arr[i]])
        prevset.append(arr[i])

    return pair 
        

def is_sum_possible_sorted(arr, k):

    pair = []

    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if (i != j) and (arr[i]+arr[j] == k):
                pair.append([arr[i],arr[j]])
            elif (arr[i]+arr[j] > k):
                break

    return pair

if __name__ == '__main__':

    arr = [1, -4, 6, 13, 18, 8]
    k = 14
    print is_sum_possible_unsorted(arr, k)

    arr = [-7, -4, 5, 6, 13, 18]
    k = 11
    print is_sum_possible_sorted(arr, k)
