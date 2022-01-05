<?php

include_once("data.php");
$data = new Data();
$data->run();

foreach ($data->films as $film) {
    echo("le film est: $film");
    echo("<br>");
    echo("il contient les espèces suivantes:");
    echo("<br>");
    
    // foreach ($value->starships as $starship) {
    //     echo("          ");
    //     echo($starship->name);
    //     echo("<br>");
    // }
    foreach ($film->species as $key => $species) {
        echo($species);

        echo("          dont la planète mère est : $species->homeworld");
        echo ("<br>");
    
    }
}


