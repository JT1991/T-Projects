//way to use ajax with jquery

var url = '/employees.php';
var data = {
  firstName: "Josh",
  lastName: "Thorn"
};
var callback = function(response) {
  //do something with response
};
$.get(url, data, callback);

/*
another way is this

$.get('/employees.php', {
firstName : "Josh",
lastName : "Thorn"
}, function (response) {
  //do something with the data
});