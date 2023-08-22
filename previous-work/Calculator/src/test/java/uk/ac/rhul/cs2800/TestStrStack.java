package uk.ac.rhul.cs2800;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import java.util.EmptyStackException;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class TestStrStack {
  private StrStack strStack;

  @BeforeEach
  public void setup() {
    strStack = new StrStack();
  }

  @Test // Test 1
  void test_isEmpty() {
    assertEquals(strStack.isEmpty(), true,
        "Test a newly created strStack to see that it is empty (meaning it has size 0.");
    // To pass this test, the value of strStack.size() must return 0.
  }

  @Test // Test 2
  void test_push() {
    assertEquals(strStack.isEmpty(), true,
        "Test a newly created strStack to see that it is empty.");
    String item = "String";
    strStack.push(item);
    assertEquals(strStack.isEmpty(), false,
        "Test the same stack to see that it is not empty since an item has been pushed onto the stack.");
    // To pass this test, first the size of strStack must be 0 since nothing has been pushed onto
    // the stack, meaning that isEmpty() returns as true. Later, after a String item has been pushed
    // onto the stack, the size of strStack increases therefore isEmpty() should return false.
  }

  @Test // Test 3
  void test_pop() {
    String item = "String";
    strStack.push(item);
    assertEquals(strStack.pop(), "String",
        "After 'String' was pushed onto the stack, test that pop returns the same value.");
    assertEquals(strStack.isEmpty(), true, "When value was popped, strStack should be empty.");
    // This test passes if pop returns the Symbol item Symbol.LEFT_BRACKET and checks that the
    // opStack is left empty.
  }

  @Test // Test 4
  void test_popEmpty() {
    assertEquals(strStack.isEmpty(), true,
        "Nothing has been added to the stack, so isEmpty should return true.");
    assertThrows(EmptyStackException.class, () -> strStack.pop(),
        "You cannot pop from an empty stack");
    // This test passes without having to modify the pop method in strStack because strStack uses
    // the pop method which was created for the Stack class, meaning that the Stack class deals with
    // this exception.
  }

  @Test // Test 5
  void testPeek() {
    strStack.push("String1");
    assertEquals(strStack.peek(), "String1",
        "After 'String1' was pushed onto the stack, test that peek returns the same value.");
    assertEquals(strStack.isEmpty(), false,
        "Peek has not removed the string from the stack hence it should not be empty.");
    // The peek() method was added whilst working on the standard calc in order to aid its evaluate method.
    // This test passes if peek() returns the value on the stack without removing it.
  }
}
