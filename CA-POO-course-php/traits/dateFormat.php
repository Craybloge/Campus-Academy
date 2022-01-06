<?php

trait DateFormat
{
    public function setReadableDate($date)
    {
        if (strlen($date) == 10) {
            $date = date_create_from_format("Y-m-d", $date);
            return date_format($date, "d/m/Y");
        } else {
            $date = date_create_from_format("Y-m-d\TH:i:s", $date);
            return date_format($date, "d/m/Y à H:i:s");
        }
    }
}
