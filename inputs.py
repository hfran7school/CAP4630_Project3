"""
    provide in the same format as (cnf, value)
"""

" sets up the program to recognize attributes and their cnf numbers in the next files "
def claspFeasObj():
    with open ('attributes.txt') as attrfile:
        count = 1
        readattr = attrfile.readline()
        attrnames = []
        attributes = {}

        while readattr != '':
            parseattr = readattr.split(':')
            head = parseattr[0]
            if head in attrnames:
                readattr = attrfile.readline()
                parseattr[:] = []
                continue
            attrnames.append(head)
            parseattr = parseattr[1].split(',')
            parseattr[0]=parseattr[0].replace(" ","")
            parseattr[1]=parseattr[1].replace(" ","")
            parseattr[0]=parseattr[0].replace("\n","")
            parseattr[1]=parseattr[1].replace("\n","")
            attributes[parseattr[0]] = count
            attributes[parseattr[1]] = -count
            " incrementing & reseting "
            count += 1
            readattr = attrfile.readline()
            parseattr[:] = []

    " Hard constraints "
    with open ('hardconstraints.txt') as constrfile:
        countsave = count
        count = 0
        constraintcount = 0
        readconstr = constrfile.readline()
        textformat = ""

        while readconstr != '':
            parseconstr = readconstr.split()
            for term in parsepref:
                if term == "NOT":
                    lastnot = True
                elif lastnot:
                    item = int(attributes[term]) * -1
                    textformat += str(item)
                    lastnot = False
                elif term == "AND":
                    textformat += " 0,"
                elif term == "OR":
                    textformat += " "
                else:
                    textformat += attributes[term]
                preferencecount += 1
        # CNF form text for hard constraints.
        ConstraintCNF = "p cnf " + str(countsave) + " " + str(preferencecount) + "," + textformat + " 0"
        return ConstraintCNF
        " This is currently set up w/o new lines between each line. I can set it up to go out to a file -- just need to" \
        " know how it's getting moved to fix it's output because it won't change much. "

    " Penalty logic "
    with open('penalty.txt') as penfile:
        lastnot = False
        preferencecount = 0
        readpen = penfile.readline()
        pentuples = []
        textformat = ""

        while readpen != '':
            parsepref = readpen.split(',')
            numsave = parsepref[1]
            for term in parsepref:
                if term == "NOT":
                    lastnot = True
                elif lastnot:
                    item = int(attributes[term]) * -1
                    textformat += item
                    lastnot = False
                elif term == "AND":
                    textformat += " 0,"
                elif term == "OR":
                    textformat += " "
                else:
                    textformat += attributes[term]
                preferencecount += 1
            PenaltyCNF = "p cnf " + str(countsave) + " " + str(preferencecount) + "," + textformat + " 0"
            t = PenaltyCNF, numsave
            # pentuples is a list of tuples -- The tuples contain 2 strings each with the first being the CNF and the
            # second being the value associated with penalty
            pentuples.append(t)
            readpen = penfile.readline()
    " Possibilistic Logic "
    with open('possibilistic.txt') as possfile:
        lastnot = False
        preferencecount = 0
        readposs = possfile.readline()
        posstuples = []
        textformat = ""

        while readposs != '':
            parsepref = readposs.split(',')
            numsave = parsepref[1]
            for term in parsepref:
                if term == "NOT":
                    lastnot = True
                elif lastnot:
                    item = int(attributes[term]) * -1
                    textformat += item
                    lastnot = False
                elif term == "AND":
                    textformat += " 0,"
                elif term == "OR":
                    textformat += " "
                else:
                    textformat += attributes[term]
                preferencecount += 1
            PossibilisticCNF = "p cnf " + str(countsave) + " " + str(preferencecount) + "," + textformat + " 0"
            t = PossibilisticCNF, numsave
            # posstuples is a list of tuples -- The tuples contain 2 strings each with the first being the CNF and the
            # second being the value associated with possibilistic logic
            posstuples.append(t)
            readposs = possfile.readline()
    " Qualitative Logic "
    with open('qualitative.txt') as qualfile:
        " Need to set this up to prepare qualitative logic rules "
