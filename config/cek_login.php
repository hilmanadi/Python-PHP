<?php
session_start();
if(isset($_SESSION['id']) == null || isset($_SESSION['id']) == ""){
    header('location:index.php');
}