package uk.ac.rhul.cs2800;

import java.util.Objects;

/**
 * The Entry class represents values and their different types that can be stored in a stack.
 * 
 * @author Norbert Blazejewski
 *
 */
public class Entry {
  private float value;
  private String string;
  private Symbol symbol;
  private Type whatType;

  /**
   * Create an Entry with a float value and Type NUMBER.
   * 
   * @param value - generates an Entry with this item.
   */
  public Entry(float value) {
    this.value = value;
    whatType = Type.NUMBER;
  }

  /**
   * Create an Entry with a string value and type STRING.
   * 
   * @param string - generates an Entry with this item.
   */
  public Entry(String string) {
    this.string = string;
    whatType = Type.STRING;
  }

  /**
   * Create an Entry with a symbol value and type SYMBOL.
   * 
   * @param symbol - generates an Entry with this item.
   */
  public Entry(Symbol symbol) {
    this.symbol = symbol;
    whatType = Type.SYMBOL;
  }

  /**
   * A getter for the float value.
   * 
   * @return the value.
   */
  public float getValue() {
    if (whatType != Type.NUMBER) {
      throw new IllegalArgumentException();
    }
    return value;
  }

  /**
   * A getter for the String string.
   * 
   * @return the value.
   */
  public String getString() {
    if (whatType != Type.STRING) {
      throw new IllegalArgumentException();
    }
    return string;
  }

  /**
   * A getter for the Symbol symbol.
   * 
   * @return the value.
   */
  public Symbol getSymbol() {
    if (whatType != Type.SYMBOL) {
      throw new IllegalArgumentException();
    }
    return symbol;
  }

  /**
   * Produces the type of a given value.
   * 
   * @return the Type of a value.
   */
  public Type getType() {
    return whatType;
  }

  /**
   * Indicates whether some other object is "equal to" this one.
   *
   * @return a boolean expressing whether two objects are the same.
   */
  @Override
  public boolean equals(Object obj) {
    if (this == obj) {
      return true;
    }
    if (obj == null) {
      return false;
    }
    if (getClass() != obj.getClass()) {
      return false;
    }
    Entry other = (Entry) obj;
    return Objects.equals(string, other.string) && symbol == other.symbol
        && Float.floatToIntBits(value) == Float.floatToIntBits(other.value)
        && whatType == other.whatType;
  }

  /**
   * Returns a hash code value for the object.
   *
   * @return an int hash code value for the object.
   */
  @Override
  public int hashCode() {
    return Objects.hash(string, symbol, value, whatType);
  }
}
