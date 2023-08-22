package uk.ac.rhul.cs2800;

import java.util.Scanner;
import java.util.function.Consumer;

/**
 * A menu available to use through the terminal.
 * Credit to Dave Cohen. This class is influenced by the AsciiView class from the MVCJavaFX example.
 * Adjustments have been made to fit the calculator project by printing the str parameter in the
 * setAnswer method. Some variable names have also been changed to make the code clearer to read.
 * 
 * @author Norbert Blazejewski
 *
 */
public class AsciiView implements ViewInterface {

  private String question;
  Runnable calculator = null;
  Consumer<OpType> operationType = null;

  /**
   * This method is responsible for displaying the main menu to the user and notifies corresponding
   * observers to print the answer.
   */
  public void menu() {
    Scanner sc = new Scanner(System.in);
    boolean scanningFinished = false;
    instructions();

    while (!scanningFinished && sc.hasNext()) {
      String inputCharacter = sc.nextLine();
      switch (inputCharacter.charAt(0)) {
        case 'C':
        case 'c':
          if (calculator != null) {
            calculator.run();
          }
          break;
        case 'I':
        case 'i':
          if (operationType != null) {
            operationType.accept(OpType.INFIX);
          }
          break;
        case 'P':
        case 'p':
          if (operationType != null) {
            operationType.accept(OpType.POSTFIX);
          }
          break;
        case '?':
          question = inputCharacter;
          question = question.substring(1);
          System.out.println("Question set to: " + question);
          break;
        case 'Q':
        case 'q':
          System.out.println("Bye");
          scanningFinished = true;
          break;
        default:
          instructions();
      }
    }
    sc.close();
  }

  /**
   * A cheatsheet to help the user use the calculator.
   */
  public void instructions() {
    System.out.println("To set an expression, use spaces between variables");
    System.out.println("For example, write 3+3 as 3 + 3");
    System.out.println("Use one of the following:");
    System.out.println("- ?Expression - to set expression");
    System.out.println("- P - to change to postfix");
    System.out.println("- I - to change to infix");
    System.out.println("- C - to calculate");
    System.out.println("- Q - to exit");
  }


  /**
   * Get the arithmetic expression from the user in a String format.
   * 
   * @return arithmetic expression to be evaluated (as a String).
   */
  @Override
  public String getExpression() {
    return question;
  }

  /**
   * A method to enable showing the user the answer to their arithmetic expression.
   * 
   * @param str - the answer.
   */
  @Override
  public void setAnswer(String str) {
    System.out.println(str);
  }

  /**
   * Adds an observer of the Calculate action.
   * 
   * @param f - the (Runnable) observer to be notified.
   */
  @Override
  public void calcObserver(Runnable f) {
    calculator = f;
  }

  /**
   * Adds an observer to recognise the change in mode for the Calculate action.
   * 
   * @param f - the observer of type OpType (which is defined in an enum as either an infix or
   *        postfix).
   */
  @Override
  public void addTypeObserver(Consumer<OpType> f) {
    operationType = f;
  }

}
