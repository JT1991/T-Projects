var playlist = new Playlist();

var HereComesTheSun = new Song("Here comes the sun", "The Beatles", "2:54");
var WalkingOnSunshine = new Song("Walking on sunshine", "Katrina and the Waves", "3:43");
var ShaunOfDead = new Movie("Shaun of the Dead", 2003, "2:13:00");


playlist.add(HereComesTheSun);
playlist.add(WalkingOnSunshine);
playlist.add(ShaunOfDead);

var playlistElement = document.getElementById("playlist");

playlist.renderInElement(playlistElement);

var playButton = document.getElementById('play');
playButton.onclick = function() {
  playlist.play();
  playlist.renderInElement(playlistElement);

}

var nextButton = document.getElementById('next');
nextButton.onclick = function() {
  playlist.next();
  playlist.renderInElement(playlistElement);

}

var stopButton = document.getElementById('stop');
stopButton.onclick = function() {
  playlist.stop();
  playlist.renderInElement(playlistElement);

}

