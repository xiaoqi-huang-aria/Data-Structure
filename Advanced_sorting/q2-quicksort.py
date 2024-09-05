comparisons = 0
swaps = 0

def medianOfThree(S, a, b):
    mid = (a + b) // 2
    temp = [S[a], S[mid], S[b]]
    if temp[0] > temp[1]:
        temp[0], temp[1] = temp[1], temp[0]
    if temp[1] > temp[2]:
        temp[2], temp[1] = temp[1], temp[2]
    if temp[0] > temp[1]:
        temp[0], temp[1] = temp[1], temp[0]
    S[b] = temp[1]
    S[a] = temp[0]
    S[mid] = temp[2]



def inplace_quick_sort(S, a, b):
    global comparisons
    global swaps

    """Sort the list from S[a] to S[b] inclusive using the quick-sort algorithm."""
    if a >= b: return                                      # range is trivially sorted
    medianOfThree(S, a, b)
    pivot = S[b]                                           # last element of range is pivot
    left = a                                               # will scan rightward
    right = b-1                                            # will scan leftward
    while left <= right:
        # scan until reaching value equal or larger than pivot (or right marker)
        while left <= right and S[left] < pivot:
            comparisons += 2
            left += 1
        # scan until reaching value equal or smaller than pivot (or left marker)
        while left <= right and pivot < S[right]:
            comparisons += 2
            right -= 1
        if left <= right:                                    # scans did not strictly cross
            swaps += 1
            comparisons += 1
            S[left], S[right] = S[right], S[left]              # swap values
            left, right = left + 1, right - 1                  # shrink range
            
    # put pivot into its final place (currently marked by left index)
    swaps += 1
    S[left], S[b] = S[b], S[left]
    # make recursive calls
    inplace_quick_sort(S, a, left - 1)
    inplace_quick_sort(S, left + 1, b)

def main():
    import random
    S = []
    for i in range(10):
        S.append(random.randint(0, 100))

    print(S)
    inplace_quick_sort(S, 0, len(S) - 1)
    print(S)
    print("Is S sorted???", S == sorted(S))
    print("comparisons:", comparisons)
    print("swaps:", swaps)
main()