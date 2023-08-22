package uk.ac.rhul.cs2800;

/**
 * Possible non-number tokens in an expression.
 * 
 * @author Norbert Blazejewski
 *
 */
public enum Symbol {
  LEFT_BRACKET, RIGHT_BRACKET, TIMES, DIVIDE, PLUS, MINUS, INVALID;

  /**
   * Method makes it possible to print any given Symbol ENUM.
   *
   * @return a printable Symbol ENUM.
   */
  public String toString() {
    return name();
  }
}
