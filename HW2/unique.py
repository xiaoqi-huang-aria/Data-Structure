def unique(s):
    """
    :param s: List[Any] -- list of values.
    :return: True if all values within s are unique.
             False otherwise.
    """
    def unique_recursive(s, start):
        if start >= len(s) - 1:
            return True
        for i in range(start + 1, len(s)):
            if s[start] == s[i]:
                return False
        return unique_recursive(s, start + 1)

    return unique_recursive(s, 0)
        


def main():
    print(unique([1, 7, 6, 5, 4, 3, 1]))  # False
    print(unique([9, 4, 3, 2, 1, 8]))  # True
    print(unique(['9', [], 4, 3, 2, 1, 8]))  # True


if __name__ == '__main__':
    main()
