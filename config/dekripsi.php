<?php
session_start();
include "config.php";

$result = shell_exec("python dekrips.py");

if($result){
	header("location:../pilih.php?success=true");
}else{
	echo "fail";
}
?>

