var array = [4, 36, 71, 87, 48, 15, 69, 84 , 9, 31, 14, 23, 17, 62, 41, 3, 75, 34, 57];
document.getElementById('names').innerHTML = array

function getArray() {
  for(var sorted = 1; sorted < array.length; sorted++) {
    var element = array[sorted]
    var unsorted = sorted

    //unsorted>0 relates to the index (position) and array[unsorted] < array[unsorted-1] means the value of the number (not the index)
    while (unsorted > 0 && array[unsorted] < array[unsorted-1]) {
      // swaps (puts in correct order)
      array[unsorted] = array[unsorted-1]
      array[unsorted - 1] = element
      //= means assigned

      // follows the current number being placed where it belongs in the sorted array
      unsorted = unsorted-1

    }
  }
  document.getElementById('numbers').innerHTML = array
}
