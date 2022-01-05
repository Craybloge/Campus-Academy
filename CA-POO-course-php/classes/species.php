<?php

class Species
{

    public function __construct($fields, $people, $planets)
    {
        foreach ($fields as $key => $value) {
            $this->$key = $value;
        }
        $this->LinkPK($people, $planets);
    }
    public function LinkPK($people, $planets)
    {
        foreach ($this->people as $key => $value) {
            $this->people[$key] = $people[$value];
        }
        if ($this->homeworld != null) {

            $this->homeworld = $planets[$this->homeworld];
        }
    }
    public function __toString()
    {
        return $this->name;
    }
}
