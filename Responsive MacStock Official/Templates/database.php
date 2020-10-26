<?php

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "macstock";

$conn = mysqli_connect($servername,$username,$password,$dbname);

if($conn)
{
    echo "Message Sended Successfully";
}
else{
    echo "Connection Failed to Server ".mysqli_connect_error();
}

?>