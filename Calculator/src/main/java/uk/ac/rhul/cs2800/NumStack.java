package uk.ac.rhul.cs2800;

import java.util.EmptyStackException;

/**
 * Class NumStack is a facade which provides a simplified stack of numbers of type float.
 * 
 * @author Norbert Blazejewski
 *
 */
public class NumStack {

  private final Stack numStack = new Stack();

  /**
   * This method checks if the stack is empty (delegated to the contained stack class).
   * 
   * @return true if stack is empty(when numStack.size() is equal to 0 and false otherwise.
   */
  public final boolean isEmpty() {
    return numStack.size() == 0;
  }

  /**
   * Pushes a new float Entry value onto the stack (delegated to the contained Stack class).
   * 
   * @param value - the item that is pushed onto the stack.
   */
  public final void push(float value) {
    numStack.push(new Entry(value));
  }

  /**
   * Removes the object at the top of this stack and returns its value (delegated to stack class).
   * 
   * @return the number at the top of the stack.
   */
  public final float pop() throws EmptyStackException {
    return numStack.pop().getValue();
  }
}
