# Function to count number
# of characters, words, spaces
# and lines in a file
import os


def counter(fname):
    # variable to store total word count
    num_words = 0

    # variable to store total line count
    num_lines = 0

    # variable to store total character count
    num_charc = 0

    # variable to store total space count
    num_spaces = 0

    # opening file using with() method
    # so that file gets closed
    # after completion of work
    with open(fname, 'r') as f:
        # loop to iterate file
        # line by line
        for line in f:
            # separating a line
            # from \n character
            # and storing again in line
            # variable for further operations
            line = line.strip(os.linesep)

            # splitting the line
            # to make a list of
            # all the words present
            # in that line and storing
            # that list in
            # wordlist variable
            wordslist = line.split()

            # incrementing value of
            # num_lines with each
            # iteration of loop to
            # store total line count
            num_lines = num_lines + 1

            # incrementing value of
            # num_words by the
            # number of items in the
            # list wordlist
            num_words = num_words + len(wordslist)

            # incrementing value of
            # num_charc by 1 whenever
            # value of variable c is other
            # than white space in the separated line
            num_charc = num_charc + sum(1 for c in line
                                        if c not in (os.linesep, ' '))

            # incrementing value of
            # num_spaces by 1 whenever
            # value of variable s is
            # white space in the separated line
            num_spaces = num_spaces + sum(1 for s in line
                                          if s in (os.linesep, ' '))


def count_number_of_lines(filename):
    with open(filename, 'r') as fp:
        lines = sum(1 for line in fp)
        return lines


# Creating Stack class (LIFO rule)
class Stack:

    def __init__(self):
        # Creating an empty stack
        self._arr = []

    # Creating push() method.
    def push(self, val):
        self._arr.append(val)

    def is_empty(self):
        # Returns True if empty
        return len(self._arr) == 0

    # Creating Pop method.
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return

        return self._arr.pop()


# Creating a function which will reverse
# the lines of a file and Overwrites the
# given file with its contents line-by-line
# reversed
def reverse_file(filename):
    S = Stack()
    original = open(filename)

    for line in original:
        S.push(line.rstrip("\n"))

    original.close()

    output = open(filename, 'w')

    while not S.is_empty():
        output.write(S.pop() + "\n")

    output.close()


def read_words(filename: str):
    # opening the text file
    with open(filename, 'r') as file:

        # reading each line
        for line in file:

            words = []
            # reading each word
            for word in line.split():
                # displaying the words
                words.append(word)

        return word
