package uk.ac.rhul.cs2800;

/**
 * CalcController creates a view and a model and it adds itself as an observer to the view so that
 * asynchronous changes can be observed.
 * Credit to Dave Cohen. Both the calculate method and the expressionType method found in this class
 * have been influenced by calculateAction method and changeType method from the Controller class in
 * the MVCJavaFX example.
 * 
 * @author Norbert Blazejewski
 *
 */
public class CalcController {
  private CalcModel calcModel;
  private ViewInterface myView;
  private boolean isInfix;

  /**
   * This method is notified when a calculation is required.
   * 
   * @throws InvalidExpressionException - exception is thrown when the user provides an empty
   *         string.
   */
  private void calculate() throws InvalidExpressionException {
    float result = calcModel.evaluate(myView.getExpression(), isInfix);
    myView.setAnswer(Float.toString(result));
  }

  /**
   * This method is notified when a change of expression type is indicated.
   * 
   * @param operationType - the calculator mode which the user wants to use (infix or postfix).
   */
  private void expressionType(OpType operationType) {
    myView.setAnswer("Changed to " + operationType);
    if (operationType == OpType.INFIX) {
      isInfix = true;
    } else {
      isInfix = false;
    }
  }

  /**
   * A constructor for CalcController which registers the observers.
   * 
   * @param model - a CalcModel object passed to the constructor.
   * @param view - a ViewInterface object passed to the constructor.
   */
  CalcController(CalcModel model, ViewInterface view) {
    calcModel = model;
    myView = view;
    // The two lines below parse in the names of the methods (expressionType() and calculate()
    // respectively.
    view.addTypeObserver(this::expressionType);
    view.calcObserver(() -> {
      try {
        calculate();
      } catch (InvalidExpressionException e) {
        e.printStackTrace();
      }
    });
  }
}
