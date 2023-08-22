package uk.ac.rhul.cs2800;

/**
 * This class is responsible for running the calculator application through the terminal.
 * 
 * @author Norbert Blazejewski
 *
 */
public class Driver {

  /**
   * Launch a standalone application.
   * 
   * @param args - the command line arguments passed to the application.
   */
  public static void main(String[] args) {
    if (System.console() != null) {
      AsciiView v = new AsciiView();
      CalcModel m = new CalcModel();
      new CalcController(m, v);
      v.menu();
    }
  }
}


