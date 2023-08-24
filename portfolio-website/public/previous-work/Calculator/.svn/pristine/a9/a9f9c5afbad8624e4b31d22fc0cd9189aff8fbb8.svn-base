package uk.ac.rhul.cs2800;

import java.util.function.Consumer;

/**
 * This interface specifies a variety of methods to help with how we want to interact with the
 * calculator.
 * 
 * @author Norbert Blazejewski
 *
 */
public interface ViewInterface {

  /**
   * Get the arithmetic expression from the user in a String format.
   * 
   * @return arithmetic expression as a String.
   */
  public String getExpression();

  /**
   * A method to enable showing the user the answer to their arithmetic expression.
   * 
   * @param str - the answer.
   */
  public void setAnswer(String str);

  /**
   * Adds an observer of the Calculate action.
   * 
   * @param f - the observer.
   */
  public void calcObserver(Runnable f);

  /**
   * Adds an observer to recognise the change in mode for the Calculate action.
   * 
   * @param f - the observer of type OpType (which is defined in an enum as either an infix or
   *        postfix).
   */
  public void addTypeObserver(Consumer<OpType> f);
}
