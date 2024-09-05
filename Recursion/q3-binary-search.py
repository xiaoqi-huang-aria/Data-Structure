import random

def binarySearch(array, element):
    return recursiveBinarySearch(array, 0, len(array) - 1, element)

def recursiveBinarySearch(array, low_index, high_index, element):
    if low_index > high_index:
        return -1
    mid = (low_index + high_index) // 2
    if array[mid] == element:
        return mid
    elif array[mid] < element:
        return recursiveBinarySearch(array, mid + 1, high_index, element)
    else:
        return recursiveBinarySearch(array, low_index, mid - 1, element)
    

def main():
    l = []
    for i in range(20):
        l.append(random. randint(1, 99))
    l.sort()
    print(l)
    print(binarySearch(l, l[5]))
    print(binarySearch(l, l[0]))
    print(binarySearch(l, l[19]))
    print(binarySearch(l, 22))

main()
