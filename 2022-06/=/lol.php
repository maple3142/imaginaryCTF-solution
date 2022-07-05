<?php
    include('flag.php');
    if ($_GET['a'] !== $_GET['b'] && $_GET['a'] == $_GET['b']) {
        echo $FLAG;
    }
    else {
    highlight_file(__FILE__);
    }
?>

