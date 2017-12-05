<?php namespace Tests;

use Santa\Day03\DayThree;

class Day03Test extends \PHPUnit_Framework_TestCase
{
    public function setUp()
    {
        $this->class = new DayThree();
    }

    public function testGetOneButton()
    {
        $this->assertFalse($this->class->checkSides([5, 10, 25]));
        $this->assertTrue($this->class->checkSides([566, 477, 376]));
    }
}
