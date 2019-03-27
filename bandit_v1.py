import numpy as np
import matplotlib.pyplot as plt
import random
from random import randint


class Agent:
    def __init__(self, total, interactions, greedyness):
        self.env = {}
        self.total = total
        self.interactions = interactions
        self.greedyness = greedyness
        self.arrayReward = [
            [0 for i in range(total)] for j in range(interactions)]
        self.arrayMean = [[0 for i in range(total)]
                          for j in range(interactions)]
        self.currentMean = [0 for i in range(total)]
        self.index = 0

    def calculateMean(self, j):
        sumArray = 0
        totalIndex = 0
        for i in range(self.index+1):
            item = self.arrayReward[i][j]
            sumArray += item
            if item != 0:
                totalIndex += 1
        mean = sumArray/totalIndex
        self.arrayMean[self.index][j] = mean
        self.currentMean[j] = mean

    def act(self, i):
        self.index = i
        p = random.uniform(0, 1)
        if p > self.greedyness or i == 0:
            j = randint(0, self.total-1)
        else:
            j = np.argmax(self.currentMean)
        reward = self.env.pull(j)
        self.arrayReward[i][j] = reward
        self.calculateMean(j)
        # print(('explore' if p > self.greedyness else 'greedy'),
        #      ' ', i, ' ', j, ' ', self.currentMean)
        return reward

    def show(self):
        for i in range(self.interactions):
            print("reward", self.arrayReward[i])
        for i in range(self.interactions):
            print("mean", self.arrayMean[i])


class Bandit:
    def __init__(self, prob, i):
        self.id = i
        self.prob = prob

    def pull(self):
        randomNumber = random.uniform(0, 1)
        reward = self.prob*randomNumber*10
        return reward


class Env:
    def __init__(self, x, total):
        self.arrayReward = [[0 for i in range(x)] for j in range(total)]
        self.arrayMean = [[0 for i in range(x)] for j in range(total)]
        self.maxReward = [0 for i in range(x)]
        self.minReward = [0 for i in range(x)]
        self.index = 0
        self.x = x
        self.total = total

    def set_bandit(self, totalBandits):
        self.bandits = []
        self.create(totalBandits)
        self.totalBandits = totalBandits

    def create(self, total):
        for i in range(total):
            prob = random.uniform(0, 1)
            bandit = Bandit(prob, i)
            self.bandits.append(bandit)

    def pull(self, i):
        for n in range(self.totalBandits):
            self.arrayReward[self.index][n] = self.bandits[n].pull()
        reward = self.arrayReward[self.index][i]
        self.index += 1
        return reward

    def calculateMean(self):
        for j in range(self.x):
            sumArray = 0
            maxReward = 0
            minReward = 1000000
            for i in range(self.total):
                item = self.arrayReward[i][j]
                sumArray += item
                self.arrayMean[i][j] = sumArray/(i+1)
                if minReward > item:
                    minReward = item
                if maxReward < item:
                    maxReward = item

            self.minReward[j] = minReward
            self.maxReward[j] = maxReward

    def show(self):
        for i in range(self.total):
            print("env reward", self.arrayReward[i])
        for i in range(self.total):
            print("env mean", self.arrayMean[i])
        print("min ", self.minReward)
        print("max ", self.maxReward)


if __name__ == "__main__":
    total = 1000
    bandit = 10
    env = Env(bandit, total)
    env.set_bandit(bandit)
    agent = Agent(bandit, total, 0.1)
    agent.env = env
    for i in range(total):
        agent.act(i)
    agent.show()
    agent.env.calculateMean()
    agent.env.show()
