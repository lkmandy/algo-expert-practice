"""
Write a function that takes in a non-empty array of integers that are sorted
in ascending order and returns a new array of the same length with the squares
of the original integers also sorted in ascending order.
"""

# (blt_ins): This implementation uses python built-in fucntions, sorting and arrays
# Time Complexity: O(nlogn)  |  Space Complexity: O(n)


def sortedSquaredArray(array):
    if len(array) == 0:
        return []

    arraySquares = list(map(lambda item: item * item, array))
    arraySquares.sort()
    return arraySquares


if __name__ == '__main__':
    sample = [5, 10, 15, 20, 25]
    print(sortedSquaredArray(sample))
