package uk.ac.rhul.cs2800;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class TestSymbol {

  private Symbol left_bracket;
  private Symbol right_bracket;
  private Symbol times;
  private Symbol divide;
  private Symbol plus;
  private Symbol minus;
  private Symbol invalid;

  @BeforeEach
  public void setup() {
    left_bracket = Symbol.LEFT_BRACKET;
    right_bracket = Symbol.RIGHT_BRACKET;
    times = Symbol.TIMES;
    divide = Symbol.DIVIDE;
    plus = Symbol.PLUS;
    minus = Symbol.MINUS;
    invalid = Symbol.INVALID;
  }

  @Test // Test 1
  void testLeft_bracket() {
    assertEquals(Symbol.valueOf("LEFT_BRACKET"), left_bracket,
        "Test the ENUM Symbol LEFT_BRACKET to see that its value is LEFT_BRACKET");
    // To pass this test, the Symbol ENUM had to contain the LEFT_BRACKET value.
  }

  @Test // Test 2
  void testRight_Bracket() {
    assertEquals(Symbol.valueOf("RIGHT_BRACKET"), right_bracket,
        "Test the ENUM Symbol RIGHT_BRACKET to see that its value is RIGHT_BRACKET");
    // To pass this test, the Symbol ENUM had to contain the RIGHT_BRACKET value.
  }

  @Test // Test 3
  void testTimes() {
    assertEquals(Symbol.valueOf("TIMES"), times,
        "Test the ENUM Symbol TIMES to see that its value is TIMES");
    // To pass this test, the Symbol ENUM had to contain the TIMES value.
  }

  @Test // Test 4
  void testDivide() {
    assertEquals(Symbol.valueOf("DIVIDE"), divide,
        "Test the ENUM Symbol DIVIDE to see that its value is DIVIDE");
    // To pass this test, the Symbol ENUM had to contain the DIVIDE value.
  }

  @Test // Test 5
  void testPlus() {
    assertEquals(Symbol.valueOf("PLUS"), plus,
        "Test the ENUM Symbol PLUS to see that its value is PLUS");
    // To pass this test, the Symbol ENUM had to contain the PLUS value.
  }

  @Test // Test 6
  void testMinus() {
    assertEquals(Symbol.valueOf("MINUS"), minus,
        "Test the ENUM Symbol MINUS to see that its value is MINUS");
    // To pass this test, the Symbol ENUM had to contain the MINUS value.
  }

  @Test // Test 7
  void testInvalid() {
    assertEquals(Symbol.valueOf("INVALID"), invalid,
        "Test the ENUM Symbol INVALID to see that its value is INVALID");
    // To pass this test, the Symbol ENUM had to contain the INVALID value.
  }

  @Test // Test 8
  void testToString() {
    assertEquals("LEFT_BRACKET", left_bracket.toString(),
        "Test the ENUM Symbol LEFT_BRACKET to see that when printed, it displays LEFT_BRACKET");
    assertEquals("RIGHT_BRACKET", right_bracket.toString(),
        "Test the ENUM Symbol RIGHT_BRACKET to see that when printed, it displays RIGHT_BRACKET");
    assertEquals("TIMES", times.toString(),
        "Test the ENUM Symbol TIMES to see that when printed, it displays TIMES");
    assertEquals("DIVIDE", divide.toString(),
        "Test the ENUM Symbol DIVIDE to see that when printed, it displays DIVIDE");
    assertEquals("PLUS", plus.toString(),
        "Test the ENUM Symbol PLUS to see that when printed, it displays PLUS");
    assertEquals("MINUS", minus.toString(),
        "Test the ENUM Symbol MINUS to see that when printed, it displays MINUS");
    assertEquals("INVALID", invalid.toString(),
        "Test the ENUM Symbol INVALID to see that when printed, it displays INVALID");
    // To pass this test I had to create a toString method.
  }
}

