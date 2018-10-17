<?php
session_start();
include "config.php";

$id = $_POST['id'];
$nama = $_POST['nama'];
$tgl_berobat = $_POST['tgl_berobat'];
$umur = $_POST['umur'];
$jenis_kelamin = $_POST['jenis_kelamin'];
$alamat = $_POST['alamat'];
$pekerjaan = $_POST['pekerjaan'];
$nama_dokter = $_POST['nama_dokter'];
$ket_rekam_medik = $_POST['ket_rekam_medik'];
$gejala = $_POST['gejala'];

$idd = escapeshellarg($id);
$namaa = escapeshellarg($nama);
$tglberobat = escapeshellarg($tgl_berobat);
$umurr = escapeshellarg($umur);
$jeniskelamin = escapeshellarg($jenis_kelamin);
$alamatt = escapeshellarg($alamat);
$pekerjaann = escapeshellarg($pekerjaan);
$namadokter = escapeshellarg($nama_dokter);
$ketrekammedik = escapeshellarg($ket_rekam_medik);
$gejalaa = escapeshellarg($gejala);

$result = shell_exec("python enkripinsert.py '$idd' '$namaa' '$tglberobat' '$umurr' '$jeniskelamin' '$alamatt' '$pekerjaann' '$namadokter' '$ketrekammedik' '$gejalaa'");
echo $result;
//$query ="INSERT INTO pasien VALUES ('$id','$nama','$tgl_berobat','$umur','$jenis_kelamin',
  //'$alamat','$pekerjaan','$nama_dokter','$ket_rekam_medik','$gejala')";
//$cek = mysqli_query($con,$query);
if ($result){
	header("location:../pilihbiasa.php?success=true");
}else {
	echo "fail";
}