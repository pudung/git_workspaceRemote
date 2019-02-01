
def test(list,value):
    i = 0
    while i < len(list):
        if list[i] == value:
            return True
        i = i + 1
    return False

print(test([1,2,3,4,5,6,7],8))