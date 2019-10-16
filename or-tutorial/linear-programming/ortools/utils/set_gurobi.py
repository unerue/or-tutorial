from gurobipy import *
from pulp import *


def set_gurobi(model, verbose=True):
    assert type(model) == gurobipy.Model, 'Not gurobi model...'

    if verbose:
        model.setParam(GRB.Param.OutputFlag, 1)
    else:
        model.setParam(GRB.Param.OutputFlag, 0)
