import subprocess as sp

class Logic:

    def penaltyLogic(self, rule):
        """Determines if an object conforms to a penalty logic rule. Returns 0 if it does, the penalty value otherwise."""

    def probabilisticLogic(self, rule):
        """Determines if an object conforms to a probabilistic logic rule. Returns 1 if it does, the probabilistic value
        otherwise."""

    def qualitativeLogic(self, rule):
        """Determines if an object conforms to a qualitative logic rule. Returns the number of the first rule the object
        conforms to, inf if no rules apply."""

    def createFeasibleObjects(self, constraints):
        """Returns a list of all feasible objects, represented in binary\n
        constraints : cnf file, formatted as a string, containing the constraints to use"""
        # Create file using constraints
        fp = open('feasible.cnf', 'w')
        fp.write(constraints)
        fp.close()

        # Run clasp on that file and capture output
        claspOut = sp.run('clingo --mode=clasp feasible.cnf -n 0 --verbose=0', shell=True, capture_output=True)
        claspString = str(claspOut.stdout)
        os.remove("feasible.cnf")

        # If the hard constraints are unsatisfiable, return an empty list
        if "UNSATISFIABLE" in claspString:
            return []

        # Clean up output string
        unquote = claspString.split("\'v ")
        solns = unquote[1].split(" 0\\r\\nv ")
        tempA = len(solns) - 1
        tempB = solns[tempA].split(" 0\\r\\n")
        solns[tempA] = tempB[0]

        # Create objects
        objects = []
        for i in solns:
            tempC = ""
            attributes = i.split()
            for j in attributes:
                if j[0] == "-":
                    tempC += "1"
                else:
                    tempC += "0"
            objects.append(tempC)

        return objects

    def createAllObjects(self, numAttr):
        """Returns a list of all objects possible, in string format, not considering the constraints\n
        attr : number of attributes"""
        # Create .cnf file to print all models
        fp = open('allattr.cnf', 'w')
        fp.write('p cnf ' + str(numAttr) + ' 0')
        fp.close()

        # Run clasp on file and capture output
        claspOut = sp.run('clingo --mode=clasp allattr.cnf -n 0 --verbose=0', shell=True, capture_output=True)
        claspString = str(claspOut.stdout)
        # Delete file
        os.remove("allattr.cnf")

        # Clean up string to put it in a format that we actually need
        unquote = claspString.split("\'v ")
        solns = unquote[1].split(" 0\\r\\nv ")
        tempA = len(solns) - 1
        tempB = solns[tempA].split(" 0\\r\\n")
        solns[tempA] = tempB[0]

        # Generate objects
        objects = []
        for i in solns:
            tempC = ""
            attributes = i.split()
            for j in attributes:
                if j[0] == "-":
                    tempC += "1"
                else:
                    tempC += "0"
            objects.append(tempC)

        return objects
