<?php

class People {

    public function __construct($fields) {
        foreach ($fields as $key => $value) {
            $this->$key = $value;
        }
        $this->gender = $this->getGender($fields->gender);
    }
    public function __toString()
    {
        return $this->name;
    }
    public function getGender($gender) {
        return ($gender == "male") ? "homme": "femme";
    }
}