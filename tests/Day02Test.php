<?php namespace Tests;

use Santa\Day02\DayTwo;

class Day02Test extends \PHPUnit_Framework_TestCase
{

    public function setUp()
    {
        $this->class = new DayTwo(DayTwo::DOOR);
    }

    public function testGetOneButton()
    {
        $this->assertEquals(1, $this->class->findButton('ULL'));
        $this->assertEquals(9, $this->class->findButton('RRDDD'));
        $this->assertEquals(8, $this->class->findButton('LURDL'));
        $this->assertEquals(5, $this->class->findButton('UUUUD'));
    }

    public function testGetFullCode()
    {
        $this->assertEquals(1985, $this->class->getCode(['ULL','RRDDD','LURDL','UUUUD']));
    }

    public function testBathroomLock()
    {
        $this->class->setType(DayTwo::BATHROOM);
        $this->assertEquals('5DB3', $this->class->getCode(['ULL','RRDDD','LURDL','UUUUD']));
    }
}