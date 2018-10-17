<?php
session_start();
include "config.php";

$result = shell_exec("python enkrips.py");

if($result){
	header("location:../pilihbiasa.php");
}else{
	echo "fail";
}
?>

