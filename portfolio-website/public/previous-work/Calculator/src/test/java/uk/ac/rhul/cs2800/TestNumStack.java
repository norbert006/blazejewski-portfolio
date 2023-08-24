package uk.ac.rhul.cs2800;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import java.util.EmptyStackException;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class TestNumStack {
  private NumStack numStack;

  @BeforeEach
  public void setup() {
    numStack = new NumStack();
  }

  @Test // Test 1
  void test_isEmpty() {
    assertEquals(numStack.isEmpty(), true,
        "Test a newly created numStack to see that it is empty (meaning it has size 0.");
    // To pass this test, the value of numStack.size() must return 0.
  }

  @Test // Test 2
  void test_push() {
    assertEquals(numStack.isEmpty(), true,
        "Test a newly created numStack to see that it is empty.");
    float value = 10.0f;
    numStack.push(value);
    assertEquals(numStack.isEmpty(), false,
        "Test the same stack to see that it is not empty since a value has been pushed onto the stack.");
    // To pass this test, first the size of numStack must be 0 since nothing has been pushed onto
    // the stack, meaning that isEmpty() returns as true. Later, after a float value has been pushed
    // onto the stack, the size of numStack increases therefore isEmpty() should return false.
  }

  @Test // Test 3
  void test_pop() {
    float value = 10.0f;
    numStack.push(value);
    assertEquals(numStack.pop(), 10.0f,
        "After 10.0f was pushed onto the stack, test that pop returns the same value.");
    assertEquals(numStack.isEmpty(), true, "When value was popped, numStack should be empty.");
    // This test passes if pop returns the float value 10.0f and checks that the numStack is left
    // empty.
  }

  @Test // Test 4
  void test_popEmpty() {
    assertEquals(numStack.isEmpty(), true,
        "Nothing has been added to the stack, so isEmpty should return true.");
    assertThrows(EmptyStackException.class, () -> numStack.pop(),
        "You cannot pop from an empty stack");
    // This test passes without having to modify the pop method in NumStack because NumStack uses
    // the pop method which was created for the Stack class, meaning that the Stack class deals with
    // this exception.
  }
}
