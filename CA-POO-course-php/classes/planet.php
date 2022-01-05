<?php

class Planet
{

    public function __construct($fields)
    {
        foreach ($fields as $key => $value) {
            $this->$key = $value;
        }
    }
    public function __toString()
    {
        return $this->name;
    }
}
