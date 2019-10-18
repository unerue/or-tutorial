from gurobipy import *
from pulp import *


def custom_callback(model, where):
    if where == GRB.Callback.SIMPLEX:
        time = model.cbGet(GRB.Callback.RUNTIME)
        if time > 10:
            model.terminate()
            
    elif where == GRB.Callback.MIP:
        time = model.cbGet(GRB.Callback.RUNTIME)
        if time > 10:
            model.terminate()