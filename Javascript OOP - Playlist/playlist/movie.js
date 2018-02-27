function Movie(title, year, duration, url) {
  Media.call(this, title, duration, url)
  this.year = year;
}

Movie.prototype = Object.create(Media.prototype);

Movie.prototype.toHTML = function() {
  var htmlString = '<li';
  if(this.isPlaying) {
    htmlString += ' class="current"';
  }
  htmlString += '>';
  htmlString += this.title;
  htmlString += ' ( '
  htmlString += this.year;
  htmlString += ')';
  htmlString += '<span class="duration">'
  htmlString += this.duration;
  htmlString += '</span></li>';
  return htmlString;
};




