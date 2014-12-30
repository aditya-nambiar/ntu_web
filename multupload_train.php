<?php


$upload_dir = "/Applications/MAMP/htdocs/ntu/training/";

if (isset($_FILES["myfile_train"])) {
    $no_files = count($_FILES["myfile_train"]['name']);
    for ($i = 0; $i < $no_files; $i++) {

        if ($_FILES["myfile_train"]["error"][$i] > 0) {
            echo "Error: " . $_FILES["myfile_train"]["error"][$i] . "<br>";
        } else {

            move_uploaded_file($_FILES["myfile_train"]["tmp_name"][$i], $upload_dir . $_FILES["myfile_train"]["name"][$i]);
            echo $_FILES["myfile_train"]["name"][$i] . "<br>";
        }
    }
    echo " Files Uploaded Successfully!<br>";
}
?>