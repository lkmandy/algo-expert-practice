/** 
 * Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
 * If any two numbers in the input array sum up to the target sum, the function should return them in an array,
 * in any order. If no two numbers sum up to the target sum, the function should return an empty array.
   
 * Note that the target sum has to be obtained by summing two different integers in the array; you can't add a
 * single integer to itself in order to obtain the target sum.

 * You can assume that there will be at most one pair of numbers summing up to the target sum.

*/

// (fl_impl): This is an implementation using Two For-loops
// Time Complexity: O(n^2)    |    Space Comaplexity: O(1)

List<int> twoNumberSum(numberList, targetSum) {
  int i;
  int j;

  for (i = 0; i <= ((numberList.length) - 2); i++) {
    int firstNumber = numberList[i];
    for (j = i + 1; j <= (numberList.length - 1); j++) {
      int secondNumber = numberList[j];
      if (targetSum == firstNumber + secondNumber) {
        return [firstNumber, secondNumber];
      }
    }
  }

  return [];
}

main() {
  final mine = [5, 11, 22, 3, 16, 8, 50];
  print(twoNumberSum(mine, 100));
}

/** if the two sum could be  obtained by adding a number to itself, the solution will be to use:
* Assign the j loop counter to 1
*  Allow the limit] of the i counter to extend to the last element of the array
**/