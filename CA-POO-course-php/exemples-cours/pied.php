<?php

include_once('common.php');

class Pied extends Common {

    public function __construct(
        $hauteur,
        $largeur,
        $couleur,
        $materiaux = null,
        $inclinaison = 0,
        $nb_pieds = 4
    ) {
        parent::__construct($hauteur, $largeur, $couleur);

        $this->materiaux = $materiaux;
        $this->inclinaison = $inclinaison;
        $this->nb_pieds = $nb_pieds;
        $this->hauteur_materiaux = $this->get_hauteur_materiaux();
    }

    public function printHauteur() {
        echo($this->hauteur);
    }

    private function get_hauteur_materiaux() {
        return $this->hauteur / $this->nb_pieds;
    }

    /*
    visibilité
    public => accessible de partout
    privé => accessible uniquement dans la classe
    protégé => accessible de la classe et des enfants directs
    */ 

} 