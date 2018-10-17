<?php
$a = "abc";
$b = "abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq";
$c = "";
echo "test vector 'abc' : ";
echo "<br>";
echo hash('sha3-224',$a);
echo "<br>";
echo "test vector 'abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq' : ";
echo "<br>";
echo hash('sha3-224',$b);
echo "<br>";
echo "test vector ' ' : ";
echo "<br>";
echo hash('sha3-224',$c);
echo "<br>";
?>