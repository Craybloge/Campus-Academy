<?php
class Data
{
    private static $instance;
    private $files = [
        "transport",
        "films",
        "people",
        "planets",
        "species",
        "vehicles"
    ];
    public function __construct()
    {
        if (is_null(self::$instance)) {
            self::$instance = 1;
            self::$instance = new Data();
        }
        return self::$instance;
    }

    public function getDataFromJson($filename)
    {
        if ($this->checkFileNameExists($filename)) {
            $url = "data_swapi/" . $filename . ".json";
            return json_decode(file_get_contents($url));
        }
    }
    private function checkFileNameExists($filename)
    {
        return in_array($filename, $this->files);
    }
}
