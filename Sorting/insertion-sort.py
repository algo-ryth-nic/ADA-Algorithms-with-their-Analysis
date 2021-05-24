def insertion_sort(list):
    for index in range(1,len(list)):
        key = list[index]
        previousIndex = index - 1
        while list[previousIndex] > key and previousIndex >= 0:
            # swapping position
            temp = key
            list[previousIndex+1] = list[previousIndex]
            list[previousIndex] = temp
            previousIndex -= 1

    return list

print("[Array]", [29,10,14,37,13,3])
arr = insertion_sort([29,10,14,37,13,3])
print(f">> Sorted: {arr}")
