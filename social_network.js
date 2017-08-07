/*
INSTRUCTIONS:

1. Create a list of 5 names of girls
2. Store 3 friends for each of these 5 girls
3. When the user enters the name of a girl from the list,
   and clicks "Get Friends" display friends of that girl
*/

/*ENTER CODE HERE*/
var friends = {
  "Grace": ["Josephine", "Obama", "Stanford", "Vermont", "Sapna"],
  "Kristen": ["Josephine", "Grace", "Tandon", "Sapna", "Clarisse"],
  "Clarisse": ["Kristen", "Sapna", "Khalid", "Nalini", "Rebekah"],
  "Rebecca": ["Angela", "Christine", "Kristen", "Shreya", "Sapna"],
  "Nalini": ["Melinda", "Shreya", "Grace", "Josephine", "code"],
  "Josephine": ["Mica", "Sarah", "Eric", "Chevy", "Shu"]
}

document.getElementById('names').innerHTML = Object.keys(friends);

function getFriends() {
  var name = document.getElementById('nameInput').value;
  document.getElementById('friends').innerHTML = friends[name];
}



/*EXTENSION*/

function addFriend() {
  var nameOfGirl = document.getElementById('nameOfGirl').value;
  var nameOfFriend = document.getElementById('nameOfFriend').value;

  friends[nameOfGirl].push(nameOfFriend);

document.getElementById('friends').innerHTML = friends[]

}
