<?php

  require_once('db.php');
 
  $conexion = getConeccion();
 
  $from_name = $_POST['name'];
  $from_email = $_POST['email'];
  $subject = $_POST['sbject'];
  $message = $_POST['message'];

  $query = "INSERT INTO contacts (name, email, subject, message) VALUES ('$from_name', '$from_email', '$subject', '$message')";
  $result = $conexion->query($query);

  if ($result) {
    echo "OK";
  } else {
    echo "Error: " . $conexion->error;
  }

?>

