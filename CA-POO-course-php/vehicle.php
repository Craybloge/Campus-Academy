<?php

class Vehicle {

    public function __construct($fields, $people) {
        foreach ($fields as $key => $value) {
            $this->$key = $value;
        }
        $this->LinkPK($people);
    }
    public function LinkPK($people) {
        foreach ($this->pilots as $key => $value) {
            $this->pilots[$key] = $people[$value];
        }
    }
    public function __toString()
    {
        return $this->vehicle_class;
    }

}