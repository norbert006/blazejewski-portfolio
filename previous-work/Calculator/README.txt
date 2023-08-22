To run the program, make sure that the file "CalculatorProject-0.0.1-SNAPSHOT-jar-with-dependencies.jar" is present inside 
\Calculator\target. 

If this file is MISSING, open the project and run a Maven Build with goals set as: clean compile package.

If the file is PRESENT, inside your command prompt, change directory to \Calculator\target and run this command: 
	java -jar CalculatorProject-0.0.1-SNAPSHOT-jar-with-dependencies.jar
This will start the Calculator application inside your command prompt.

To use the calculator, first set an expression that you want to be evaluated by typing it out with spaces in between
each character as well as a leading "?". For example, if you want the program to evaluate "3+3", type in "?3 + 3". Then,
choose a mode for the calculator. This can either be infix (I) or postfix (P). Once everything is set, you can run
the calculation by entering "C".