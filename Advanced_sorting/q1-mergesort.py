import random


def merge(array1, array2):
    merged_array = []
    i, j = 0, 0
    
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            merged_array.append(array1[i])
            i += 1
        else:
            merged_array.append(array2[j])
            j += 1
            
    if i < len(array1):
        merged_array += array1[i:]
    else:
        merged_array += array2[j:]
    return merged_array


def mergeSort(array):
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left_half = mergeSort(array[:mid])
    right_half = mergeSort(array[mid:])
    
    return merge(left_half, right_half)



def testMerge():
    l1, l2 = [], []
    for i in range(6):
        l1.append(random. randint(1, 99))
        l2.append(random. randint(1, 99))
    l2.append(random. randint(1, 99))
    l2.append(random. randint(1, 99))
    l1.sort()
    l2.sort()
    print(l1)
    print(l2)
    print(merge(l1, l2))

def testMergeSort():
    l = []
    for i in range(23):
        l.append(random. randint(1, 99))
    print(l)
    l2 = l[:]
    l2.sort()
    print(l2)
    l2 = mergeSort(l)
    print(l2)


def main():
    testMerge()
    testMergeSort()    

main()
