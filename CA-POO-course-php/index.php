<?php

include_once('classes/fileReader.php');

$fr = new FileReader();
foreach ($fr->annualFiles as $af) {
    echo("<br>lecture du fichier : " . $af . "<br>");
    $fr->readFile($af);
}
