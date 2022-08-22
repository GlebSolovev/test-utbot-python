import re


def isPalindrome(s):
    return s == s[::-1]


# Recursive function to check if a
# string is palindrome
def isPalindrome_recusrive(s):
    # to change it the string is similar case
    s = s.lower()
    # length of s
    l = len(s)

    # if length is less than 2
    if l < 2:
        return True

    # If s[0] and s[l-1] are equal
    elif s[0] == s[l - 1]:

        # Call is palindrome form substring(1,l-1)
        return isPalindrome(s[1: l - 1])

    else:
        return False


# count function count the common unique
# characters present in both strings .
def count(str1, str2):
    # set of characters of string1
    set_string1 = set(str1)

    # set of characters of string2
    set_string2 = set(str2)

    # using (&) intersection mathematical operation on sets
    # the unique characters present in both the strings
    # are stored in matched_characters set variable
    matched_characters = set_string1 & set_string2

    # printing the length of matched_characters set
    # gives the no. of matched characters
    return len(matched_characters)


def Find(string):
    # findall() has been used
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    return [x[0] for x in url]


def find_dup_char(input):
    x = []
    for i in input:
        if i not in x and input.count(i) > 1:
            x.append(i)
    print(" ".join(x))
