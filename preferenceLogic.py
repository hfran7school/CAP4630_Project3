import subprocess as sp

class Logic:

    def determinePenaltyPreference(self, objects: list[str], rules: list):
        """Returns a list of tuples of objects, where the earlier in the list an object appears, the more preferred it is.\n
        objects : the objects to apply the rules to, formatted as binary strings\n
        rules : the rules to run the objects against"""
        # Determine the penalties of each object
        objPens = []
        for o in objects:
            penalty = 0
            for r in rules:
                inpRule = r[0]
                if self.checkRule(o, inpRule) == 0:
                    penalty += int(r[1])
            t = (o, penalty)
            objPens.append(t)

        # Determine how many unique penalty values there are and make a list of them
        penalties = []
        for i in objPens:
            if i[1] not in penalties:
                penalties.append(i[1])
        penalties.sort()

        # Prepare result list
        temp = []
        for i in penalties:
            temp.append([])

        # Populate result list
        for i in objPens:
            j = self.findIndex(penalties, i[1])
            temp[j].append(i[0])

        # Convert result list into a list of tuples
        result = []
        for i in temp:
            result.append(tuple(i))

        return result

    def determinePossibilisticPreference(self, objects: list[str], rules: list):
        """Returns a list of tuples of objects, where the earlier in the list an object appears, the more preferred it is.\n
        objects : the objects to apply the rules to, formatted as binary strings\n
        rules : the rules to run the objects against"""
        # Determine the possibilities of each object
        objPens = []
        for o in objects:
            probabilities = []
            for r in rules:
                inpRule = r[0]
                if self.checkRule(o, inpRule) == 0:
                    probabilities.append(float(r[1]))
                else:
                    probabilities.append(1)
            t = (o, min(probabilities))
            objPens.append(t)

        # print("Objects and their penalties:")
        # for i in objPens:
        #     print(i)

        # Determine how many unique penalty values there are and make a list of them
        penalties = []
        for i in objPens:
            if i[1] not in penalties:
                penalties.append(i[1])
        # print("There are " + str(len(penalties)) + " unique possibilistic values.")
        penalties.sort(reverse=True)

        # Prepare result list
        temp = []
        for i in penalties:
            temp.append([])

        # Populate result list
        for i in objPens:
            j = self.findIndex(penalties, i[1])
            temp[j].append(i[0])

        # Convert result list into a list of tuples
        result = []
        for i in temp:
            result.append(tuple(i))

        return result

    def findIndex(self, list, search):
        a = 0;
        for i in list:
            if i == search:
                return a
            a += 1

        return -1;

    def checkRule(self, object: str, rule):
        """Determines if an object conforms to a penalty logic rule. Returns 1 if it does, 0 otherwise."""
        fp = open('checkRule.cnf', 'w')
        fp.write(rule)
        fp.write("\n")
        items = object.split()
        for i in items:
            fp.write(i + " 0\n")
        fp.close()
        claspOut = sp.run('clingo --mode=clasp checkRule.cnf --verbose=0', shell=True, capture_output=True)
        claspString = str(claspOut.stdout)
        os.remove("checkRule.cnf")

        # print("Result of clasp:\n" + claspString)
        if "UNSATISFIABLE" in claspString:
            return 0
        else:
            return 1

    def createFeasibleObjects(self, constraints: str) -> list[str]:
        """Returns a list of all feasible objects. If no feasible objects are possible, return []\n
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
