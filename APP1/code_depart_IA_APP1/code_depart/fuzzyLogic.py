import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
from Games2D import *

def createFuzzyController():
    # TODO: Create the fuzzy variables for inputs and outputs.
    # Defuzzification (defuzzify_method) methods for fuzzy variables:
    #    'centroid': Centroid of area
    #    'bisector': bisector of area
    #    'mom'     : mean of maximum
    #    'som'     : min of maximum
    #    'lom'     : max of maximum

    #in
    direction = ctrl.Antecedent(np.linspace(-1, 1, 1000), 'direction')
    up_p = ctrl.Antecedent(np.linspace(0, 170, 1000), 'up_p')
    down_p = ctrl.Antecedent(np.linspace(0, 170, 1000), 'down_p')
    left_p = ctrl.Antecedent(np.linspace(0, 170, 1000), 'left_p')
    right_p = ctrl.Antecedent(np.linspace(0, 170, 1000), 'right_p')


    #out
    move = ctrl.Consequent(np.linspace(0, 360, 1000), 'move', defuzzify_method='centroid')
    #move_y = ctrl.Consequent(np.linspace(-1, 1, 10), 'move_y', defuzzify_method='centroid')

    # Accumulation (accumulation_method) methods for fuzzy variables:
    #    np.fmax
    #    np.multiply
    move.accumulation_method = np.fmax
    #move_y.accumulation_method = np.fmax

    # TODO: Create membership functions
    #dir = ['up', 'down', 'left', 'right']
    #direction.automf(names=dir)
    #direction['up'] = fuzz.trimf(direction.universe, [-1, -0.75, -0.5])
    #direction['down'] = fuzz.trimf(direction.universe, [-0.5, -0.25, 0])
    #direction['left'] = fuzz.trimf(direction.universe, [0, 0.25, 0.5])
    #direction['right'] = fuzz.trimf(direction.universe, [0.5, 0.75, 1])

    up_p['leave'] = fuzz.trapmf(up_p.universe, [0, 0, 10, 15])
    up_p['go_to'] = fuzz.trapmf(up_p.universe, [0, 80, 170, 170])

    down_p['leave'] = fuzz.trapmf(down_p.universe, [0, 0, 10, 15])
    down_p['go_to'] = fuzz.trapmf(down_p.universe, [0, 80, 170, 170])

    right_p['leave'] = fuzz.trapmf(right_p.universe, [0, 0, 10, 15])
    right_p['go_to'] = fuzz.trapmf(right_p.universe, [0, 80, 170, 170])

    left_p['leave'] = fuzz.trapmf(left_p.universe, [0, 0, 10, 15])
    left_p['go_to'] = fuzz.trapmf(left_p.universe, [0, 80, 170, 170])

    direction = ['HD', 'HG', 'BG', 'BD']
    move.automf(names=direction)
    #move['left'] = fuzz.trimf(move_x.universe, [-1, -1, 0])
    #move['right'] = fuzz.trimf(move_x.universe, [0, 1, 1])
    #move['up'] = fuzz.trimf(move_x.universe, [-1, -1, 0])
    #move['down'] = fuzz.trimf(move_x.universe, [0, 1, 1])

    # TODO: Define the rules.
    rules = []
    #------------------------------------------------------------------------------------------------------------------#
    #-----------------------------------------------go_to--------------------------------------------------------------#
    #------------------------------------------------------------------------------------------------------------------#
    rules.append(ctrl.Rule(antecedent=(up_p['go_to']),
                           consequent=(move['HD'], move['HG'])))
    rules.append(ctrl.Rule(antecedent=(down_p['go_to']),
                           consequent=(move['BD'], move['BG'])))
    rules.append(ctrl.Rule(antecedent=(left_p['go_to']),
                           consequent=(move['HG'], move['BG'])))
    rules.append(ctrl.Rule(antecedent=(right_p['go_to']),
                           consequent=(move['HD'], move['BD'])))
    # -----------------------------------------------------------------------------------------------------------------#
    # -----------------------------------------------LEAVE-------------------------------------------------------------#
    # -----------------------------------------------------------------------------------------------------------------#
    #rules.append(ctrl.Rule(antecedent=(up_p['leave']),
    #                       consequent=(move_y['down'])))
    #rules.append(ctrl.Rule(antecedent=(down_p['leave']),
    #                       consequent=(move_y['up'])))
    #rules.append(ctrl.Rule(antecedent=(left_p['leave']),
    #                       consequent=(move_x['right'])))
    #rules.append(ctrl.Rule(antecedent=(right_p['leave']),
    #                       consequent=(move_x['left'])))
    # -----------------------------------------------------------------------------------------------------------------#
    # -----------------------------------------------down-------------------------------------------------------------#
    # -----------------------------------------------------------------------------------------------------------------#
    #rules.append(ctrl.Rule(antecedent=(down_p['leave'] & left_p['leave'] & right_p['go_to']),
    #                       consequent=(move['up'])))
    rules.append(ctrl.Rule(antecedent=(down_p['go_to'] & left_p['leave'] & right_p['go_to']),
                           consequent=(move['BD'])))
    rules.append(ctrl.Rule(antecedent=(down_p['go_to'] & left_p['go_to'] & right_p['leave']),
                           consequent=(move['BG'])))
    # -----------------------------------------------------------------------------------------------------------------#
    # -----------------------------------------------up----------------------------------------------------------------#
    # -----------------------------------------------------------------------------------------------------------------#
    #rules.append(ctrl.Rule(antecedent=(up_p['leave'] & left_p['leave'] & right_p['go_to']),
    #                       consequent=(move['up'])))
    rules.append(ctrl.Rule(antecedent=(up_p['go_to'] & left_p['leave'] & right_p['go_to']),
                           consequent=(move['BD'])))
    rules.append(ctrl.Rule(antecedent=(down_p['go_to'] & left_p['go_to'] & right_p['leave']),
                           consequent=(move['BG'])))
    # -----------------------------------------------------------------------------------------------------------------#
    # -----------------------------------------------left--------------------------------------------------------------#
    # -----------------------------------------------------------------------------------------------------------------#
    #rules.append(ctrl.Rule(antecedent=(down_p['leave'] & left_p['leave'] & right_p['go_to']),
    #                       consequent=(move['up'])))
    rules.append(ctrl.Rule(antecedent=(down_p['go_to'] & left_p['leave'] & right_p['go_to']),
                           consequent=(move['BD'])))
    rules.append(ctrl.Rule(antecedent=(down_p['go_to'] & left_p['go_to'] & right_p['leave']),
                           consequent=(move['BG'])))
    # -----------------------------------------------------------------------------------------------------------------#
    # -----------------------------------------------right-------------------------------------------------------------#
    # -----------------------------------------------------------------------------------------------------------------#
    #rules.append(ctrl.Rule(antecedent=(down_p['leave'] & left_p['leave'] & right_p['go_to']),
    #                       consequent=(move['up'])))
    rules.append(ctrl.Rule(antecedent=(right_p['go_to'] & left_p['leave'] & right_p['go_to']),
                           consequent=(move['BD'])))
    rules.append(ctrl.Rule(antecedent=(down_p['go_to'] & left_p['go_to'] & right_p['leave']),
                           consequent=(move['BG'])))
    tt

    for rule in rules:
        #somme ou somme ponderer possible
        rule.and_func = np.fmin
        rule.or_func = np.fmax


    #system
    system = ctrl.ControlSystem(rules)
    sim = ctrl.ControlSystemSimulation(system)
    return sim