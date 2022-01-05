<?php

class Person {

    public $sexe;
    public $ddn;
    public $ddd;

    public function __construct($sexe, $ddn, $ddd) {
        $this->sexe = $this->defineSexe($sexe);
        $this->ddn = $this->createDateOrNull($ddn);
        $this->ddd = $this->createDateOrNull($ddd);
        if (!is_null($this->ddn) && !is_null($this->ddd)) {
            $this->age = $this->getAge();
        }
    }

    private function createDateOrNull($date) {
        if (!is_null($date) && !empty($date)) {
            return DateTime::createFromFormat('Ymd', $date);
        }
        return null;
    }

    private function defineSexe($sexe) {
        if ($sexe == 1) {
            return "h";
        }
        return "f";
    }

    private function getAge() {
        return $this->ddn->diff($this->ddd)->y;
    }

}