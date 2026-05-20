import numpy as np
import skfuzzy as fuzz

from skfuzzy import control as ctrl

# Variáveis fuzzy

sentiment_prob = ctrl.Antecedent(
    np.arange(0, 1.01, 0.01),
    'sentiment_prob'
)

wait_time = ctrl.Antecedent(
    np.arange(0, 61, 1),
    'wait_time'
)

satisfaction = ctrl.Consequent(
    np.arange(0, 101, 1),
    'satisfaction'
)

# Funções de pertinência

sentiment_prob['low'] = fuzz.trimf(
    sentiment_prob.universe,
    [0, 0, 0.5]
)

sentiment_prob['medium'] = fuzz.trimf(
    sentiment_prob.universe,
    [0.3, 0.5, 0.7]
)

sentiment_prob['high'] = fuzz.trimf(
    sentiment_prob.universe,
    [0.5, 1, 1]
)

wait_time['short'] = fuzz.trimf(
    wait_time.universe,
    [0, 0, 20]
)

wait_time['medium'] = fuzz.trimf(
    wait_time.universe,
    [10, 30, 50]
)

wait_time['long'] = fuzz.trimf(
    wait_time.universe,
    [40, 60, 60]
)

satisfaction['low'] = fuzz.trimf(
    satisfaction.universe,
    [0, 0, 40]
)

satisfaction['medium'] = fuzz.trimf(
    satisfaction.universe,
    [30, 50, 70]
)

satisfaction['high'] = fuzz.trimf(
    satisfaction.universe,
    [60, 100, 100]
)

# Regras fuzzy

rule1 = ctrl.Rule(
    sentiment_prob['high'] & wait_time['short'],
    satisfaction['high']
)

rule2 = ctrl.Rule(
    sentiment_prob['medium'] & wait_time['medium'],
    satisfaction['medium']
)

rule3 = ctrl.Rule(
    sentiment_prob['low'] | wait_time['long'],
    satisfaction['low']
)

# Sistema Mamdani

control_system = ctrl.ControlSystem([
    rule1,
    rule2,
    rule3
])

simulation = ctrl.ControlSystemSimulation(control_system)

def evaluate_satisfaction(probability, waiting):

    simulation.input['sentiment_prob'] = probability

    simulation.input['wait_time'] = waiting

    simulation.compute()

    return simulation.output['satisfaction']