
<?php


  require_once('db.php');
 
  $conexion = getConeccion();
 
  $name = $_POST['name'];
  $email = $_POST['email'];
  $phone = $_POST['phone'];
  $date = $_POST['date'];
  $time = $_POST['time'];
  $people = $_POST['people'];
  $message = $_POST['message'];
 
  $query = "INSERT INTO book_a_table (name, email, phone, date, time, people, message) VALUES ('$name', '$email', '$phone', '$date', '$time', '$people', '$message')";
  $result = $conexion->query($query);

  if ($result) {
    echo "OK";
  } else {
    echo "Error: " . $conexion->error;
  }

?>

