"""
Given two non-empty arrays of integers, write a function that determines
whether the second array is a subsequence of the first one.
"""

# (wl_impl): This is an implementation using while-loops
# Time Complexity: O(n)    |    Space Comaplexity: O(1)


def isValidSubsequence(array, subsequence):
    subsequenceindex = 0
    arrayIndex = 0

    if len(array) == 0 or len(subsequence) == 0:
        return False

    while subsequenceindex < len(subsequence) and arrayIndex < len(array):
        if subsequence[subsequenceindex] == array[arrayIndex]:
            subsequenceindex += 1
        arrayIndex += 1
    return subsequenceindex == len(subsequence)


if __name__ == '__main__':
    print(isValidSubsequence([1, 2, 3, 4, 5, 6, 7], []))
