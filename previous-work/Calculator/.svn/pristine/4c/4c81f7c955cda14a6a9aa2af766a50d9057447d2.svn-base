package uk.ac.rhul.cs2800;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class TestEntry {

  private Entry floatEntry;
  private Entry symbolEntry;
  private Entry stringEntry;


  @BeforeEach
  void setup() {
    floatEntry = new Entry(10.0f);
    stringEntry = new Entry("String");
    symbolEntry = new Entry(Symbol.LEFT_BRACKET);
  }

  @Test // Test 1
  void testGetValue() {
    assertThrows(IllegalArgumentException.class, () -> symbolEntry.getValue(),
        "Type of value must be NUMBER.");
    assertEquals(10.0, floatEntry.getValue(), "This should return a float value 10.0.");
    // To pass this test I had to create the getValue method. Later, I added the exception to pass
    // the IllegalArgumentException (the same applies to Test 2 and Test 3).
  }

  @Test // Test 2
  void testGetString() {
    assertThrows(IllegalArgumentException.class, () -> symbolEntry.getValue(),
        "Type of string must be STRING.");
    assertEquals("String", stringEntry.getString(), "This should return a String value String.");
    // To pass this test I had to create the getString method.
  }

  @Test // Test 3
  void testGetSymbol() {
    assertThrows(IllegalArgumentException.class, () -> stringEntry.getValue(),
        "Type of symbol must be SYMBOL.");
    assertEquals(Symbol.LEFT_BRACKET, symbolEntry.getSymbol(),
        "This should return a Symbol value LEFT_BRACKET.");
    // To pass this test I had to create the getSymbol method.
  }

  @Test // Test 4
  void testGetType() {
    assertEquals(Type.NUMBER, floatEntry.getType(),
        "floatEntry is a NUMBER type and floatEntry.getType() should return that.");
    assertEquals(Type.SYMBOL, symbolEntry.getType(),
        "symbolEntry is a SYMBOL type and symbolEntry.getType() should return that.");
    assertEquals(Type.STRING, stringEntry.getType(),
        "stringEntry is a STRING type and stringEntry.getType() should return that.");
    // To pass this test I had to create the getType method.
  }

  @Test // Test 5
  void testFloatEquals() {
    Entry secondFloatEntry = new Entry(10.0f);
    Entry thirdFloatEntry = new Entry(20.5f);
    assertTrue(floatEntry.equals(secondFloatEntry),
        "floatEntry and secondFloatEntry are both 10.0 and both of type NUMBER hence should be equal.");
    assertFalse(floatEntry.equals(thirdFloatEntry),
        "floatEntry(10.0) and thirdFloatEntry(20.5) are not the same hence should not be equal.");
    assertEquals(floatEntry.hashCode(), secondFloatEntry.hashCode(),
        "floatEntry and secondFloatEntry are the exact same object so the hashcode should be the same for both.");
    assertNotEquals(floatEntry.hashCode(), thirdFloatEntry.hashCode(),
        "floatEntry(10.0) and thirdFloatEntry(20.5) are not same object so the hashcode should be different.");
    assertFalse(floatEntry.equals(stringEntry),
        "floatEntry and stringEntry are not equal because they are different values and types");
    assertFalse(floatEntry.equals(symbolEntry),
        "floatEntry and symbolEntry are not equal because they are different values and types");
    // To pass this set of tests, I first instantiated two new Entry objects, both of type float,
    // but containing different values. I then generated the hashcode and equals methods
    // through Eclipse's generator. Similar idea applies to the next two tests.

  }

  @Test // Test 6
  void testStringEquals() {
    Entry secondStringEntry = new Entry("String");
    Entry thirdStringEntry = new Entry("Different String");
    assertTrue(stringEntry.equals(secondStringEntry),
        "stringEntry and secondStringEntry are both String and both of type STRING hence should be equal.");
    assertFalse(stringEntry.equals(thirdStringEntry),
        "stringEntry(String) and thirdStringEntry(Different String) are not the same hence should not be equal.");
    assertEquals(stringEntry.hashCode(), secondStringEntry.hashCode(),
        "stringEntry and secondStringEntry are the exact same object so the hashcode should be the same for both.");
    assertNotEquals(stringEntry.hashCode(), thirdStringEntry.hashCode(),
        "stringEntry(String) and thirdStringEntry(Different String) are not same object so the hashcode should be different.");
    assertFalse(stringEntry.equals(symbolEntry),
        "stringEntry and symbolEntry are not equal because they are different values and types");
    // All three different types of entries have now been compared to each other and none of them
    // are equal (which is correct).
    // To pass this set of tests, I first instantiated two new Entry objects, both of type String,
    // but containing different values. Hashcode and equals methods were already created for Test 5.

  }

  @Test // Test 7
  void testSymbolEquals() {
    Entry secondSymbolEntry = new Entry(Symbol.LEFT_BRACKET);
    Entry thirdSymbolEntry = new Entry(Symbol.DIVIDE);
    assertTrue(symbolEntry.equals(secondSymbolEntry),
        "symbolEntry and secondSymbol Entry are both LEFT_BRACKET and both of type SYMBOL hence should be equal.");
    assertFalse(symbolEntry.equals(thirdSymbolEntry),
        "symbolEntry(LEFT_BRACKET) and thirdSymbolEntry(DIVIDE) are not the same hence should not be equal.");
    assertEquals(symbolEntry.hashCode(), secondSymbolEntry.hashCode(),
        "symbolEntry and secondSymbolEntry are the exact same object so the hashcode should be the same for both.");
    assertNotEquals(symbolEntry.hashCode(), thirdSymbolEntry.hashCode(),
        "symbolEntry(LEFT_BRACKET) and thirdSymbolEntry(DIVIDE) are not same object so the hashcode should be different.\"");
    // To pass this set of tests, I first instantiated two new Entry objects, both of type Symbol,
    // but containing different values. Hashcode and equals methods were already created for Test 5.
  }
}
