def palindrome_recursive(string, index):
    if index >= len(string) // 2:
        return True
    if string[index] != string[-(index + 1)]:
        return False
    return palindrome_recursive(string, index + 1)

def main():
    s1 = "nodevillivedon"
    s2 = "livenoevil!liveonevil"
    s3 = "beliveivileb"
    r1 = palindrome_recursive(s1, 0)
    r2 = palindrome_recursive(s2, 0)
    r3 = palindrome_recursive(s3, 0)
    print("s1 is", r1)  # Should be True
    print("s2 is", r2)  # Should be True
    print("s3 is", r3)  # Should be False

main()
    
    
