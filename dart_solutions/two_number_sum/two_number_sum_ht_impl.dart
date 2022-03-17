/** 
 * Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
 * If any two numbers in the input array sum up to the target sum, the function should return them in an array,
 * in any order. If no two numbers sum up to the target sum, the function should return an empty array.
   
 * Note that the target sum has to be obtained by summing two different integers in the array; you can't add a
 * single integer to itself in order to obtain the target sum.

 * You can assume that there will be at most one pair of numbers summing up to the target sum.

*/

// (ht_impl): This is an implementation using Hash Tables
// Time Complexity: O(n)    |    Space Comaplexity: O(n)

List<int> twoNumberSum(numberList, targetSum) {
  Map<int, bool> testSet = Map();

  for (int item in (numberList.getRange(0, numberList.length))) {
    int targetNumber = targetSum - item;
    if (testSet.containsKey(targetNumber)) {
      return [item, targetNumber];
    } else {
      testSet[item] = true;
    }
  }
  return [];
}

main() {
  final mine = [5, 11, 22, 3, 16, 8, 50];
  print(twoNumberSum(mine, 8));
}
