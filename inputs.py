"""
    provide in the same format as (cnf, value)
"""

" sets up the program to recognize attributes and their cnf numbers in the next files "
with open ('filename') as attrfile:
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
        attributes[parseattr[0]] = {count}
        attributes[parseattr[1]] = {-count}
        " incrementing & reseting "
        count += 1
        readattr = attrfile.readline()
        parseattr[:] = []

" Hard constraints "
with open ('filename') as constrfile:
    count = 1
    readconstr = constrfile.readline()