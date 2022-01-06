<?php

include_once("factory.php");
include_once("data.php");

class Main
{
    public $transport = [];
    public $planets = [];
    public $people = [];
    public $species = [];
    public $vehicles = [];
    public $films = [];

    public function __construct()
    {
        $this->data = new Data();
    }
    public function run()
    {
        $this->runTransports();
        $this->runPlanets();
        $this->runCharacters();
        $this->runSpecies();
        $this->runVehicles();
        $this->runFilms();

        $this->linkAllPK();
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
        $this->transport[$data->pk] = Factory::create($data->fields, "transport");
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
        $this->planets[$data->pk] = Factory::create($data->fields, "planet");
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
        $this->people[$data->pk] = Factory::create($data->fields, "people");
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
        $this->species[$data->pk] = Factory::create($data->fields, "species");
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
        $this->vehicles[$data->pk] = Factory::create($data->fields, "vehicle");
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
        $this->films[$data->pk] = Factory::create($data->fields, "film");
    }
    private function linkAllPK()
    {
        foreach ($this->people as $value) {
            $value->linkPK($this->planets);
        }
        foreach ($this->species as $value) {
            $value->linkPK($this->people, $this->planets);
        }
        foreach ($this->vehicles as $value) {
            $value->linkPK($this->people);
        }
        foreach ($this->films as $value) {
            $value->linkPK($this->people, $this->transport, $this->planets, $this->species, $this->vehicles);
        }
    }
    public function __toString()
    {
        $content = "la liste des films est: <br>";
        foreach ($this->films as $film) {
            $content = $content . $film . "<br>";
        }
        return $content;
    }
    public function print()
    {
        foreach ($this->films as $film) {
            foreach ($film as $key => $content) {
                if (is_array($content)) {
                    echo ("$key: <br>");
                    foreach ($content as $value) {
                        echo ('<p style="margin-left: 40px">' . $value . '</p>');
                    }
                } else {
                    echo ($key . " : " . $content . "<br>");
                }
            }
        }
    }
}
