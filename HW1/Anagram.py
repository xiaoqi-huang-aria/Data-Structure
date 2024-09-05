import re

def anagram(string1, string2):
    """
    :param string1: String -- the first python string.
    :param string2: String -- the second python string.

    :return: True if string1 is anagram of string2
             False otherwise.
    """
    # To do
    regex = re.escape(" \\/.,()[]")
    s1 = re.sub(f"[{regex}]", '', string1).lower()
    s2 = re.sub(f"[{regex}]", '', string2).lower()
    
    count1 = {}
    count2 = {}
    
    for char in s1:
        if char in count1:
            count1[char] += 1
        else:
            count1[char] = 1
    
    for char in s2:
        if char in count2:
            count2[char] += 1
        else:
            count2[char] = 1

    return count1 == count2


'''
note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''


# def main():
#     string1 = "william shakespeare"
#     string2 = "i am a weakish speller"
#     print(anagram(string1, string2))

#     string1 = "software"
#     string2 = "swear oft"
#     print(anagram(string1, string2))


# if __name__ == '__main__':
#     main()
