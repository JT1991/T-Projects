var activeMedia;

function MediaHandler(){
  this.stream = undefined;
}

function Playlist() {
  this.songs = [];
  this.nowPlayingIndex = 0;
}

Playlist.prototype.add = function(song) {
  this.songs.push(song)
};

Playlist.prototype.play = function() {
  var currentSong = this.songs[this.nowPlayingIndex];
  activeMedia = currentSong.url;
  currentSong.play()
  return activeMedia
};

Playlist.prototype.stop = function(){
  var currentSong = this.songs[this.nowPlayingIndex];
  currentSong.stop();
};

Playlist.prototype.next = function() {
  this.stop()
  this.nowPlayingIndex++;
  if(this.nowPlayingIndex === this.songs.length) {
    this.nowPlayingIndex = 0;
  }
  this.play();
};

Playlist.prototype.renderInElement = function(list) {
  list.innerHTML = "";
  for(var i = 0; i < this.songs.length; i++) {
    list.innerHTML += this.songs[i].toHTML();
  }
};

MediaHandler.prototype.play = function(activeMedia){
	this.stream = new Audio(activeMedia);
	this.stream.play();
}

MediaHandler.prototype.stop = function()
{
	this.stream.pause();
	this.currentTIme = 0;
}
