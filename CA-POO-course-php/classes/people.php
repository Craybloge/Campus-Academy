<?php

class People
{

    public function __construct($fields, $planets)
    {
        foreach ($fields as $key => $value) {
            $this->$key = $value;
        }
        $this->gender = $this->getGender($fields->gender);
        $this->LinkPK($planets);
    }
    public function __toString()
    {
        return $this->name;
    }
    public function getGender($gender)
    {
        return ($gender == "male") ? "homme" : "femme";
    }
    public function LinkPK($planets)
    {
        $this->homeworld = $planets[$this->homeworld];
    }
}
