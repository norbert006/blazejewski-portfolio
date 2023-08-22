package uk.ac.rhul.cs2800;

import java.util.ArrayList;
import java.util.EmptyStackException;

/**
 * Stack implementation.
 * 
 * @author Norbert Blazejewski
 *
 */
public class Stack {

  ArrayList<Entry> value = new ArrayList<Entry>();

  /**
   * Returns the number of elements in this list.
   * 
   * @return size of the stack.
   */
  public int size() {
    return value.size();
  }

  /**
   * Pushed an Entry onto the top of the stack.
   * 
   * @param i - the item to be pushed onto this stack.
   */
  public void push(Entry i) {
    value.add(i);
  }

  /**
   * Removes the object at the top of this stack and returns that object as the value of this
   * function.
   * 
   * @return The object at the top of this stack.
   */
  public Entry pop() {
    if (value.size() == 0) {
      throw new EmptyStackException();
    }
    Entry valueOnTopOfStack = value.get(value.size() - 1);
    value.remove(value.size() - 1);
    return valueOnTopOfStack;
  }

  /**
   * Looks at the object at the top of this stack without removing it from the stack.
   * 
   * @return The object at the top of this stack.
   */
  public Entry top() {
    if (value.size() == 0) {
      throw new EmptyStackException();
    }
    return value.get(value.size() - 1);
  }
}
