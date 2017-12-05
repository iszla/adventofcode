<?php namespace Santa\Day02;

class Position
{
    public $X = 1;
    public $Y = 1;

    public function setPosition(int $x, int $y)
    {
        $this->X = $x;
        $this->Y = $y;
    }
}