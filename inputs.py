class Inputs:
    def updateDictionary(self, attributes: list):
        count = 1
        dictionary = {}
        for item in attributes:
            readattr = item.split(',')
            dictionary[readattr[0]] = count
            dictionary[readattr[1]] = -count
            count += 1
        return dictionary


    def cnfConstraints(self, constraints: list, cnfDict: dict):
        attr = cnfDict
        numattributes = int(len(attr) / 2)
        numclauses = 0
        textformat = ""
        lastnot = False
        for constr in constraints:
            if textformat != "":
                textformat += "\n"
            parseconstr = constr.split()
            for term in parseconstr:
                if term == "NOT":
                    lastnot = True
                elif lastnot:
                    item = int(attr[term]) * -1
                    textformat += str(item)
                    lastnot = False
                elif term == "AND":  # The AND is implicit in hard constraints -- keeping regardless
                    textformat += " 0\n"
                    numclauses += 1
                elif term == "OR":
                    textformat += " "
                else:
                    textformat += str(attr[term])
            numclauses += 1
            textformat += " 0"
        cnfString = "p cnf " + str(numattributes) + " " + str(numclauses) + "\n" + textformat
        return cnfString

# Used for both PENALTY and POSSIBILISTIC logics
    def cnfLogic(self, logicLines: list, cnfDict: dict):
        logic = cnfDict
        numattr = int(len(logic) / 2)
        numclauses = 1
        textformat = ""
        logictuples = []
        lastnot = False
        for lines in logicLines:
            parselogic = lines.split(',')
            numsave = str(parselogic[1])
            parselogic = parselogic[0].split()
            for term in parselogic:
                if term == "NOT":
                    lastnot = True
                elif lastnot:
                    item = int(logic[term]) * -1
                    textformat += str(item)
                    lastnot = False
                elif term == "AND":
                    textformat += " 0\n"
                    numclauses += 1
                elif term == "OR":
                    textformat += " "
                else:
                    textformat += str(logic[term])
            cnfLogic = "p cnf " + str(numattr) + " " + str(numclauses) + "\n" + textformat + " 0"
            t = cnfLogic, numsave
            logictuples.append(t)
            textformat = ""
            numclauses = 1
        return logictuples  # Returns list of tuples in format of [(cnfstring, value), ...]

# Used for QUALITATIVE logic
    def cnfQualitative(self, qualLines: list, cnfDict: dict):
        numattr = int(len(cnfDict) / 2)
        numclauses = 1
        textformat = ""
        qualtuples = []
        rule = []
        lastnot = False
        for lines in qualLines:
            if lines.endswith("IF"):
                condition = "0"
                qualitems = lines.split("IF")
                quallist = qualitems[0].split()
            else:
                qualitems = lines.split("IF")
                condition = str(cnfDict[qualitems[1]])
                quallist = qualitems[0].split()
            for term in quallist:
                if term == "NOT":
                    lastnot = True
                elif lastnot:
                    item = int(cnfDict[term]) * -1
                    textformat += str(item)
                    lastnot = False
                elif term == "AND":
                    textformat += " 0\n"
                    numclauses += 1
                elif term == "OR":
                    textformat += " "
                elif term == "BT":
                    cnfQual = "p cnf " + str(numattr) + " " + str(numclauses) + "\n" + textformat + " 0"
                    rule.append(cnfQual)
                    textformat = ""
                    numclauses = 1
                else:
                    textformat += str(cnfDict[term])
            cnfQual = "p cnf " + str(numattr) + " " + str(numclauses) + "\n" + textformat + " 0"
            rule.append(cnfQual)
            t = condition, tuple(rule)
            qualtuples.append(t)
            rule[:] = []
            textformat = ""
            numclauses = 1
        return qualtuples  # Returns list of tuples in format of [(condition, (cnf, ...)), ...]
        # Condition will be 0 if there are no conditions.
