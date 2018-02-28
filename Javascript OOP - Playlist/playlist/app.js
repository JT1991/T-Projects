var playlist = new Playlist();
var stream = new MediaHandler();

//var SchizoidMan = new Song("21st Century Schizoid Man Including Mirrors", "", "", "audio/1.mp3");
//var TalkWind = new Song("I Talk To The Wind", "", "", "audio/2.mp3");
//var Warmest = new Movie("Blue Is the Warmest Colour", 2011, "2:13:00", "audio/3.mkv");

//playlist.add(SchizoidMan);
//playlist.add(TalkWind);
//playlist.add(Warmest);

  
var playlistElement = document.getElementById("playlist");

playlist.renderInElement(playlistElement);

var playButton = document.getElementById('play');
playButton.onclick = function() {
  playlist.play();
  stream.play(activeMedia);
  playlist.renderInElement(playlistElement);

}

var nextButton = document.getElementById('next');
nextButton.onclick = function() {
  playlist.next();
  stream.stop(activeMedia);
  stream.play(activeMedia);
  playlist.renderInElement(playlistElement);

}

var stopButton = document.getElementById('stop');
stopButton.onclick = function() {
  playlist.stop();
  stream.stop(activeMedia);
  playlist.renderInElement(playlistElement);

}

document.getElementById('file').onchange = function(){

  var file = this.files[0];

  var reader = new FileReader();
  reader.onload = function(progressEvent){
    // Entire file
    console.log(this.result);

    // By lines
    var lines = this.result.split('\n');
    for(var line = 0; line < lines.length; line++){
      //console.log(lines[line]);
	  var uploadedSongs = new Song(lines[line], " ", " ", "audio/"+lines[line]);
	  playlist.add(uploadedSongs);
      playlist.renderInElement(playlistElement);
	  console.log(uploadedSongs);
    }
  };
  reader.readAsText(file);
};



