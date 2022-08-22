import requests


def _sum(arr):
    # initialize a variable
    # to store the sum
    # while iterating through
    # the array later
    sum = 0

    # iterate through the array
    # and add each element to the sum variable
    # one at a time
    for i in arr:
        sum = sum + i

    return (sum)


def isMonotonic(A):
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))


# Function to reverse a list using list comprehension
def reverse_list(original_list):
    return [original_list[len(original_list) - i] for i in range(1, len(original_list) + 1)]


# list using traversal
def multiplyList(myList):
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result


# Function returns N largest elements
def Nmaxelements(list1, N):
    final_list = []

    for i in range(0, N):
        max1 = 0

        for j in range(len(list1)):
            if list1[j] > max1:
                max1 = list1[j]

        list1.remove(max1)
        final_list.append(max1)

    return final_list


def sorting_of_element(list1, list2):
    # initializing blank dictionary
    f_1 = {}

    # initializing blank list
    final_list = []

    # Addition of two list in one dictionary
    f_1 = {list1[i]: list2[i] for i in range(len(list2))}

    # sorting of dictionary based on value
    f_lst = {k: v for k, v in sorted(f_1.items(), key=lambda item: item[1])}

    # Element addition in the list
    for i in f_lst.keys():
        final_list.append(i)
    return final_list


def CountFrequency(my_list):
    # Creating an empty dictionary
    freq = {}
    for items in my_list:
        freq[items] = my_list.count(items)

    for key, value in freq.items():
        print("% d : % d" % (key, value))


# Scrapes the words from the URL below and stores
# them in a list
def getWords():
    # contains about 2500 words
    url = "http://www.puzzlers.org/pub/wordlists/unixdict.txt"
    fetchData = requests.get(url)

    # extracts the content of the webpage
    wordList = fetchData.content

    # decodes the UTF-8 encoded text and splits the
    # string to turn it into a list of words
    wordList = wordList.decode("utf-8").split()

    return wordList


# function to determine whether a word is ordered or not
def isOrdered():
    # fetching the wordList
    collection = getWords()

    # since the first few of the elements of the
    # dictionary are numbers, getting rid of those
    # numbers by slicing off the first 17 elements
    collection = collection[16:]
    word = ''

    for word in collection:
        result = 'Word is ordered'
        i = 0
        l = len(word) - 1

        if (len(word) < 3):  # skips the 1 and 2 lettered strings
            continue

        # traverses through all characters of the word in pairs
        while i < l:
            if (ord(word[i]) > ord(word[i + 1])):
                result = 'Word is not ordered'
                break
            else:
                i += 1

        # only printing the ordered words
        if (result == 'Word is ordered'):
            print(word, ': ', result)
