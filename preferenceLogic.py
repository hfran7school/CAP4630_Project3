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

    def createFeasibleObjects(self, constraint):
        """Returns a list of all feasible objects, represented in binary"""

    def createAllObjects(self, attr):
        """Returns a list of all objects possible, not considering the constraints\nattr : number of attributes"""
        fp = open('allattr.cnf', 'w')
        fp.write('p cnf ' + attr + ' 0')
        fp.close()
        claspOut = sp.run('clingo --mode=clasp allattr.cnf -n 0', shell=True, capture_output=True)
        print(claspOut)
