from gurobipy import *
from pulp import *


def output(model):
    if type(model) == pulp.LpProblem:
        pass
    elif type(model) == gurobipy.Model:
        pass