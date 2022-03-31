import subprocess as sp
import os
import random

class Logic:

    def determinePenaltyPreference(self, objects: list[str], rules: list):
        """Returns a list of tuples of objects, where the earlier in the list an object appears, the more preferred it is. This function uses penalty logic.\n
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
        """Returns a list of tuples of objects, where the earlier in the list an object appears, the more preferred it is. This function uses possibilistic logic.\n
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
        """Returns the index of a value in a list, or -1 if it can't be found41"""
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

    def exemplify(self, feasibleObjects: list, rules: tuple) -> list:
        """
        Picks two feasible objects at random, and compares them according to the different logics.\n
        :param feasibleObjects: the list of feasible objects
        :param rules: the preference rules to use. Must be a 3-tuple, with the elements being the rules for penalty, possibilistic, and qualitative logics, respectfully
        :return: a list containing a 2-tuple with the objects used, and the number of the object (1 or 2) that is preferred for each of the logics, in the above order, with 0 being congruency (and -1 for incompatibility for qualitative)
        """
        # Select two random objects
        results = []
        obj1Int = random.randrange(0, len(feasibleObjects))
        obj2Int = random.randrange(0, len(feasibleObjects))
        if obj1Int == obj2Int:
            if obj2Int+1 == len(feasibleObjects):
                obj2Int -= 1
            else:
                obj2Int += 1
        obj1 = feasibleObjects[obj1Int]
        obj2 = feasibleObjects[obj2Int]
        results.append((obj1, obj2))

        # Test 1: Penalty logic. Ruleset = rules[0]
        penaltyResults = self.determinePenaltyPreference([obj1, obj2], rules[0])
        if len(penaltyResults) != 2:
            results.append(0)
        else:
            if penaltyResults[0][0] == obj1:
                results.append(1)
            else:
                results.append(2)

        # Test 2: Possibilistic logic. Ruleset = rules[1]
        possibilisticResults = self.determinePossibilisticPreference([obj1, obj2], rules[1])
        if len(possibilisticResults) != 2:
            results.append(0)
        else:
            if possibilisticResults[0][0] == obj1:
                results.append(1)
            else:
                results.append(2)

        # Test 3: Qualitative Choice logic. Ruleset = rules[2]
        # TODO: this part

        return results

    def omniOptimize(self, feasibleObjects: list, rules: tuple):
        """
        Runs penalty, possibilistic, and qualitative logics on all feasible objects, and returns all optimal objects.\n
        :param feasibleObjects: all feasible objects
        :param rules: the preference rules to use. Must be a 3-tuple, with the elements being the rules for penalty, possibilistic, and qualitative logics, respectfully
        :return: a list containing tuples of the optimal objects for each logic, in order (penalty, possibilistic, qualitative)
        """
        penaltyOptimal = self.determinePenaltyPreference(feasibleObjects, rules[0])
        possibilisitcOptimal = self.determinePossibilisticPreference(feasibleObjects, rules[1])
        # TODO: qualitativeOptimal = self.determineQualitativePreference(feasibleObjects, rules[2]
        return [penaltyOptimal[0], possibilisitcOptimal[0]]

    def optimize(self, feasibleObjects: list, rules: tuple):
        """
        Runs omniOptimize, selects one random element from each tuple, and returns each.\n
        :param feasibleObjects: all feasible objects
        :param rules: the preference rules to use. Must be a 3-tuple, with the elements being the rules for penalty, possibilistic, and qualitative logics, respectfully
        :return: a list containing one optimal object for each of the logics
        """
        optimal = self.omniOptimize(feasibleObjects, rules)
        rand1 = random.randrange(0, len(optimal[0]))
        rand2 = random.randrange(0, len(optimal[1]))

        return [optimal[0][rand1], optimal[1][rand2]]

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
        # objects = []
        # for i in solns:
        #     tempC = ""
        #     attributes = i.split()
        #     for j in attributes:
        #         if j[0] == "-":
        #             tempC += "1"
        #         else:
        #             tempC += "0"
        #     objects.append(tempC)

        return solns
