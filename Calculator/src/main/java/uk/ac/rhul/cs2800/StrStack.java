package uk.ac.rhul.cs2800;

import java.util.EmptyStackException;

/**
 * Class StrStack is a facade which provides a simplified stack of values of type String.
 * 
 * @author Norbert Blazejewski
 *
 */
public class StrStack {
  private final Stack strStack = new Stack();

  /**
   * This method checks if the stack is empty (delegated to the contained stack class).
   * 
   * @return true if stack is empty(when strStack.size() is equal to 0) and false otherwise.
   */
  public final boolean isEmpty() {
    return strStack.size() == 0;
  }

  /**
   * Pushes a new String Entry value onto the stack (delegated to the contained Stack class).
   * 
   * @param item - the item that is pushed onto the stack.
   */
  public final void push(String item) {
    strStack.push(new Entry(item));
  }

  /**
   * Removes the object at the top of this stack and returns its value (delegated to stack class).
   * 
   * @return the String at the top of the stack.
   * @throws EmptyStackException if there is nothing in the stack.
   */
  public final String pop() throws EmptyStackException {
    return strStack.pop().getString();
  }

  /**
   * Return the value at the top of the stack without removing it.
   * 
   * @return the String at the top of the stack.
   * @throws EmptyStackException if there is nothing in the stack.
   */
  public final String peek() throws EmptyStackException {
    return strStack.top().getString();
  }
}
