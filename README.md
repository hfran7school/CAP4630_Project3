# CAP4630_Project3
Authors: Hailey Francis, Jacob McGee, Edward Hage

# Requirements and Relevent Information
- On startup, the files "attributes.txt", "constraints.txt", "penalty.txt", "possible.txt" and "qualitative.txt" must be in the same directory as the source code.
- We are expecting "attributes.txt", "constraints.txt", "penalty.txt", "possible.txt" and "qualitative.txt" to be formatted correctly with respect to one another with all "Update with File Info" buttons: there is no error-checking implementing for validating if the file is useable.
- The Optimize and Omni-Optimize buttons may take a while to calculate. A pop-up window will appear with that warning, but it needs to be closed for the computation to actually begin.

# Instructions
- Make sure main.py, inputs.py, and preferenceLogic.py are in the same directory
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

- Clicking the "Exemplify" button will generate two random objects from the list of feasible objects and return which objects are preferred over the other: either "Object 1", "Object 2", "Congruent", or "Incomparable." This information will appear in a new window.

- Clicking the "Optimize" button will find an optimal object w.r.t each of the different preferences. This information will appear in a new window.

- Clicking the "Omni-Optimize" button will generate all the optimal objects for each of the three preference. This information will appear in a new window.

- This program does not support the deletion of individual attributes, constraints, and preferences. If you would like to restart, click the "Reset" button to clear the data in all lists as well as the associated files.

- If you'd like to exit the program, select the "Quit" button.
