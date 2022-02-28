
"""
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. 
If any two numbers in the input array sum up to the target sum, the function should return them in an array, 
in any order. If no two numbers sum up to the target sum, the function should return an empty array.

Note that the target sum has to be obtained by summing two different integers in the array; you can't add a 
single integer to itself in order to obtain the target sum.

You can assume that there will be at most one pair of numbers summing up to the target sum.
"""

# (ht_impl): This is an implementation using Hash Tables
# Time Complexity: O(n)    |    Space Comaplexity: O(n)


def twoNumberSum(numbers, targetSum):
    store = {}
    for i in numbers:
        targetNumber = targetSum - i
        if targetNumber in store:
            return [targetNumber, i]
        else:
            store[i] = 1
    return []


if __name__ == '__main__':
    numberList = [3, 5, 8, 9, 1, 2, 10]
    targetSum = 5

    print(twoNumberSum(numberList, targetSum))
