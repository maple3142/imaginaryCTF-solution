<?php
  include 'f.php'; //flag in $flag, if it helps
  $payload = $_GET["escape"];
  if ($payload) {
    if (preg_match("/[a-z0-9\\\]/i", $payload) || strlen($payload) > 25) {
      echo "php good <br>";
    }
    else {
      eval($payload);
    }
  }
  else {
    show_source(__FILE__);
  }
?>
