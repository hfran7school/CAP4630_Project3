import subprocess as sp

class Logic:

    def determinePenaltyPreference(self, objects: list[str], rules: list):
        """Returns a list of tuples of objects, where the earlier in the list an object appears, the more preferred it is.\n
        objects : the objects to apply the rules to, formatted as binary strings\n
        rules : the rules to run the objects against"""
        # for each object
            # for each rule
                # if object satisfies rule
                    # object penalty = 0
                # else
                    # object penalty = rule[2] (aka rule penalty)
        # for each object
            # tuple together with


    def penaltyLogic(self, rule):
        """Determines if an object conforms to a penalty logic rule. Returns 0 if it does, the penalty value otherwise."""

    def possiblisticLogic(self, rule):
        """Determines if an object conforms to a probabilistic logic rule. Returns 1 if it does, the probabilistic value
        otherwise."""

    def qualitativeLogic(self, rule):
        """Determines if an object conforms to a qualitative logic rule. Returns the number of the first rule the object
        conforms to, inf if no rules apply."""

    def createFeasibleObjects(self, constraints: str) -> list[str]:
        """Returns a list of all feasible objects, represented as binary strings. If no feasible objects are possible, return []\n
        constraints : cnf file, formatted as a string, containing the constraints to use\n
        ** Example use: createFeasibleObjects(\"p cnf 4 2\\\\n2 -3 0\\\\n-4 1 0\")"""
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
        # objects = []
        # for i in solns:
        #     tempC = ""
        #     attributes = i.split()
        #     for j in attributes:
        #         if j[0] == "-":
        #             tempC += "0"
        #         else:
        #             tempC += "1"
        #     objects.append(tempC)

        return solns

    def createAllObjects(self, numAttr: int) -> list[str]:
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
