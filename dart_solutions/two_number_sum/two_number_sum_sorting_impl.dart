/** 
 * Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
 * If any two numbers in the input array sum up to the target sum, the function should return them in an array,
 * in any order. If no two numbers sum up to the target sum, the function should return an empty array.
   
 * Note that the target sum has to be obtained by summing two different integers in the array; you can't add a
 * single integer to itself in order to obtain the target sum.

 * You can assume that there will be at most one pair of numbers summing up to the target sum.

*/

// (sorting_impl): This is an implementation using Sorting
// Time Complexity: O(nlog(n))    |    Space Comaplexity: O(1)

List<int> twoNumberSum(numberList, targetSum) {
  numberList.sort();

  int leftPointer = 0;
  int rightPointer = numberList.length - 1;

  while (numberList[leftPointer] < numberList[rightPointer]) {
    int currentSum = numberList[leftPointer] + numberList[rightPointer];
    if (currentSum == targetSum) {
      return [numberList[leftPointer], numberList[rightPointer]];
    } else if (currentSum < targetSum) {
      leftPointer += 1;
    } else if (currentSum > targetSum) {
      rightPointer -= 1;
    }
  }

  return [];
}

main() {
  final mine = [5, 11, 22, 3, 16, 8, 50];
  print(twoNumberSum(mine, 6));
}
