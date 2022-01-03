<?php

require_once("commonInterface.php");

class Common implements CommonInterface {

    public function __construct(
        $hauteur,
        $largeur,
        $couleur    
    ) { 
        $this->hauteur = $hauteur;
        $this->largeur = $largeur;
        $this->couleur = $couleur;
    }

    // public function volume() {
    //     return $this->hauteur * $this->largeur * $this->largeur;
    // }

}