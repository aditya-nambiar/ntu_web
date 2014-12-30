<?php


$upload_dir = "/Applications/MAMP/htdocs/ntu/training/";

if (isset($_FILES["myfile"])) {
    $no_files = count($_FILES["myfile"]['name']);
    for ($i = 0; $i < $no_files; $i++) {

        if ($_FILES["myfile"]["error"][$i] > 0) {
            echo "Error: " . $_FILES["myfile"]["error"][$i] . "<br>";
        } else {

            move_uploaded_file($_FILES["myfile"]["tmp_name"][$i], $upload_dir . $_FILES["myfile"]["name"][$i]);
            echo $_FILES["myfile"]["name"][$i] . "<br>";
        }
    }
    echo " Files Uploaded Successfully!<br>";
}
?>