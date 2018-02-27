var playlist = new Playlist();
var stream = new MediaHandler();

var SchizoidMan = new Song("21st Century Schizoid Man Including Mirrors", "King Crimson", "7:00", "audio/1.mp3");
var TalkWind = new Song("I Talk To The Wind", "King Crimson", "3:43", "audio/2.mp3");
//var Warmest = new Movie("Blue Is the Warmest Colour", 2011, "2:13:00", "audio/3.mkv");

playlist.add(SchizoidMan);
playlist.add(TalkWind);
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


