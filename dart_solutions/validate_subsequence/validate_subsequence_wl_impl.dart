/** 
* Given two non-empty arrays of integers, write a function that determines
* whether the second array is a subsequence of the first one.
*/

/// (wl_impl): This is an implementation using while-loops
// Time Complexity: O(n)    |    Space Comaplexity: O(1)

bool isValidSubsequence(array, subsequence) {
  int arrayIndx = 0;
  int subsequenceIndx = 0;

  if (array.isEmpty && subsequence.isEmpty) {
    return false;
  }

  while (arrayIndx < array.length && subsequenceIndx < subsequence.length) {
    if (subsequence[subsequenceIndx] == array[arrayIndx]) {
      subsequenceIndx += 1;
    }
    arrayIndx += 1;
  }
  return subsequenceIndx == subsequence.length;
}

main() {
  List<int> numbers = [3, 4, 6, 7, 9, 0, 23];
  List<int> numberSubSet = [6, 7];

  print(isValidSubsequence(numbers, numberSubSet));
}
