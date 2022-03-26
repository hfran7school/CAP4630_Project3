import pyclasp as clasp

class Logic:

    def penaltyLogic(self, obj, rule):
        """Determines if an object conforms to a penalty logic rule. Returns 0 if it does, the penalty value otherwise."""

    def probabilisticLogic(self, obj, rule):
        """Determines if an object conforms to a probabilistic logic rule. Returns 1 if it does, the probabilistic value
        otherwise."""

    def qualitativeLogic(self, obj, rule):
        """Determines if an object conforms to a qualitative logic rule. Returns the number of the first rule the object
        conforms to, inf if no rules apply."""

    def createFeasibleObjects(self, obj, constraint):
        """Returns a list of all feasible objects, represented in binary"""

    def createAllObjects(self, attr):
        """Returns a list of all objects possible, not considering the constraints"""
