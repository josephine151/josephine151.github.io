class Person {
  constructor(first_name, last_name, address) {
    this.first_name = first_name;
    this.last_name = last_name;
    this.address = address;
  }
  getFullName(){
    return (this.first_name + " " + this.last_name);
  }
  getAddress(){
    return (this.address);
  }
}

var tc = new Person("Tom", "Cruise", "123 Josephine ILY");
document.getElementById("myName").innerText = tc.getFullName();
document.getElementById("myAddress").innerText = tc.getAddress();
