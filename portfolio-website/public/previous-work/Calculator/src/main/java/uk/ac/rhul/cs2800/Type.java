package uk.ac.rhul.cs2800;

/**
 * A list of the types of value an Entry can represent.
 * 
 * @author Norbert Blazejewski
 */
public enum Type {
  NUMBER, SYMBOL, STRING, INVALID;

  /**
   * Method makes it possible to print any given Type ENUM.
   *
   * @return a printable Type ENUM.
   */
  public String toString() {
    return name();
  }
}
