//Prevent spoiler being seen
//hide and reveal spoilers through user interaction

$(".spoiler span").hide();
$(".spoiler").append("<button>Reveal Spoiler!</button>");
$(".spoiler button").click(function(){
  $(this).prev().show();
  $(this).remove();
});