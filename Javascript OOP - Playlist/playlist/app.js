var playlist = new Playlist();
var stream = new MediaHandler();

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

var uploadButton = document.getElementById('upload');
uploadButton.onclick = function(){
	
	playlist.renderInElement(playlistElement);
}

