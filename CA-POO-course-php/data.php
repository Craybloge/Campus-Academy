<?php

include_once("people.php");
include_once("film.php");
include_once("transport.php");
include_once("planet.php");
include_once("species.php");
include_once("vehicle.php");

class Data {

    public function run() {
        
        $url = "swapi/people.json";
        $c = json_decode(file_get_contents($url));
        $this->people = [];
        foreach ($c as $value) {
            $this->people[$value->pk] = new People($value->fields);
        }
        
        $url = "swapi/transport.json";
        $c = json_decode(file_get_contents($url));
        $this->transport = [];
        foreach ($c as $value) {
            $this->transport[$value->pk] = new Transport($value->fields);
        }
        
        $url = "swapi/planets.json";
        $c = json_decode(file_get_contents($url));
        $this->planets = [];
        foreach ($c as $value) {
            $this->planets[$value->pk] = new Planet($value->fields);
        }

        $url = "swapi/species.json";
        $c = json_decode(file_get_contents($url));
        $this->species = [];
        foreach ($c as $value) {
            $this->species[$value->pk] = new Species($value->fields, $this->people, $this->planets);
        }

        $url = "swapi/vehicles.json";
        $c = json_decode(file_get_contents($url));
        $this->vehicles = [];
        foreach ($c as $value) {
            $this->vehicles[$value->pk] = new Vehicle($value->fields, $this->people, $this->planets);
        }
        
        $url = "swapi/films.json";
        $c = json_decode(file_get_contents($url));
        $this->films = [];
        foreach ($c as $value) {
            $this->films[$value->pk] = new Film($value->fields, $this->people, $this->transport, $this->planets, $this->species, $this->vehicles);
        }
        
    
    }

}