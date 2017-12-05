<?php namespace Tests;

use Santa\Day01\DayOne;

class Day01Test extends \PHPUnit_Framework_TestCase
{
    public function setUp()
    {
        $this->class = new DayOne();
    }

    public function testFirstExample()
    {
        $this->assertEquals(5, $this->class->navigate('R2, L3'));
    }

    public function testSecondExample()
    {
        $this->assertEquals(2, $this->class->navigate('R2, R2, R2'));
    }

    public function testThirdExample()
    {
        $this->assertEquals(12, $this->class->navigate('R5, L5, R5, R3'));
    }

    public function testDoubleExample()
    {
        $this->assertEquals(4, $this->class->navigateToFirstDouble('R8, R4, R4, R8'));
    }
}
