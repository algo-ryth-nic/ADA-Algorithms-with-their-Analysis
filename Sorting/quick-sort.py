from timeit import default_timer as timer

def quick_sort(arr, lower_bound, upper_bound):

    # base case
    if upper_bound - lower_bound <= 1:
        return arr

    # pivot is the first element
    pivot = arr[lower_bound]
    left = lower_bound + 1
    right = upper_bound

    # partitioning subroutine, O(n)
    while left<=right:
        if arr[left] < pivot:
            left += 1
        elif arr[right] >= pivot:
            right -= 1
        else:
            # swapping
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    # swapping the pivot with the "right" index, now the pivot is in its "sorted"/"final" position
    arr[lower_bound], arr[right] = arr[right], arr[lower_bound]

    pivot_index = right

    # recursively solving for both/all the sublists
    quick_sort(arr, lower_bound, pivot_index-1);         # 1st half/branch
    quick_sort(arr, pivot_index+1, upper_bound);         # 2nd half/branch

    return arr

arr = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
start = timer()
sorted_arr = quick_sort(arr, 0, len(arr)-1)
end = timer()
print(f">> Sorted Array: {sorted_arr}")
print(f"[Time Taken] {end-start}ms")
