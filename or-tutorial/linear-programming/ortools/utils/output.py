import gurobipy
import pulp 
from tabulate import tabulate


def output(model, sensitivity=False):
    if type(model) == pulp.LpProblem and model.status == pulp.LpStatusOptimal:
        print('Status: {}'.format(pulp.LpStatus[model.status]))
        print('Objective value: {}\n'.format(pulp.value(model.objective)))
        
        if  sensitivity:           
            table = []
            for i in model.variables():
                table.append([i.name, i.varValue, i.dj])
            
            print(tabulate(table, headers=['Variables', 'Values', 'Reduced costs']))

            # Sensitivity Analysis
            print('\nSensitivity Analysis:')

            table = []
            for name, c in model.constraints.items():
                table.append([name, c.pi, c.slack])

            print(tabulate(table, headers=['Constraints', 'Shadow prices', 'Slack']))

        else:
            table = []
            for i in model.variables():
                table.append([i.name, i.varValue])
            
            print(tabulate(table, headers=['Variables', 'Values']))

        print('\nStatistics:\n- Number of variables: {}'.format(len(model.variables())))
        print('- Number of constraints: {}'.format(len(model.constraints)))
        print('- Solve time: {:.3f}s'.format(model.solutionTime))
        
    elif type(model) == gurobipy.Model and model.status == gurobipy.GRB.OPTIMAL:
        print('Status: Optimal')
        print('Objective value: {}\n'.format(model.objVal))
        
        if  sensitivity:           
            table = []
            for v in model.getVars():
                table.append([v.varName, v.x, v.RC])
            
            print(tabulate(table, headers=['Variables', 'Values', 'Reduced costs']))

            # Sensitivity Analysis
            print('\nSensitivity Analysis:')

            table = []
            for c in model.getConstrs():
                table.append([c.ConstrName, c.Pi, c.Slack])

            print(tabulate(table, headers=['Constraints', 'Shadow prices', 'Slack']))

        else:
            table = []
            for v in model.getVars():
                table.append([v.varName, v.x])
            
            print(tabulate(table, headers=['Variables', 'Values']))

        print('\nStatistics:\n- Number of variables: {}'.format(model.numVars))
        print('- Number of constraints: {}'.format(model.numConstrs))
        print('- Solve time: {:.3f}s'.format(model.runTime))

    else:
        print('Not optimal')