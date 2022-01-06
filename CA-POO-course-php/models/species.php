<?php
include_once("model.php");

class Species extends Model
{

    public function __construct($fields)
    {
        parent::__construct($fields);
    }
    public function linkPK($people, $planets)
    {
        foreach ($this->people as $key => $value) {
            $this->people[$key] = $people[$value];
        }
        if ($this->homeworld != null) {

            $this->homeworld = $planets[$this->homeworld];
        }
    }
}
