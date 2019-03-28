import numpy as np
import matplotlib.pyplot as plt
import random
from random import randint


class Agent:
    def __init__(self, env, totalItems, greedyness):
        self.env = env
        self.totalItems = totalItems
        self.greedyness = greedyness
        self.play = 0
        self.rewards = []
        self.sumReward = 0
        self.

    def play():
        pass

    def isGreedy():
        pass

    def explore():
        pass

    def exploit():
        pass


class Bandit:
    def __init__(self, prob, i):
        self.id = i
        self.prob = prob

    def action(self):
        randomNumber = random.uniform(0, 1)
        reward = self.prob*randomNumber*10
        return reward


class Env:
    def __init__(self, x, total):


if __name__ == "__main__":
    totalItems = 10
    totalPlays = 100
    epsilon = 0.1

    env = Env(totalItems)
    agent = Agent(Env, totalItems, epsilon)
    for i in range(totalPlays):
        agent.play()
    agent.show()
    env.show()
