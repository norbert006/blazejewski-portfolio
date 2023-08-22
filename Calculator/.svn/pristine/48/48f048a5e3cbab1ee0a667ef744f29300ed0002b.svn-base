package uk.ac.rhul.cs2800;

/**
 * This class is the model for the calculator.
 * 
 * @author Norbert Blazejewski
 *
 */
public final class CalcModel {
  RevPolishCalc revPolish = new RevPolishCalc();
  StandardCalc standard = new StandardCalc();

  /**
   * This method is responsible for evaluating the expression given by the user.
   * 
   * @param expression - the arithmetic expression to be evaluated, given by the user.
   * @param infix - a boolean indicating whether the expression is given in an infix form or not.
   * @return - the result to the expression
   * @throws InvalidExpressionException - exception is thrown if the expression is blank.
   */
  public float evaluate(String expression, boolean infix) throws InvalidExpressionException {
    if (infix) {
      return standard.evaluate(expression);
    }
    return revPolish.evaluate(expression);
  }

}
