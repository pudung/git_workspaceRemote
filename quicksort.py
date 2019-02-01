def quick_sort(list):
    arr_length = len(list)
    if arr_length <=1:
        return list
    else:
        pivot = list[0]
        lesser = [element for element in list[1:] if element < pivot]
        greater = [element for element in list[1:] if element > pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)

# 리스트를 입력받아서 quick_sort
print("원소의 갯수를 입력해주세요 1<= n <= 1000\n")
list = []
size = input()
for i in range(0,int(size)):
    list.append(int(input()))
print(quick_sort(list))

print("last commit")