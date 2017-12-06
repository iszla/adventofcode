<?php namespace Tests;
use AOC\D01\DayOne;

class Day01Test extends \PHPUnit_Framework_TestCase
{
    public function setUp()
    {
        $this->class = new DayOne();
    }

    public function testFirst()
    {
        $this->assertEquals(3, $this->class->sum('1122'));
        $this->assertEquals(4, $this->class->sum('1111'));
        $this->assertEquals(0, $this->class->sum('1234'));
        $this->assertEquals(9, $this->class->sum('91212129'));
        $this->assertEquals(18, $this->class->sum('9121212991212129'));
        $this->assertEquals(38, $this->class->sum('7966644237548182561728628128776886755141422'));
    }
    
    public function testSecond()
    {
        $this->assertEquals(6, $this->class->sum2('1212'));
        $this->assertEquals(0, $this->class->sum2('1221'));
        $this->assertEquals(4, $this->class->sum2('123425'));
        $this->assertEquals(12, $this->class->sum2('123123'));
        $this->assertEquals(4, $this->class->sum2('12131415'));
    }
}