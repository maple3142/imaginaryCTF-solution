<!DOCTYPE HTML>
<html>
  <head>
    <title>I l0v3 Php</title>
  </head>
  <body>
    <p>If you exec <code>secret_function()</code> you will get the flag</p>
  </body>
<?php
    include "flag.php";
    show_source(__FILE__);

    if (isset($_GET['cmd'])) {
        if ((strlen($_GET['cmd']) < 100) && (!preg_match("/[A-Za-z0-9]+/",$_GET['cmd']))) {
            eval($_GET['cmd']);
        }else{
            printf("Try Harder!!");
        }
    }else{
        printf("Try Harder!!");
    }

?>
</html>

