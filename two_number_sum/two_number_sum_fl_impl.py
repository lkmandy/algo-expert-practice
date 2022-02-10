
"""
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. 
If any two numbers in the input array sum up to the target sum, the function should return them in an array, 
in any order. If no two numbers sum up to the target sum, the function should return an empty array.

Note that the target sum has to be obtained by summing two different integers in the array; you can't add a 
single integer to itself in order to obtain the target sum.

You can assume that there will be at most one pair of numbers summing up to the target sum.
"""

# (fl_impl): This is an implementation using Two For-loops
# Time Complexity: O(n^2)    |    Space Comaplexity: O(1)


def twoNumberSum(numberList, targetSum):
    for i in range(len(numberList) - 1):
        firstNumber = numberList[i]
        for j in range(i + 1, len(numberList)):
            secondNumber = numberList[j]
            if (firstNumber + secondNumber == targetSum):
                return [firstNumber, secondNumber]
    return []


if __name__ == '__main__':

    numbers = [3, 5, -4, 8, 11, 1, -1, 6]
    target = 10

    print(twoNumberSum(numbers, target))
