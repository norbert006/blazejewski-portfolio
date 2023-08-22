package uk.ac.rhul.cs2800;

/**
 * The StandardCalc class is responsible for evaluating infix string expression through the use of a
 * Reverse Polish Calculator.
 * 
 * @author Norbert Blazejewski
 *
 */
public class StandardCalc {
  RevPolishCalc rpCalc = new RevPolishCalc();

  /**
   * This method uses the Shunting Yard algorithm to evaluate the expression given by the user.
   * 
   * @param expression - the expression to be evaluated.
   * @return a float value that is the result to the evaluated expression.
   * @throws InvalidExpressionException - throws a custom exception message when the user provides a
   *         blank expression.
   */
  public float evaluate(String expression) throws InvalidExpressionException {
    if (expression.isBlank()) {
      throw new InvalidExpressionException("The provided expression cannot be blank");
    } else {
      String rearrangedExpression = precedence(expression);
      float output = rpCalc.evaluate(rearrangedExpression);
      return output;
    }
  }

  /**
   * The method precedence iterates through the expression provided by the user and rearranges it
   * into a postfix format.
   * 
   * @param expression - the expression to be evaluated.
   * @return a rearranged string in a postfix format.
   */
  public String precedence(String expression) {
    // symbolStack holds the operators that are given in the expression.
    StrStack symbolStack = new StrStack();
    // Operator will represent the sign of the operator on the stack.
    String operator = null;
    // RearrangedExpression is a String which will hold the numerical values from the expression
    // intertwined with operators in the correct places.
    String rearrangedExpression = new String("");
    // Iterating through the expression, if a character is the +, -, * or / operator it is added
    // to the stack (and popped and added to the rearrangedExpression if the next operator has the
    // same or higher precedence), otherwise, the character is appended to rearrangedExpression.
    for (int i = 0; i < expression.length(); i++) {
      char c = expression.charAt(i);
      if (c == '+' || c == '-' || c == '*' || c == '/') {
        if (symbolStack.isEmpty()) {
          symbolStack.push(String.valueOf(c));
        } else if (symbolStack.peek().equals("-") && c == '-') {
          operator = symbolStack.pop();
          rearrangedExpression = rearrangedExpression + " " + operator;
          symbolStack.push(String.valueOf(c));
        } else if (symbolStack.peek().equals("+") && c == '+') {
          operator = symbolStack.pop();
          rearrangedExpression = rearrangedExpression + " " + operator;
          symbolStack.push(String.valueOf(c));
        } else if (symbolStack.peek().equals("+") && c == '-') {
          operator = symbolStack.pop();
          rearrangedExpression = rearrangedExpression + " " + operator;
          symbolStack.push(String.valueOf(c));
        } else if (symbolStack.peek().equals("-") && c == '+') {
          operator = symbolStack.pop();
          rearrangedExpression = rearrangedExpression + " " + operator;
          symbolStack.push(String.valueOf(c));
        } else if (symbolStack.peek().equals("*") && c == '*') {
          operator = symbolStack.pop();
          rearrangedExpression = rearrangedExpression + " " + operator;
          symbolStack.push(String.valueOf(c));
        } else if (symbolStack.peek().equals("+") && c == '*') {
          symbolStack.push(String.valueOf(c));
        } else if (symbolStack.peek().equals("*") && c == '+') {
          operator = symbolStack.pop();
          rearrangedExpression = rearrangedExpression + " " + operator;
          symbolStack.push(String.valueOf(c));
        } else if (symbolStack.peek().equals("*") && c == '-') {
          while (!symbolStack.isEmpty()) {
            operator = symbolStack.pop();
            rearrangedExpression = rearrangedExpression + " " + operator;
          }
          symbolStack.push(String.valueOf(c));
        } else if (symbolStack.peek().equals("-") && c == '*') {
          symbolStack.push(String.valueOf(c));
        } else if (symbolStack.peek().equals("/") && c == '/') {
          operator = symbolStack.pop();
          rearrangedExpression = rearrangedExpression + " " + operator;
          symbolStack.push(String.valueOf(c));
        } else if (symbolStack.peek().equals("/") && c == '+') {
          operator = symbolStack.pop();
          rearrangedExpression = rearrangedExpression + " " + operator;
          symbolStack.push(String.valueOf(c));
        } else if (symbolStack.peek().equals("+") && c == '/') {
          symbolStack.push(String.valueOf(c));
        } else if (symbolStack.peek().equals("/") && c == '-') {
          while (!symbolStack.isEmpty()) {
            operator = symbolStack.pop();
            rearrangedExpression = rearrangedExpression + " " + operator;
          }
          symbolStack.push(String.valueOf(c));
        } else if (symbolStack.peek().equals("-") && c == '/') {
          symbolStack.push(String.valueOf(c));
        } else if (symbolStack.peek().equals("/") && c == '*') {
          operator = symbolStack.pop();
          rearrangedExpression = rearrangedExpression + " " + operator;
          symbolStack.push(String.valueOf(c));
        } else if (symbolStack.peek().equals("*") && c == '/') {
          operator = symbolStack.pop();
          rearrangedExpression = rearrangedExpression + " " + operator;
          symbolStack.push(String.valueOf(c));
        }
      } else {
        rearrangedExpression += c;
      }
    }
    // If the stack is not empty, pop the operator and append it to the end of the
    // rearrangedExpression.
    while (!symbolStack.isEmpty()) {
      operator = symbolStack.pop();
      rearrangedExpression = rearrangedExpression + " " + operator;
    }
    return rearrangedExpression;
  }
}
