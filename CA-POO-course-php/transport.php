<?php

class Transport {

    public function __construct($fields) {
        foreach ($fields as $key => $value) {
            $this->$key = $value;
        }
    }
    public function __toString()
    {
        return "le transport s'appelle $this->name, et peut contenir $this->passengers passager";
    }
}