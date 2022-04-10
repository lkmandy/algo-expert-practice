/** 
 * Write a function that takes in a non-empty array of integers that are sorted
 * in ascending order and returns a new array of the same length with the squares
 * of the original integers also sorted in ascending order.
*/

// (pointer): This implementation uses the two pointer technique
// Time Complexity: O(n)  |  Space Complexity: O(n)

List<num> sortedSquare(array) {
  int startIdx = 0;
  int j, endIdx = array.length - 1;
  int i = array.length - 1;
  List<num> sortedSquares = List.filled(array.length, 0);
  array.sort();

  for (i; i >= 0; i--) {
    if (array[endIdx].abs() > array[startIdx].abs()) {
      sortedSquares[i] = array[endIdx] * array[endIdx];
      endIdx -= 1;
    } else {
      sortedSquares[i] = array[startIdx] * array[startIdx];
      startIdx += 1;
    }
  }
  return sortedSquares;
}

main() {
  var array = [5, 11, -22, -3, -1, 16, 8, 0, -2, -1, 50];
  print(sortedSquare(array));
}
