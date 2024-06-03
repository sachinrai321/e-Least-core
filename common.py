import numpy as np
import cvxpy as cp

def calculate_least_core(players, values):
    # players: list of player IDs
    # values: dict of coalition values
    
    n = len(players)
    coalitions = list(values.keys())
    
    # Define the cvxpy variables
    x = cp.Variable(n)
    epsilon = cp.Variable()
    
    # Define the constraints
    constraints = []
    for coalition in coalitions:
        coalition_value = values[coalition]
        constraints.append(cp.sum([x[players.index(player)] for player in coalition]) >= coalition_value - epsilon)
    
    # Define the objective
    objective = cp.Minimize(epsilon)
    
    # Define and solve the problem
    prob = cp.Problem(objective, constraints)
    prob.solve()
    
    least_core_value = prob.value
    least_core_distribution = x.value
    
    return least_core_value, least_core_distribution
