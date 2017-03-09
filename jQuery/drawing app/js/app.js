//Problem: No user interaction causes no change to application
//Solution: When user interacts cause changes appropriately

var color = $(".selected").css('background-color');
var $canvas = $('canvas');
var context = $('canvas')[0].getContext('2d');
var lastEvent;
var mousedown = false;

//When clicking on control list items
$('.controls').on('click', 'li', function(){
  
  //deselect sibling elements
   $(this).siblings().removeClass('selected');
  //seelct clicked element
  $(this).addClass('selected');
  //cache current color
  color = $(this).css('background-color');
  });

//When "new color" is pressed
$('#revealColorSelect').click(function(){
  //show color select or hide color select
  changeColor();
  $('#colorSelect').toggle();
});

//update the color span
function changeColor(){
  var r = $('#red').val();
  var b = $('#blue').val();
  var g = $('#green').val();
  $('#newColor').css('background-color', 'rgb(' + r + ',' + g +', ' + b +')');
 };
                     
//when color sliders change
$('input[type=range]').change(changeColor);
  //update new color span

//when "add color" pressed
$('#addNewColor').click(function(){
  //appened the color to the controls ui
  var $newColor = $('<li></li>');
  $newColor.css('background-color', $('#newColor').css('background-color'));
  $('.controls ul').append($newColor);
  //select new color
  $newColor.click();
});


$canvas.mousedown(function(e){
  lastEvent = e;
  mousedown = true;
}).mousemove(function(e){
  //draw on canvas
  if (mousedown){
    context.beginPath();
    context.moveTo(lastEvent.offsetX, lastEvent.offsetY);
    context.lineTo(e.offsetX, e.offsetY);
    context.strokeStyle = color;
    context.stroke();
    lastEvent = e;
  }
}).mouseup(function(){
  mousedown = false;
}).mouseleave(function(){
  $canvas.mouseup();
});










































