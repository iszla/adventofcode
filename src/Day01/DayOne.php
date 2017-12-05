<?php namespace Santa\Day01;

class DayOne
{
    private $visited;

    public function navigate($input)
    {
        $this->visited[] = [0, 0];
        $position = $this->parse($input);

        return $this->findShortestRoute($position['X'], $position['Y']);
    }

    public function navigateToFirstDouble($input)
    {
        $this->visited[] = [0, 0];
        $this->parse($input);

        $double = $this->firstDouble();
        
        if ($double == null) {
            return "No double found";
        }

        return $this->findShortestRoute($double[0], $double[1]);
    }

    private function parse($input)
    {
        $currentPosition = ['heading' => 'N', 'X' => 0, 'Y' => 0];
        $steps = explode(', ', $input);

        for ($i=0; $i < count($steps); $i++) {
            $step = [$steps[$i][0], substr($steps[$i], 1)];
            $currentPosition = $this->goTo($currentPosition, $step[0], $step[1]);
        }

        return $currentPosition;
    }

    private function goTo($currentPosition, $turnTo, $steps)
    {
        switch ($currentPosition['heading']) {
            case 'N':
                if ($turnTo == 'L') {
                    $currentPosition['heading'] = 'W';
                    $currentPosition['X'] -= $steps;
                    $this->addToVisited('X', '-', $steps);
                }
                if ($turnTo == 'R') {
                    $currentPosition['heading'] = 'E';
                    $currentPosition['X'] += $steps;
                    $this->addToVisited('X', '+', $steps);
                }
                break;
            case 'W':
                if ($turnTo == 'L') {
                    $currentPosition['heading'] = 'S';
                    $currentPosition['Y'] -= $steps;
                    $this->addToVisited('Y', '-', $steps);
                }
                if ($turnTo == 'R') {
                    $currentPosition['heading'] = 'N';
                    $currentPosition['Y'] += $steps;
                    $this->addToVisited('Y', '+', $steps);
                }
                break;
            case 'S':
                if ($turnTo == 'L') {
                    $currentPosition['heading'] = 'E';
                    $currentPosition['X'] += $steps;
                    $this->addToVisited('X', '+', $steps);
                }
                if ($turnTo == 'R') {
                    $currentPosition['heading'] = 'W';
                    $currentPosition['X'] -= $steps;
                    $this->addToVisited('X', '-', $steps);
                }
                break;
            case 'E':
                if ($turnTo == 'L') {
                    $currentPosition['heading'] = 'N';
                    $currentPosition['Y'] += $steps;
                    $this->addToVisited('Y', '+', $steps);
                }
                if ($turnTo == 'R') {
                    $currentPosition['heading'] = 'S';
                    $currentPosition['Y'] -= $steps;
                    $this->addToVisited('Y', '-', $steps);
                }
                break;
        }

        return $currentPosition;
    }

    private function findShortestRoute($sx, $sy, $ex = 0, $ey = 0)
    {
        $steps = 0;

        while ($sx !== $ex) {
            if ($sx > $ex) {
                $sx--;
                $steps++;
            } elseif ($sx < $ex) {
                $sx++;
                $steps++;
            }
        }

        while ($sy !== $ey) {
            if ($sy > $ey) {
                $sy--;
                $steps++;
            } elseif ($sy < $ey) {
                $sy++;
                $steps++;
            }
        }

        return $steps;
    }

    private function firstDouble()
    {
        $tmp = [];

        for ($i=0; $i < $this->visited; $i++) {
            if (in_array($this->visited[$i], $tmp)) {
                return $this->visited[$i];
            }

            $tmp[] = $this->visited[$i];
        }

        return;
    }

    private function addToVisited($dir, $sign, $val)
    {
        for ($i=1; $i <= $val; $i++) {
            $tmp = end($this->visited);
            if ($dir == 'X') {
                if ($sign == '+') {
                    $this->visited[] = [$tmp[0] + 1, $tmp[1]];
                }
                if ($sign == '-') {
                    $this->visited[] = [$tmp[0] - 1, $tmp[1]];
                }
            }
            if ($dir == 'Y') {
                if ($sign == '+') {
                    $this->visited[] = [$tmp[0], $tmp[1] + 1];
                }
                if ($sign == '-') {
                    $this->visited[] = [$tmp[0], $tmp[1] - 1];
                }
            }
        }
    }
}
