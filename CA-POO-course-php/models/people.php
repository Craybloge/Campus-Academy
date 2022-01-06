<?php
include_once("model.php");

class People extends Model
{

    public function __construct($fields)
    {
        parent::__construct($fields);
        $this->gender = $this->getGender($fields->gender);
    }
    public function getGender($gender)
    {
        return ($gender == "male") ? "homme" : "femme";
    }
    public function linkPK($planets)
    {
        $this->homeworld = $planets[$this->homeworld];
    }
}
