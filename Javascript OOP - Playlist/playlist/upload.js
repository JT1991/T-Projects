var form = document.getElementById('file-form');
var fileSelect = document.getElementById('file-select');
var uploadButton = document.getElementById('upload-button');
//Using AJAX for file upload
form.onsubmit = function(event){
	event.preventDefault();
	uploadButton.innerHTML = 'Uploading..';
	var files = fileSelect.files;
	var formData = new FormData();
	
	for (var i = 0; i < files.length; i++){
		var file = files[i];
		if (!file.type.match('mp3.*')){
			continue;
		}
		formData.append('songs[]', file, file.name);
	}
	
	//set up request
	var xhr = new XMLHttpRequest();
	//open connection
	xhr.open('POST', 'handler.php', true );
	//send
	xhr.send(formData);
	// Set up a handler for when the request finishes.
	xhr.onload = function () {
  		if (xhr.status === 200) {
   		 // File(s) uploaded.
    			uploadButton.innerHTML = 'Uploaded';
  		} else {
    			alert('An error occurred!');
 		}
	};
	
}