<?php

// Where the file is going to be placed 
$target_path = "audio/";

/* Add the original filename to our target path.  
Result is "uploads/filename.extension" */
$target_path = $target_path . basename( $_FILES['uploadedfile']['name']); 

if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) {
    echo "The file ".  basename( $_FILES['uploadedfile']['name']). 
    " has been uploaded";
	$myFile = "testFile.txt";
	$fh = fopen($myFile, 'a');
	$songData = ($_FILES['uploadedfile']['name'] .PHP_EOL);
	fwrite($fh, $songData);
	fclose($fh);
	header("Location:index.html");
} else{
    echo "There was an error uploading the file, please try again!";
}

?>
