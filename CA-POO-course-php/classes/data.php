<?php
class Data
{
    private $files = [
        "transport",
        "films",
        "people",
        "planets",
        "species",
        "vehicles"
    ];

    public function getDataFromJson($filename)
    {
        if ($this->checkFileNameExists($filename)) {
            $url = "swapi/" . $filename . ".json";
            return json_decode(file_get_contents($url));
        }
    }
    private function checkFileNameExists($filename)
    {
        return in_array($filename, $this->files);
    }
}
