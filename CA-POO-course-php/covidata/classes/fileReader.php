<?php

include_once('classes/person.php');

class FileReader {

    public function __construct() {
        $this->annualFiles = $this->getAnnualFiles();
    }

    public function readFile($filename) {
        // $filename = "datas/deces/annuels/deces-2020.txt";
        $handle = fopen($filename, "r");
        if (FALSE === $handle) {
            exit("Echec lors de l'ouverture du flux vers l'URL");
        }

        $count = 0;
        $age = 0;
        $h = 0;
        $f = 0;
        $age_h = 0;
        $age_f = 0;
        while (!feof($handle)) {
            $count++;
            $line = fgets($handle);
            $sexe = substr($line, 80, 1);
            $ddn = substr($line, 81, 8);
            $ddd = substr($line, 154, 8);
            $person = new Person($sexe, $ddn, $ddd);
            $age += $person->age;
            if($person->sexe == "h") {
                $age_h += $person->age;
                $h++;
            } else {
                $age_f += $person->age;
                $f++;
            }
        }
        fclose($handle);

        echo("nb décès : " . $count);
        echo("<br><br> moyenne d'age : ");
        echo($age / $count);
        echo("<br><br> moyenne d'age homme : ");
        echo($age_h / $h);
        echo("<br><br> moyenne d'age femme : ");
        echo($age_f / $f);
    }

    private function getAnnualFiles() {
        $folder = "datas/deces/annuels";
        $files = scandir($folder);
        $files = array_slice($files, 2);
        $toto = [];
        foreach ($files as $file) {
            $toto[] = $folder . "/" . $file;
        }
        return $toto;
    }

}