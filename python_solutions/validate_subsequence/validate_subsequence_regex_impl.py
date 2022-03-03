"""
Given two non-empty arrays of integers, write a function that determines
whether the second array is a subsequence of the first one.
"""

# (regex_impl): This is an implementation using regular expressions
# Time Complexity: O(n)    |    Space Comaplexity: O(1)

# TODO: Make all tests passs


def isValidSubsequence(array, subsequence):
    if ''.join(map(str, subsequence)) in ''.join(map(str, array)):
        return True
    return False


if __name__ == '__main__':
    print(isValidSubsequence([2, 4, 3], [2, 3]))
