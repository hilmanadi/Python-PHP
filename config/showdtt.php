<?php
session_start();
include "config.php";

$result = shell_exec("python dekrips.py");

if ($result){
	header("location:showdtbiasa.php");
}else {
	echo "fail";
}
mysqli_close($con);



