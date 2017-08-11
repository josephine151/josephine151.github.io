var id = 0;

function addPlans() {
  var input = document.getElementById("userInput").value;
  document.getElementById("userInput").value="";
  var span = document.createElement("span");
  var newDiv = document.createElement("div");
  span.className="tasks";
  span.innerHTML=input;
  var toDoList = document.getElementById("plans");
  toDoList.appendChild(createNewCheckbox(id));
  toDoList.appendChild(span);
  toDoList.appendChild(newDiv);
  id++;
}

function createNewCheckbox(id){
    var checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.id = id;
    checkbox.className="box";
    return checkbox;
}

function deletePlans() {
  var checks = document.getElementsByClassName("box")
  var tasks = document.getElementsByClassName("tasks")
    for(var i = 0; i < checks.length; i++){
      var check = checks[i];
      var task = tasks[i];
      if(check.checked){
        check.parentNode.removeChild(check);
        task.parentNode.removeChild(task);
      }
    }
}
