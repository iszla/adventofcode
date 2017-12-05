<?php namespace Santa\Day03;

class DayThree
{
    public function checkSides(array $sides)
    {
        return (
            ((int)$sides[0] + (int)$sides[1]) > (int)$sides[2] &&
            ((int)$sides[1] + (int)$sides[2]) > (int)$sides[0] &&
            ((int)$sides[0] + (int)$sides[2]) > (int)$sides[1]
        );
    }

    public function checkForAmountOfValids(array $triangles)
    {
        $count = 0;
        foreach ($triangles as $tri) {
            if ($this->checkSides($tri)) {
                $count += 1;
                continue;
            }
        }

        return $count;
    }
}