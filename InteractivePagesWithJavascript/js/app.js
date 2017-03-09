//Problem: User interaction doesn't provide desired results.
//Solution: Add interactivty so the user can manage daily tasks.

var taskInput = document.getElementById('new-task'); //new-task
var addButton = document.getElementsByTagName('Button')[0]; //first button
var incompleteTasksHolder = document.getElementById('incomplete-tasks'); //incomplete tasks
var completedTasksHolder = document.getElementById('completed-tasks'); // completed tasks

//new task list item
var createNewTaskElement  = function(taskString) {
  var listItem = document.createElement('li');
  
  //input (checkbox)
  var checkBox = document.createElement('input');  //checkbox
  //label
  var label = document.createElement('label'); //label
  //input (text)
  var editInput = document.createElement('input'); //text
  //button.edit
  var editButton = document.createElement('button'); //button
  //button.delete
  var deleteButton = document.createElement('button'); //button
  
  //Each elements, needs modifiying 
  checkBox.type = 'checkBox';
  editInput.type = 'text';
  editButton.innerText = "Edit";
  editButton.className = "edit";
  deleteButton.innerText = "Delete";
  deleteButton.className = "delete";
  
  
  label.innerText = taskString;
  
  
  //and appending
  listItem.appendChild(checkBox);
  listItem.appendChild(label);
  listItem.appendChild(editInput);
  listItem.appendChild(editButton);
  listItem.appendChild(deleteButton);
  
  return listItem;
}

//Add a new task
var addTask = function() {
  console.log("Add task");
  //Create a new list item with the text from #new-task:
  var listItem = createNewTaskElement(taskInput.value);
  //append listItem to incompeleteTasksHolder
  incompleteTasksHolder.appendChild(listItem);
  bindTaskEvents(listItem, taskCompleted);
  taskInput.value = '';
}

//Edit an existing task
var editTask = function() {
    console.log("Edit task");
    var listItem = this.parentNode;
    var editInput = listItem.querySelector('input[type=text');
    var label = listItem.querySelector('label');
    var containsClass = listItem.classList.contains('editMode');
    //if the class of the parent is .editMode
    if(containsClass) {
      //Switch from .editMode
      //label text become the input's value
      label.innerText = editInput.value;
    } else {
      //Switch to .editMode
      //input value becomes the label's text
      editInput.value = label.innerText;
    }
    //Toggle .editMode on the parent
    listItem.classList.toggle('editMode');
}

//Delete an existing task
var deleteTask = function() {
    console.log("Delete task");
    //Remove the parent list item from the ul
    var listItem = this.parentNode;
    var ul = listItem.parentNode;
    
    ul.removeChild(listItem);
}

//Mark a task as complete
var taskCompleted = function() {
    console.log("Task complete");
    //Append the task list item to the #completed-tasks
    var listItem = this.parentNode;
    completedTasksHolder.appendChild(listItem);
    bindTaskEvents(listItem, taskIncomplete);
}

//Mark a task as incomplete
var taskIncomplete = function() {
    console.log("Task incomplete");
    //Append the task list item to the #incomplete-tasks
    var listItem = this.parentNode;
    incompleteTasksHolder.appendChild(listItem);
    bindTaskEvents(listItem, taskCompleted);
}

var bindTaskEvents = function(taskListItem, checkBoxEventHandler){
    console.log('bind list item events');
    //select taskListItem's children
    var checkBox = taskListItem.querySelector('input[type=checkbox]');
    var editButton = taskListItem.querySelector('button.edit');
    var deleteButton = taskListItem.querySelector('button.delete');
  
    //bind editTask to edit button
    editButton.onclick = editTask;
    //bind delete task to delete button
    deleteButton.onclick = deleteTask;
    //bind CheckBoxEventHandler to checkbox
    checkBox.onchange = checkBoxEventHandler;
}
  

var ajaxRequest = function () {
  console.log("AJAX Request");
}

//Set the click handler to the addTask function
addButton.addEventListener('click', addTask);
addButton.addEventListener('click', ajaxRequest);

    

//cycle over incompletedtaskholder ul list items
for(var i = 0; i < incompleteTasksHolder.children.length; i++) {
  //bind events to list items children (taskCompleted)
  bindTaskEvents(incompleteTasksHolder.children[i], taskCompleted);
}

//cycle over completedTasksHolder ul list items
for(var i = 0; i < completedTasksHolder.children.length; i++) {
  //bind events to list item's children (taskIncomplete)
  bindTaskEvents(completedTasksHolder.children[i], taskIncomplete);
}










