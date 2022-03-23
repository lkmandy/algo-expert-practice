/** 
* Given two non-empty arrays of integers, write a function that determines
* whether the second array is a subsequence of the first one.
*/

/// (fl_impl): This is an implementation using for-loops
// Time Complexity: O(n)    |    Space Comaplexity: O(1)

bool isValidSubsequence(array, subsequence) {
  int subsequenceIndx = 0;

  if (array.isEmpty && subsequence.isEmpty) {
    return false;
  }

  for (int item in array) {
    if (subsequenceIndx == subsequence.length) {
      break;
    }
    if (subsequence[subsequenceIndx] == item) {
      subsequenceIndx += 1;
    }
  }

  return subsequenceIndx == subsequence.length;
}

main() {
  List<int> numbers = [3, 4, 6, 7, 9, 0, 23];
  List<int> numberSubSet = [3, 6, 0, 5, 23];

  print(isValidSubsequence(numbers, numberSubSet));
}
