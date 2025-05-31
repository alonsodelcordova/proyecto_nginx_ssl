<?php

    

    global $conexion;

    function getConeccion()  {
        $servername = "db_mysql";
        $username = "restaurant";
        $password = "restaurant";
        $dbname = "restaurant";
        if (!isset($conexion)) {
            $conexion = new mysqli($servername, $username, $password, $dbname);
            if ($conexion->connect_error) {
                die("No se pudo conectar a la base de datos: " . $conexion->connect_error);
            }
        }
        return $conexion;
    }