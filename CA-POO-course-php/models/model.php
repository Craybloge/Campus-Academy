<?php
include_once("traits/dateFormat.php");

class Model
{
    use DateFormat;
    private $dateRegex = "/\\d{4}-\\d{2}-\\d{2}(T\\d{2}:\\d{2}:\\d{2})?/";

    public function __construct($fields)
    {
        foreach ($fields as $key => $value) {
            $this->$key = $value;
            if (is_string($value)) {
                if (preg_match($this->dateRegex, $value, $matches) == 1) {
                    $this->$key = $this->setReadableDate($matches[0]);
                }
            }
        }
    }
    public function __toString()
    {
        return $this->name;
    }
}
