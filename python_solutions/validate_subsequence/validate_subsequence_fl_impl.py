"""
Given two non-empty arrays of integers, write a function that determines
whether the second array is a subsequence of the first one.
"""

# (fl_impl): This is an implementation using for-loops
# Time Complexity: O(n)    |    Space Comaplexity: O(1)


def isValidSubsequence(array, subsequence):
    subsequenceIndex = 0

    if len(array) == 0 or len(subsequence) == 0:
        return False

    for element in array:
        if subsequenceIndex == len(subsequence):
            break
        if subsequence[subsequenceIndex] == element:
            subsequenceIndex += 1
    return subsequenceIndex == len(subsequence)


if __name__ == '__main__':
    print(isValidSubsequence([1, 2, 3, 4, 5, 6, 7], []))
