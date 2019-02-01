def quick_sort(list):
    arr_length = len(list)
    if arr_length <=1:
        return list
    else:
        pivot = list[0]
        lesser = [element for element in list[1:] if element < pivot]
        greater = [element for element in list[1:] if element > pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)

print(quick_sort([5,8,6,2,4]))