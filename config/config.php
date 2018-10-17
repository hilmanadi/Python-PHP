<?php

$server		= 'localhost';
$username	= 'root';
$password	= '';
$database	= 'rekam_medik';

$con 		= mysqli_connect($server, $username, $password, $database) or die("Connection failed!");