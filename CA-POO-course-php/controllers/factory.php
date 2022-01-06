<?php

include_once("models/people.php");
include_once("models/film.php");
include_once("models/transport.php");
include_once("models/planet.php");
include_once("models/species.php");
include_once("models/vehicle.php");

class Factory
{

    public static function create($data, $model)
    {
        if ($model == "transport") {
            return new Transport($data);
        } elseif ($model == "planet") {
            return new Planet($data);
        } elseif ($model == "people") {
            return new People($data);
        } elseif ($model == "species") {
            return new Species($data);
        } elseif ($model == "vehicle") {
            return new Vehicle($data);
        } elseif ($model == "film") {
            return new Film($data);
        }
    }
}
