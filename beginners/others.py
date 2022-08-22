import math


def TowerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    TowerOfHanoi(n - 1, source, auxiliary, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    TowerOfHanoi(n - 1, auxiliary, destination, source)


# Dynamic Programming Python implementation of Coin
# Change problem
def count(S, m, n):
    # We need n+1 rows as the table is constructed
    # in bottom up manner using the base case 0 value
    # case (n = 0)
    table = [[0 for x in range(m)] for x in range(n + 1)]

    # Fill the entries for 0 value case (n = 0)
    for i in range(m):
        table[0][i] = 1

    # Fill rest of the table entries in bottom up manner
    for i in range(1, n + 1):
        for j in range(m):
            # Count of solutions including S[j]
            x = table[i - S[j]][j] if i - S[j] >= 0 else 0

            # Count of solutions excluding S[j]
            y = table[i][j - 1] if j >= 1 else 0

            # total count
            table[i][j] = x + y

    return table[n][m - 1]


# Returns the number of divisors of (A - B)
# greater than B
def calculateDivisors(A, B):
    N = A - B
    noOfDivisors = 0

    a = math.sqrt(N)
    for i in range(1, int(a + 1)):
        # if N is divisible by i
        if ((N % i == 0)):
            # count only the divisors greater than B
            if (i > B):
                noOfDivisors += 1

            # checking if a divisor isnot counted twice
            if ((N / i) != i and (N / i) > B):
                noOfDivisors += 1

    return noOfDivisors


# Utility function to calculate number of all
# possible values of X for which the modular
# equation holds true

def numberOfPossibleWaysUtil(A, B):
    # if A = B there are infinitely many solutions
    # to equation  or we say X can take infinitely
    # many values > A. We return -1 in this case
    if (A == B):
        return -1

    # if A < B, there are no possible values of
    # X satisfying the equation
    if (A < B):
        return 0

    # the last case is when A > B, here we calculate
    # the number of divisors of (A - B), which are
    # greater than B

    noOfDivisors = 0
    noOfDivisors = calculateDivisors
    return noOfDivisors


# Python code to calculate number
# of ways of selecting \'p\' non
# consecutive stations out of
# \'n\' stations

def stopping_station(p, n):
    num = 1
    dem = 1
    s = p

    # selecting \'s\' positions
    # out of \'n-s+1\'
    while p != 1:
        dem *= p
        p -= 1

    t = n - s + 1
    while t != (n - 2 * s + 1):
        num *= t
        t -= 1
    if (n - s + 1) >= s:
        return int(num / dem)
    else:
        # if conditions does not
        # satisfy of combinatorics
        return -1
