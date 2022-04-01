# CAP4630_Project3
Authors: Hailey Francis, Jacob McGee, Edward Hage

# Relevant Information
- On startup, the files "attributes.txt", "constraints.txt", "penalty.txt", "possible.txt" and "qualitative.txt" will be created. If they already exist in the current directory, they will be overwritten.
- (Have not decided if the files will be cleared or deleted on program close)

# Instructions
- Make sure main.py, inputs.py, and preferenceLogic.py are in the same directory. For Windows users, ensure clingo.exe is in the same folder as the other Python files.
- Run "python main.py" in command line to open the User Interface.

- To add the binary attributes you wish to use, put the attribute name in the "Attribute" box, and put the two binary options in "Option 1" and "Option 2", then click the "Add Attribute" button.
Example:)
Attribute: Cheese
Option 1: Cheddar
Option 2: Swiss
This will add your binary attribute in a list for you to see, as well as write it to a file called "attributes.txt".

- To add hard constraints, enter the constraint in the proper CNF format in the "Constraint" textbox. Once you hit the "Add Constraint" button, it will add the constraint on the list for you to see as well as write it to the file "constraints.txt"

- To add penalty logic and possibilistic logic, enter the preference in proper CNF form in the "Preference" textbox and the associated value attatched to the preference in the "Value" box (penalty value for penalty logic, decimal probability between 0-1 for possibilistic logic).

- To add qualitative logic...

- To get a list of feasible objects, once you have your binary attributes and hard constraints added, click the "Update" button in Feasible Objects section to generate the list of all feasible objects w.r.t. the hard constraints you have.

- Clicking the "Exemplify" button will choose two random feasible objects and determine, through penalty, possibilistic, and qualitative logic, which one is preferred over the other.

- Clicking the "Optimize" button will choose a feasible object that is the most optimal with respect to the penalty, possibilistic, and qualitative logic rules provided.

- Clicking the "Omni-Optimize" button does the same as optimize, but instead displays all optimal feasible objects.

- This program does not support the deletion of individual attributes, constraints, and preferences. If you would like to restart, click the "Reset" button to clear the data in all lists as well as the associated files.

- If you'd like to exit the program, select the "Quit" button.
