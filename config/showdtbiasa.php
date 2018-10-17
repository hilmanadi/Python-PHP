<!doctype html>
<html lang="en">
<head>
	<meta charset="utf-8" />
	<link rel="icon" type="image/png" href="../assets/img/favicon.ico">
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />

	<title>Rekam Medik</title>

	<meta content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0' name='viewport' />
    <meta name="viewport" content="width=device-width" />
    
    
    <!-- Bootstrap core CSS     -->
    <link href="../assets/css/bootstrap.min.css" rel="stylesheet" />
        

    
    <!--  CSS for Demo Purpose, don't include it in your project     -->
    <link href="../assets/css/demo.css" rel="stylesheet" />
    
        
    <!--     Fonts and icons     -->
    <link href="http://maxcdn.bootstrapcdn.com/font-awesome/latest/css/font-awesome.min.css" rel="stylesheet">
    <link href='http://fonts.googleapis.com/css?family=Roboto:400,700,300' rel='stylesheet' type='text/css'>
    <link href="../assets/css/pe-icon-7-stroke.css" rel="stylesheet" />

</head>
<body style="background-color:#87CB16"> 
<?php
if (isset($_GET['success'])){
	
?>
<script type='text/javascript'>alert('Success')</script>
<?php
}
?>
<nav class="navbar navbar-transparent navbar-absolute">
    <div class="container">    
        <div class="navbar-header">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navigation-example-2">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
        </div>
        <div class="collapse navbar-collapse">       

		
        </div>
    </div>
</nav>


<div class="wrapper wrapper-full-page">
    <div class="full-page login-page" data-color="green" data-image="../assets/img/full-screen-image-1.jpg">
        
    <!--   you can change the color of the filter page using: data-color="blue | azure | green | orange | red | purple" -->
        <div class="content">
            <div class="container">
                <div class="row">                   
                    <div class="">
                        <?php
							session_start();
							include "config.php";

							
							$query =$sql = "SELECT * FROM pasien";
							$cek = mysqli_query($con,$query);

							echo "<table border='1' class='table table-bordered table-responsive'>
							<tr>
							<th>Id</th>
							<th>Nama</th>
							<th>Tanggal Berobat</th>
							<th>Umur</th>
							<th>Jenis Kelamin</th>
							<th>Alamat</th>
							<th>Pekerjaan</th>
							<th>Nama Dokter</th>
							<th>Keterangan Rekam Medik</th>
							<th>Gejala</th>
							</tr>";
							while($row = mysqli_fetch_array($cek)){
							echo "<tr>";
							echo "<td>" .$row['no_pasien']. "</td>";
							echo "<td>" .$row['nama']. "</td>";
							echo "<td>" .$row['tgl_berobat']. "</td>";
							echo "<td>" .$row['umur']. "</td>";
							echo "<td>" .$row['jenis_kelamin']. "</td>";
							echo "<td>" .$row['alamat']. "</td>";
							echo "<td>" .$row['pekerjaan']. "</td>";
							echo "<td>" .$row['nama_dokter']. "</td>";
							echo "<td>" .$row['ket_rekam_medik']. "</td>";
							echo "<td>" .$row['gejala']. "</td>";
							}
							echo "</table>";
							echo "<a href = enkripsibiasa.php style='color:white;'>Back</a>";

							mysqli_close($con);   
						?>
                    </div>                    
                </div>
            </div>
        </div>
    	
    	<footer class="footer footer-transparent pull-right">
            <div class="container pull-right">
                <p class="copyright pull-right">
                    &copy; 2018 <a href="">Rekam Medik</a>, Kesehatan itu Mahal!!
                </p>
            </div>
        </footer>

    </div>                             
       
</div>


</body>
    
    <!--   Core JS Files and PerfectScrollbar library inside jquery.ui   -->
    <script src="../assets/js/jquery.min.js" type="text/javascript"></script>
    <script src="../assets/js/jquery-ui.min.js" type="text/javascript"></script>
	<script src="../assets/js/bootstrap.min.js" type="text/javascript"></script>
	
	
	<!--  Forms Validations Plugin -->
	<script src="../assets/js/jquery.validate.min.js"></script>
	
	<!--  Plugin for Date Time Picker and Full Calendar Plugin-->
	<script src="../assets/js/moment.min.js"></script>
	
    <!--  Date Time Picker Plugin is included in this js file -->
    <script src="../assets/js/bootstrap-datetimepicker.js"></script>
    
    <!--  Select Picker Plugin -->
    <script src="../assets/js/bootstrap-selectpicker.js"></script>
    
	<!--  Checkbox, Radio, Switch and Tags Input Plugins -->
	<script src="../assets/js/bootstrap-checkbox-radio-switch-tags.js"></script>
	
	<!--  Charts Plugin -->
	<script src="../assets/js/chartist.min.js"></script>

    <!--  Notifications Plugin    -->
    <script src="../assets/js/bootstrap-notify.js"></script>
    
    <!-- Sweet Alert 2 plugin -->
	<script src="../assets/js/sweetalert2.js"></script>
        
    <!-- Vector Map plugin -->
	<script src="../assets/js/jquery-jvectormap.js"></script>
	
    <!--  Google Maps Plugin    -->
    <script src="https://maps.googleapis.com/maps/api/js"></script>
	
	<!-- Wizard Plugin    -->
    <script src="../assets/js/jquery.bootstrap.wizard.min.js"></script>

    <!--  Datatable Plugin    -->
    <script src="../assets/js/bootstrap-table.js"></script>
    
    <!--  Full Calendar Plugin    -->
    <script src="../assets/js/fullcalendar.min.js"></script>
    
    <!-- Light Bootstrap Dashboard Core javascript and methods -->
	<script src="../assets/js/light-bootstrap-dashboard.js"></script>
	
	<!-- Light Bootstrap Dashboard DEMO methods, don't include it in your project! -->
	<script src="../assets/js/demo.js"></script>
	    
    <script type="text/javascript">
        $().ready(function(){
            lbd.checkFullPageBackgroundImage();
            
            setTimeout(function(){
                // after 1000 ms we add the class animated to the login/register card
                $('.card').removeClass('card-hidden');
            }, 700)
        });
    </script>    
</html>
