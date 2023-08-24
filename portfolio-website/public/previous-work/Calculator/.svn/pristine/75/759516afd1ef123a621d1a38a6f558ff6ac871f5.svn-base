package uk.ac.rhul.cs2800;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class TestRevPolishCalc {
  RevPolishCalc rpc;

  @BeforeEach
  void setup() {
    rpc = new RevPolishCalc();
  }

  @Test // Test 1
  void testEvaluate2() throws InvalidExpressionException {
    assertEquals(rpc.evaluate("2"), 2,
        "Test that evalute returns the same value that was given in the expression but parsed as a float");
    // To pass the test the evaluate method returns the same value that was given in the expression.
  }

  @Test // Test 2
  void testEvalauteTwoValueAddition() throws InvalidExpressionException {
    assertEquals(rpc.evaluate("1 4 +"), 5,
        "Test evaluating that 1 4 + using Reverse Polish Notation produces 5.");
    // This test successfully passes after debugging an issue which occurred in the stack class.
    // This test passes when the provided expression evaluates to 5.
  }

  @Test // Test 3
  void testEvaluateMoreAddition() throws InvalidExpressionException {
    assertEquals(rpc.evaluate("1 2 3 +"), 5,
        "Test evaluating that 2 3 + using Reverse Polish Notation produces 5.");

    assertEquals(rpc.evaluate("1 2 3 + 6 +"), 11, "Test evaluating that (2 + 3) + 6 = 11.");

    assertEquals(rpc.evaluate("1 2 3 + 6 + + "), 12,
        "Test evaluating that ((2 + 3) + 6) + 1 = 12.");

    assertEquals(rpc.evaluate("1 2      3 +    6  + + "), 12,
        "Testing to see if the expression if affected by the number white spaces");
    // This set of tests checks if the expression is correctly evaluated when the addition sign is
    // positioned differently. It also checks if expression is affected by the number of white
    // spaces.
  }

  @Test // Test 4
  void testEvaluateTwoValuesSubtraction() throws InvalidExpressionException {
    assertEquals(rpc.evaluate("4 1 -"), 3,
        "Test evaluating that 4 1 - using Reverse Polish Notation produces 3.");
    // To pass this test, a new case had to be added to the switch statement which recognised the
    // minus sign. The test passes if the expression evaluates to 3.
  }

  @Test // Test 5
  void testEvaluateMoreSubtraction() throws InvalidExpressionException {
    assertEquals(rpc.evaluate("1 4 -"), -3, "Test evaulating that 1 - 4 = -3.");
    assertEquals(rpc.evaluate("1 4 3 -"), 1, "Test evaulating that 4 - 3 = 1.");
    assertEquals(rpc.evaluate("1 4 3 - +"), 2, "Test evaulating that (4 - 3) + 1 = 2.");
    assertEquals(rpc.evaluate("1 4 3 - + 3 4 + -"), -5,
        "Test evaulating that ((4 - 3) + 1) - (3 + 4) = -5.");
    assertEquals(rpc.evaluate("1         4  3     -"), 1,
        "Testing to see that white spaces don't affect the expression");
    // This set of tests checks if the expression is correctly evaluated when the subtraction sign
    // is positioned differently and when mixed with addition. It also checks if expression is
    // affected by the number of white spaces.
  }

  @Test // Test 6
  void testEvaluateTwoValuesMultiplication() throws InvalidExpressionException {
    assertEquals(rpc.evaluate("3 3 *"), 9,
        "Test evaluating that 3 3 * using Reverse Polish Notation produces 9.");
    // To pass this test, a new case had to be added to the switch statement which recognised the
    // multiplication sign. The test passes if the expression evaluates to 9.
  }

  @Test // Test 7
  void testEvaluateMoreMultiplication() throws InvalidExpressionException {
    assertEquals(rpc.evaluate("3 3 4 *"), 12, "Test evaluating that 3 * 4 = 12.");
    assertEquals(rpc.evaluate("3 3 4 * +"), 15, "Test evaluating that (3 * 4) + 3 = 15.");
    assertEquals(rpc.evaluate("3 3 4 * + 2 3 * -"), 9,
        "Test evaluating that ((3 * 4) + 3) - (2 * 3) = 9.");
    assertEquals(rpc.evaluate("3 3    4 * +  2    3 * -"), 9,
        "Testing to see that white spaces don't affect the expression.");
    // This set of tests checks if the expression is correctly evaluated when the multiplication
    // sign is positioned differently and when mixed with addition and subtraction. It also checks
    // if expression is affected by the number of white spaces.
  }

  @Test // Test 8
  void testEvaluateTwoValuesDivision() throws InvalidExpressionException {
    assertEquals(rpc.evaluate("12 3 /"), 4,
        "Test evaluating that 12 3 / using Reverse Polish Notation produces 4.");
    // To pass this test, a new case had to be added to the switch statement which recognised the
    // division sign. The test passes if the expression evaluates to 4.
  }

  @Test // Test 9
  void testEvaluateMoreDivision() throws InvalidExpressionException {
    assertEquals(rpc.evaluate("3 3 4 * + 2 3 * - 3 /"), 3,
        "Test evaluating that (((3 * 4) + 3) - (2 * 3)) / 3 = 3.");
    assertEquals(rpc.evaluate("3 3 4   * +   2     3   * - 3   /"), 3,
        "Testing to see that white spaces don't affect the expression.");
    // This set of tests checks if the expression is correctly evaluated when the division
    // sign is positioned differently and when mixed with addition, subtraction and multiplication.
    // It also checks if expression is affected by the number of white spaces.
  }
  
  @Test // 10
  void testThrowException() {
    assertThrows(InvalidExpressionException.class, () -> rpc.evaluate("  "),
        "Expression cannot be blank.");
    assertThrows(InvalidExpressionException.class, () -> rpc.evaluate(""),
        "Expression cannot be blank.");
  }
}


