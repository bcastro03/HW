def sentence_palindrome(s):
    l = 0
    h = len(s) - 1

    s = s.lower()

    while l <= h:
        get_at_l = s[l]
        get_at_h = s[h]

        if not get_at_l.isalpha():
            l += 1
        elif not get_at_h.isalpha():
            h -= 1
        elif get_at_l == get_at_h:
            l += 1
            h -= 1
        else:
            return False

    return True

def main():
    s = "Was it a car or a cat I saw hh"
    if sentence_palindrome(s):
        print("Sentence is palindrome")
    else:
        print("Sentence is not palindrome")

if __name__ == "__main__":
    main()