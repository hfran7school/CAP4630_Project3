"""
    provide in the same format as (cnf, value)
"""

" sets up the program to recognize attributes and their cnf numbers in the next files "
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
            continue
        attrnames.append(head)
        parseattr = parseattr[1].split(',')
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
        if parseconstr[count] == "NOT":
            count += 1
            item1 = int(attributes[parseconstr[count]]) * -1
            " made it an int so its easier to negate negatives "
        item1 = attributes[parseconstr[count]]
        count += 2
        if parseconstr[count] == "NOT":
            count += 1
            item2 = int(attributes[parseconstr[count]]) * -1
        item2 = attributes[parseconstr[count]]
        textformat += str(item1) + " " + str(item2) + " 0"
        count = 0
        constraintcount += 1
    " use for hard constraints "
    textformatC = "p cnf " + str(countsave) + str(constraintcount) + textformat
    " This is currently set up w/o new lines between each line. I can set it up to go out to a file -- just need to" \
    " know how it's getting moved to fix it's output because it won't change much. "

with open('preferences.txt') as preffile:
    lastnot = False
    count = 0
    preferencecount = 0
    readpref = preffile.readline()
    preftuples = []
    textformat = ""

    while readpref != '':
        " If it has a comma then it's either penalty or possibilistic "
        if readpref.contains(','):
            parsepref = readpref.split(',')
            numsave = parsepref[1]
            for term in parsepref:
                if term == "NOT":
                    lastnot = True
                elif lastnot:
                    item = int(attributes[term]) * -1
                    textformat += item
                    lastnot = False
                elif term == "AND":
                    textformat += " 0"
                elif term == "OR":
                    textformat += " "
                else:
                    textformat += attributes[term]
                preferencecount += 1
            textformatC = "p cnf " + str(countsave) + str(preferencecount) + textformat
            t = textformatC, numsave
            preftuples.append(t)
            " Unsure how to have it formatted but the cnf form and number associated are present "
        elif true:
            a = 0
        " I don't know how to format the cnf for qualitative logic "
