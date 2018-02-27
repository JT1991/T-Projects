function Media(title, duration, url) {//file
  this.title = title;
  this.duration = duration;
  this.url = url;
  this.isPlaying = false;
}

Media.prototype.play = function() {
  this.isPlaying = true;
};

Media.prototype.stop = function() {
  this.isPlaying = false;
};















