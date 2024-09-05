import random


def either_or_sort(array):
    """ EitherOr sort arranges all of the zeros in array at the front, before all of the ones.
        It must perform the sorting in-place, and its complexity must be in O(N).
        @array: the python list being sorted
    """
    left = 0
    right = len(array) - 1

    while left <= right:
        if array[left] == 1 and array[right] == 0:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
        if array[left] == 0:
            left += 1
        if array[right] == 1:
            right -= 1


def main():
    array = []
    for i in range(20):
        array.append(random.randint(0, 1))

    print("Before sorting:")
    print(array)
    either_or_sort(array)
    print("After sorting:")
    print(array)


if __name__ == "__main__":
    main()
