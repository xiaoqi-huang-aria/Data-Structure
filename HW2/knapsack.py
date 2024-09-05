import copy


def knapsack_driver(capacity, weights):
    """
    @capacity: positive integer. the value we are summing up to.
    @weights:  list of positive integers.

    ### Friendly tip: This function can't solve the problem,
    ### you need more parameters to pass information between recursive functions.
    ### So, define another function!! Return the result from your new function!!

    @return: List of all combinations that can add up to capacity.
    """
    def recursive_knapsack(capacity, weights, current_combination, index, result):
        if capacity == 0:
            result.append(copy.deepcopy(current_combination))
            return
        if capacity < 0 or index == len(weights):
            return
        
        current_combination.append(weights[index])
        recursive_knapsack(capacity - weights[index], weights, current_combination, index + 1, result)
        
        current_combination.pop()
        recursive_knapsack(capacity, weights, current_combination, index + 1, result)

    result = []
    recursive_knapsack(capacity, weights, [], 0, result)
    return result


def main():
    casts = [1, 2, 8, 4, 9, 1, 4, 5]
    # order does not matter, inner values order doesn't matter either. [[9, 5], [9, 1, 4], [4, 1, 4, 5], [4, 9, 1],
    # [8, 1, 5], [2, 8, 4], [2, 8, 4], [1, 9, 4], [1, 4, 4, 5], [1, 4, 9], [1, 8, 5], [1, 8, 1, 4], [1, 8, 4, 1]]
    print(knapsack_driver(14, casts))


if __name__ == '__main__':
    main()
