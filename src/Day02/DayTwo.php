<?php namespace Santa\Day02;

use Santa\Day02\Position;

class DayTwo
{
    const DOOR = 1;
    const BATHROOM = 2;

    private $keypads = [
        DayTwo::DOOR => [[1,2,3],[4,5,6],[7,8,9]],
        DayTwo::BATHROOM => [[0,0,1,0,0],[0,2,3,4,0],[5,6,7,8,9],[0,'A','B','C',0],[0,0,'D',0,0]]
    ];
    private $position;
    private $max_x;
    private $max_y;
    private $type;

    public function __construct(int $type)
    {
        $this->position = new Position();
        $this->setType($type);
    }

    // Public methods
    public function findButton(string $map)
    {
        $steps = str_split($map);

        foreach ($steps as $step) {
            switch ($step) {
                case 'U':
                    $this->moveUp();
                    break;
                case 'D':
                    $this->moveDown();
                    break;
                case 'L':
                    $this->moveLeft();
                    break;
                case 'R':
                    $this->moveRight();
                    break;
            }
        }

        return $this->keypads[$this->type][$this->position->X][$this->position->Y];
    }

    public function getCode(array $map)
    {
        $code = "";
        foreach ($map as $line) {
            $code = $code . $this->findButton($line);
        }

        return $code;
    }

    public function setType(int $type)
    {
        switch ($type) {
            case DayTwo::DOOR:
                $this->max_x = 2;
                $this->max_y = 2;
                $this->position->setPosition(1, 1);
                break;
            case DayTwo::BATHROOM:
                $this->max_x = 4;
                $this->max_y = 4;
                $this->position->setPosition(2, 0);
                break;
        }

        $this->type = $type;

        return $this;
    }

    // Private methods

    private function moveUp()
    {
        if ($this->position->X === 0) {
            return;
        }

        $this->position->X--;

        if ($this->isZero()) $this->position->X++;
    }

    private function moveDown()
    {
        if ($this->position->X === $this->max_x) {
            return;
        }

        $this->position->X++;

        if ($this->isZero()) $this->position->X--;
    }

    private function moveLeft()
    {
        if ($this->position->Y === 0) {
            return;
        }

        $this->position->Y--;

        if ($this->isZero()) $this->position->Y++;
    }

    private function moveRight()
    {
        if ($this->position->Y === $this->max_y) {
            return;
        }

        $this->position->Y++;

        if ($this->isZero()) $this->position->Y--;
    }

    private function isZero()
    {
        return $this->keypads[$this->type][$this->position->X][$this->position->Y] === 0;
    }
}
