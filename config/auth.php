<?php
session_start();
include "config.php";

$username = $_POST['username'];
$password = hash('sha3-224',$_POST['password']);

$cek = mysqli_query($con, "SELECT * FROM user WHERE username = '$username' AND password = '$password'");
$ada = mysqli_num_rows($cek);
$data = mysqli_fetch_assoc($cek);

if ($ada > 0) {
	$_SESSION['username'] = $username;
	$_SESSION['role'] = $data["role"];
	if($data["role"] == "1"){
		header("location:../pilih.php");
	}else if($data["role"]=="2"){
		header("location:../pilihbiasa.php");
	}else {
		header("location:../index.php");
	}
}else {
	header("location:../index.php");
}


