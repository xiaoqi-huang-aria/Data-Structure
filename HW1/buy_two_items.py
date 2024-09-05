def buy_two_items(credit, list1):
    """
    @credit: integer, you want to spend this total amount, exactly.
    @list1: list of integers.

    remember to mention your runtime as comment!
    # TODO
    My runtime is: O(n^2)

    @return: a tuple of two integers. They should sum up to credit. (Order doesn't matter)
    """
    for i in range(len(list1)):
        for j in range(i + 1, len(list1)):
            if list1[i] + list1[j] == credit:
                return (list1[i], list1[j])



'''
Note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''


def main():
    print(buy_two_items(200, [150, 24, 79, 50, 88, 345, 3]))
    print(buy_two_items(295, [678, 227, 764, 37, 956, 982, 118, 212, 177, 597, 519, 968, 866, 121, 771, 343, 561]))


if __name__ == '__main__':
    main()
