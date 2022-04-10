/** 
 * Write a function that takes in a non-empty array of integers that are sorted
 * in ascending order and returns a new array of the same length with the squares
 * of the original integers also sorted in ascending order.
*/

// (blt_ins): This implementation uses python built-in fucntions, sorting and arrays
// Time Complexity: O(nlogn)  |  Space Complexity: O(1)

List<num> sortedSquare(array) {
  int tracker = 0;
  while (tracker < array.length) {
    array[tracker] = array[tracker] * array[tracker];
    tracker += 1;
  }
  array.sort();
  return array;
}

main() {
  var array = [-1, 5, 11, -22, -3, 0, 16, -0.5, 8, 0, 0, 50];
  print(sortedSquare(array));
}
