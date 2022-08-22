import re


# Define a function for
# for validating an Email
def check(email):
    # Make a regular expression
    # for validating an Email
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # pass the regular expression
    # and the string into the fullmatch() method
    if (re.fullmatch(regex, email)):
        return "Valid Email"

    else:
        return "Invalid Email"


# Function to categorize password
def password(v):
    # the password should not be a
    # newline or space
    if v == "\n" or v == " ":
        return "Password cannot be a newline or space!"

    # the password length should be in
    # between 9 and 20
    if 9 <= len(v) <= 20:

        # checks for occurrence of a character
        # three or more times in a row
        if re.search(r'(.)\1\1', v):
            return "Weak Password: Same character repeats three or more times in a row"

        # checks for occurrence of same string
        # pattern( minimum of two character length)
        # repeating
        if re.search(r'(..)(.*?)\1', v):
            return "Weak password: Same string pattern repetition"

        else:
            return "Strong Password!"

    else:
        return "Password length must be 9-20 characters!"


def extractMax(input):
    # get a list of all numbers separated by
    # lower case characters
    # \d+ is a regular expression which means
    # one or more digit
    # output will be like ['100','564','365']
    numbers = re.findall('\d+', input)

    # now we need to convert each number into integer
    # int(string) converts string into integer
    # we will map int() function onto all elements
    # of numbers list
    numbers = map(int, numbers)

    return max(numbers)
