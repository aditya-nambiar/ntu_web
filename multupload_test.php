<?php


$upload_dir = "/Applications/MAMP/htdocs/ntu/testing/";

if (isset($_FILES["myfile_test"])) {
    $no_files = count($_FILES["myfile_test"]['name']);
    for ($i = 0; $i < $no_files; $i++) {

        if ($_FILES["myfile_test"]["error"][$i] > 0) {
            echo "Error: " . $_FILES["myfile_test"]["error"][$i] . "<br>";
        } else {

            move_uploaded_file($_FILES["myfile_test"]["tmp_name"][$i], $upload_dir . $_FILES["myfile_test"]["name"][$i]);
            echo $_FILES["myfile_test"]["name"][$i] . "<br>";
        }
    }
    echo " Files Uploaded Successfully!<br>";
}
?>