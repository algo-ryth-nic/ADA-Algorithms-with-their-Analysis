def selection_sort(arr):
    swaps = 0
    for l in range(0, len(arr)-1):    #
        key_index = l

        # searching for min/max element
        for i in range(l+1, len(arr)):
            if arr[key_index] >= arr[i]:
                key_index = i
        else:
            # swapping
            arr[l], arr[key_index] = arr[key_index], arr[l]
            swaps += 1

    #print(swaps)
    return arr

print(selection_sort([29,10,14,37,13,3]))
