package uk.ac.rhul.cs2800;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class TestType {
  private Type number;
  private Type symbol;
  private Type string;
  private Type invalid;

  @BeforeEach
  public void setup() {
    number = Type.NUMBER;
    symbol = Type.SYMBOL;
    string = Type.STRING;
    invalid = Type.INVALID;
  }

  @Test // Test 1
  void testNumber() {
    assertEquals(Type.valueOf("NUMBER"), number,
        "Test the ENUM Type NUMBER to see that its value is NUMBER.");
    // To pass this test, the Type ENUM had to contain the NUMBER value.
  }

  @Test // Test 2
  void testSymbol() {
    assertEquals(Type.valueOf("SYMBOL"), symbol,
        "Test the ENUM Type SYMBOL to see that its value is SYMBOL.");
    // To pass this test, the Type ENUM had to contain the SYMBOL value.
  }

  @Test // Test 3
  void testString() {
    assertEquals(Type.valueOf("STRING"), string,
        "Test the ENUM Type STRING to see that its value is STRING.");
    // To pass this test, the Type ENUM had to contain the STRING value.
  }

  @Test // Test 4
  void testInvalid() {
    assertEquals(Type.valueOf("INVALID"), invalid,
        "Test the ENUM Type INVALID to see that its value is INVALID.");
    // To pass this test, the Type ENUM had to contain the INVALID value.
  }


  @Test // Test 5
  void testToString() {
    assertEquals("NUMBER", number.toString(),
        "Test the ENUM Type NUMBER to see that when printed, it displays NUMBER");
    assertEquals("SYMBOL", symbol.toString(),
        "Test the ENUM Type SYMBOL to see that when printed, it displays SYMBOL");
    assertEquals("STRING", string.toString(),
        "Test the ENUM Type STRING to see that when printed, it displays STRING");
    assertEquals("INVALID", invalid.toString(),
        "Test the ENUM Type STRING to see that when printed, it displays INVALID");
    // To pass this test I had to create a toString method.
  }
}
