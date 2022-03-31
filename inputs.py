def updateDictionary(attributes: list):
    count = 1
    dictionary = {}
    for item in attributes:
        readattr = item.split(',')
        dictionary[readattr[0]] = count
        dictionary[readattr[1]] = -count
        count += 1
    return dictionary


def cnfConstraints(constraints: list, cnfDict: dict):
    attr = cnfDict
    numattributes = len(attr)
    numclauses = 1
    textformat = ""
    for constr in constraints:
        parseconstr = constr.split()
        for term in parseconstr:
            if term == "NOT":
                lastnot = True
            elif lastnot:
                item = int(attr[term]) * -1
                textformat += str(item)
                lastnot = False
            elif term == "AND":
                textformat += " 0\n"
                numclauses += 1
            elif term == "OR":
                textformat += " "
            else:
                textformat += str(attr[term])
    cnfString = "p cnf " + str(numattributes) + " " + str(numclauses) + "\n" + textformat + " 0"
    return cnfString

# def cnfLogic(logic):
#     logic = cnfDictionary
#     numattr = len(pen)
#     numclauses = 1
#     readlogic = logic.split('\n')
#     textformat = ""
#     logictuples = []
#     for lines in readlogic:
#         parselogic = lines.split(',')
#         numsave = parselogic[1]
#         parselogic = parselogic[0].split()
#         for term in parselogic:
#             if term == "NOT":
#                 lastnot = True
#             elif lastnot:
#                 item = int(logic[term]) * -1
#                 textformat += str(item)
#                 lastnot = False
#             elif term == "AND":
#                 textformat += " 0\n"
#                 numclauses += 1
#             elif term == "OR":
#                 textformat += " "
#             else:
#                 textformat += logic[term]
#         cnfLogic = "p cnf " + str(numattr) + " " + str(numclauses) + "\n" + textformat + " 0"
#         t = cnfLogic, numsave
#         logictuples.append(t)
#         textformat = ""


# # All of below will receive the cnf dictionary and string representing the contents of the file
# " Hard constraints "
# with open ('hardconstraints.txt') as constrfile: # Will return a string representing the cnf file
#     countsave = count
#     count = 0
#     constraintcount = 0
#     readconstr = constrfile.readline()
#     textformat = ""
#
#     while readconstr != '':
#         parseconstr = readconstr.split()
#         for term in parsepref:
#             if term == "NOT":
#                 lastnot = True
#             elif lastnot:
#                 item = int(attributes[term]) * -1
#                 textformat += str(item)
#                 lastnot = False
#             elif term == "AND":
#                 textformat += " 0\n"
#             elif term == "OR":
#                 textformat += " "
#             else:
#                 textformat += attributes[term]
#             preferencecount += 1
#     # CNF form text for hard constraints.
#     ConstraintCNF = "p cnf " + str(countsave) + " " + str(preferencecount) + "\n" + textformat + " 0"
# " Penalty logic "
# with open('penalty.txt') as penfile:
#     lastnot = False
#     preferencecount = 0
#     readpen = penfile.readline()
#     pentuples = []
#     textformat = ""
#
#     while readpen != '':
#         parsepref = readpen.split(',')
#         numsave = parsepref[1]
#         for term in parsepref:
#             if term == "NOT":
#                 lastnot = True
#             elif lastnot:
#                 item = int(attributes[term]) * -1
#                 textformat += item
#                 lastnot = False
#             elif term == "AND":
#                 textformat += " 0\n"
#             elif term == "OR":
#                 textformat += " "
#             else:
#                 textformat += attributes[term]
#             preferencecount += 1
#         PenaltyCNF = "p cnf " + str(countsave) + " " + str(preferencecount) + "\n" + textformat + " 0"
#         t = PenaltyCNF, numsave
#         # pentuples is a list of tuples -- The tuples contain 2 strings each with the first being the CNF and the
#         # second being the value associated with penalty
#         pentuples.append(t)
#         readpen = penfile.readline()
# " Possibilistic Logic "
# with open('possibilistic.txt') as possfile:
#     lastnot = False
#     preferencecount = 0
#     readposs = possfile.readline()
#     posstuples = []
#     textformat = ""
#
#     while readposs != '':
#         parsepref = readposs.split(',')
#         numsave = parsepref[1]
#         for term in parsepref:
#             if term == "NOT":
#                 lastnot = True
#             elif lastnot:
#                 item = int(attributes[term]) * -1
#                 textformat += item
#                 lastnot = False
#             elif term == "AND":
#                 textformat += " 0\n"
#             elif term == "OR":
#                 textformat += " "
#             else:
#                 textformat += attributes[term]
#             preferencecount += 1
#         textformatC = "p cnf " + str(countsave) + " " + str(preferencecount) + "\n" + textformat + " 0"
#         t = textformatC, numsave
#         # posstuples is a list of tuples -- The tuples contain 2 strings each with the first being the CNF and the
#         # second being the value associated with possibilistic logic
#         posstuples.append(t)
#         readposs = possfile.readline()
