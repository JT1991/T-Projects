$(document).ready(function () {
  var url = '../office-jquery/data/employees.json';
  $.getJSON(url, function(response) {
    var statusHTML = '<ul class="bulleted">';
    $.each(response, function (index, employee) {
      if (employee.inoffice === true) {
        statusHTML += '<li class="in">';
      } else {
        statusHTML += '<li class="out">';
      }
      statusHTML += employee.name + '</li>';
    });
    statusHTML += '</ul>';
    $('#employeeList').html(statusHTML);
  });//end getJSON
  
  var url2 = '../office-jquery/data/rooms.json';
  $.getJSON(url2, function(response) {
    var statusHTML = '<ul class ="rooms">';
    $.each(response, function (index, room) {
      if (room.available === true) {
        statusHTML += '<li class="empty">';
      } else {
        statusHTML += '<li class="full">';
      }
      statusHTML += room.room + '</li>';
    });
    statusHTML += '</ul>';
    $('#roomList').html(statusHTML);
  });
}); //end ready


