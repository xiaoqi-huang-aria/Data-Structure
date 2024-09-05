def has_duplicate(list1):
    """
    remember to mention your runtime as comment!
    # TODO
    My runtime is: O(n^2)

    :param list1: List -- list of integers
    :return: True if list1 has duplicate, return False otherwise.
    """
    
    for i in range(len(list1)):
        for j in range(i + 1, len(list1)):
            if list1[i] == list1[j]:
                return True
    return False


'''
Note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''


# def main():
#     print(has_duplicate([0, 6, 2, 4, 9]))  # False

#     print(has_duplicate([0, 6, 2, 4, 9, 1, 2]))  # True


# if __name__ == '__main__':
#     main()
