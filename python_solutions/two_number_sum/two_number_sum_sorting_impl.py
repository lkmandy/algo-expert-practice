
"""
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
If any two numbers in the input array sum up to the target sum, the function should return them in an array,
in any order. If no two numbers sum up to the target sum, the function should return an empty array.

Note that the target sum has to be obtained by summing two different integers in the array; you can't add a
single integer to itself in order to obtain the target sum.

You can assume that there will be at most one pair of numbers summing up to the target sum.
"""

# (sorting_impl): This is an implementation using Sorting
# Time Complexity: O(nlog(n))    |    Space Comaplexity: O(1)


def twoNumberSum(numbers, targetSum):
    numbers.sort()

    leftPointer = 0
    righPointer = len(numbers) - 1

    while leftPointer < righPointer:
        currentSum = numbers[leftPointer] + numbers[righPointer]
        if currentSum == targetSum:
            return [numbers[leftPointer], numbers[righPointer]]
        # if this is true, it means we need a larger current sum, so we need to move
        # the left pointer right/forward
        elif currentSum < targetSum:
            leftPointer += 1
        # if this is true, it means we need a smaller current sum, so we need to move
        # the right pointer left/backward
        elif currentSum > targetSum:
            righPointer -= 1
    return []


if __name__ == '__main__':
    numberList = [3, 5, 8, 9, 1, 2, 10]
    target = 10

    print(twoNumberSum(numberList, target))
