<?php namespace Tests;
use AOC\D02\DayTwo;

class Day02Test extends \PHPUnit_Framework_TestCase
{
    public function setUp()
    {
        $this->class = new DayTwo();
    }

    public function testFirst()
    {
        $this->assertEquals(8, $this->class->checkRow('5 1 9 5'));
        $this->assertEquals(4, $this->class->checkRow('7 5 3'));
        $this->assertEquals(6, $this->class->checkRow('2 4 6 8'));
        $this->assertEquals(18, $this->class->getChecksum());
    }
    
    public function testSecond()
    {
        $this->assertEquals(4, $this->class->checkDivide('5 9 2 8'));
        $this->assertEquals(3, $this->class->checkDivide('9 4 7 3'));
        $this->assertEquals(2, $this->class->checkDivide('3 8 6 5'));
    }
}