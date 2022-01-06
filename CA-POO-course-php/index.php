<?php

include_once("controllers/main.php");
$data = new Main();
$data->run();
// echo ($data);
$data->print();
