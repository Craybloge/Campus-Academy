<?php
include_once("model.php");

class Vehicle extends Model
{

    public function __construct($fields)
    {
        parent::__construct($fields);
    }
    public function linkPK($people)
    {
        foreach ($this->pilots as $key => $value) {
            $this->pilots[$key] = $people[$value];
        }
    }
    public function __toString()
    {
        return $this->vehicle_class;
    }
}
