<?php
$email=$_REQUEST['email'];
$name=$_REQUEST['name'];
$ip=$_REQUEST['ip'];
session_start();
$_SESSION['session'] = $email;
$_SESSION['uname']=$name;
$_SESSION['ip']=$ip;
header('location:dashboard/index.php');


?>
