var message = '';
var student;
var search;

function print(message) {
  var outputDiv = document.getElementById('output');
  outputDiv.innerHTML = message;
}

function getStudentReport(student){
    var report = '<h2>Student: ' + student.Name + '</h2>';
    report += '<p>Track: ' + student.Track + '</p>';
    report += '<p>Points: ' + student.Points + '</p>';
    report += '<p>Achievements: ' + student.Achievements + '</p>';
    return report;
}

while (true) {
  search = prompt('Search student recordsl type a name [Lily] or type quit to end.');
  if (search === null || search.toLowerCase() === 'quit'){
    break;
  }
  for (var i = 0; i < students.length; i += 1){
    student = students[i];
    if (student.Name === search){
      message = getStudentReport(student);
      print(message);
   }
  }

}



