def longest_palindrome(s):
    frequency = [0] * 128
    length = 0
    for c in s:
        frequency[ord(c)] += 1
        if frequency[ord(c)] == 2:
            length += 2
            frequency[ord(c)] = 0
    if length < len(s):
        length += 1
    return length

if __name__ == "__main__":
    s = "aabbccdd"

    # Function call
    print longest_palindrome(s)