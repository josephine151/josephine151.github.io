var arr = [1, 9, 28, 57, 73, 92,131, 142, 201, 239, 273, 294, 307, 358, 361, 385, 435, 460, 471, 478, 511];
document.getElementById('names').innerHTML = arr;

  function getPosition() {
    var x = document.getElementById('numberInput').value;
    console.log(x)
    var low = 0;
    var high = arr.length - 1;
    var i = -1;
      while(low<=high) {
        var mid = Math.floor((low + high)/2);
        if (arr[mid] == x) {
          i = mid;
          break;
        }
        else if (arr[mid]<x) {
          low = mid + 1;
        }
        else {
          high = mid - 1;
        }
  }
  document.getElementById('numbers').innerHTML = i;
}
