"""
Write a function that takes in a non-empty array of integers that are sorted
in ascending order and returns a new array of the same length with the squares
of the original integers also sorted in ascending order.
"""

# (pointers): This implementation uses two pointers, aka the start and end pointer technique
# Time Complexity: O(n)  |  Space Comaplexity: O(n)


def sortedSquaredArray(array):
    if len(array) == 0:
        return []

    startIdx = 0
    endIdx = len(array) - 1
    itemBox = [0 for _ in array]

    for item in reversed(range(len(array))):
        if abs(array[endIdx]) > abs(array[startIdx]):
            itemBox[item] = array[endIdx] * array[endIdx]
            endIdx -= 1
        else:
            itemBox[item] = array[startIdx] * array[startIdx]
            startIdx += 1
    return itemBox


if __name__ == '__main__':
    sample = [-2, -4, 10, -15, 20, 25]
    print(sortedSquaredArray(sample))
