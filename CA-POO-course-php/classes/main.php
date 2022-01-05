<?php

include_once("classes/people.php");
include_once("classes/film.php");
include_once("classes/transport.php");
include_once("classes/planet.php");
include_once("classes/species.php");
include_once("classes/vehicle.php");
include_once("classes/data.php");

class Main
{
    public $transport = [];
    public $planets = [];
    public $people = [];
    public $species = [];
    public $vehicles = [];
    public $films = [];

    public function run()
    {
        $this->data = new Data();
        $this->runTransports();
        $this->runPlanets();
        $this->runCharacters();
        $this->runSpecies();
        $this->runVehicles();
        $this->runFilms();
    }
    private function runTransports()
    {
        $datas = $this->data->getDataFromJson("transport");
        foreach ($datas as $data) {
            $this->runTransport($data);
        }
    }
    private function runTransport($data)
    {
        $this->transport[$data->pk] = new Transport($data->fields);
    }
    private function runPlanets()
    {
        $datas = $this->data->getDataFromJson("planets");
        foreach ($datas as $data) {
            $this->runPlanet($data);
        }
    }
    private function runPlanet($data)
    {
        $this->planets[$data->pk] = new Planet($data->fields);
    }
    private function runCharacters()
    {
        $datas = $this->data->getDataFromJson("people");
        foreach ($datas as $data) {
            $this->runCharacter($data);
        }
    }
    private function runCharacter($data)
    {
        $this->people[$data->pk] = new People($data->fields, $this->planets);
    }
    private function runSpecies()
    {
        $datas = $this->data->getDataFromJson("species");
        foreach ($datas as $data) {
            $this->runSpecie($data);
        }
    }
    private function runSpecie($data)
    {
        $this->species[$data->pk] = new Species($data->fields, $this->people, $this->planets);
    }
    private function runVehicles()
    {
        $datas = $this->data->getDataFromJson("vehicles");
        foreach ($datas as $data) {
            $this->runVehicle($data);
        }
    }
    private function runVehicle($data)
    {
        $this->vehicles[$data->pk] = new Vehicle($data->fields, $this->people, $this->planets);
    }
    private function runFilms()
    {
        $datas = $this->data->getDataFromJson("films");
        foreach ($datas as $data) {
            $this->runFilm($data);
        }
    }
    private function runFilm($data)
    {
        $this->films[$data->pk] = new Film($data->fields, $this->people, $this->transport, $this->planets, $this->species, $this->vehicles);
    }
    public function __toString()
    {
        $print = "la liste des films est: <br>";
        foreach ($this->films as $film) {
            $print = $print . $film . "<br>";
        }
        return $print;
    }
    public function print()
    {
        foreach ($this->films as $film) {
            echo ("le film est: $film");
            echo ("<br>");
            echo ("il contient les personnages suivants:");
            echo ("<br>");

            // foreach ($film->starships as $starship) {
            //     echo("          ");
            //     echo($starship->name);
            //     echo("<br>");
            // }
            // foreach ($film->species as $key => $species) {
            //     echo($species);
            //     echo("          dont la planète mère est : $species->homeworld");
            //     echo ("<br>");

            // }
            foreach ($film->characters as $key => $character) {
                echo ($character);
                echo (" dont la planète mère est: $character->homeworld");
                echo ("<br>");
            }
        }
    }
}
