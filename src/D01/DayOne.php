<?php namespace AOC\D01;

class DayOne
{
    public function setInput(string $input)
    {
        $this->arrInput = str_split($input);
    }

    public function sum($input = null)
    {
        if ($input !== null) $this->setInput($input);

        $maxValue = count($this->arrInput) - 1;
        $totalValue = 0;

        for ($i=0; $i < count($this->arrInput); $i++) {
            if ($i === $maxValue) {
                $totalValue += ($this->arrInput[$i] == $this->arrInput[0]) ? $this->arrInput[$i] : 0;
                continue;
            }

            $totalValue += ($this->arrInput[$i] == $this->arrInput[$i+1]) ? $this->arrInput[$i] : 0;
        }
        return $totalValue;
    }

    public function sum2($input = null)
    {
        if ($input !== null) $this->setInput($input);
        
        $offset = count($this->arrInput) / 2;
        $maxValue = count($this->arrInput);
        $totalValue = 0;

        for ($i=0; $i < count($this->arrInput); $i++) {
            if (($i + $offset) >= $maxValue) {
                $totalValue += ($this->arrInput[$i] == $this->arrInput[$i - $offset]) ? $this->arrInput[$i] : 0;
                continue;
            }

            $totalValue += ($this->arrInput[$i] == $this->arrInput[$i + $offset]) ? $this->arrInput[$i] : 0;
        }

        return $totalValue;
    }
}
