import numpy as np
import matplotlib.pyplot as plt
import random


class MapAgent:
    def __init__(self, total):
        self.total = total
        self.map = [0]*total

    def getMaxIndex(self):
        i = np.argmax([b for b in self.map])
        return i

    def random(self):
        i = np.random.choice(self.total)
        return i


class Agent:
    def __init__(self):
        self.reward = 0
        self.env = {}
        self.actions = {}
        self.greedyness = 0.5
        self.map = {}

    def run(self, totalInteractions):
        totalBandits = self.env.totalBandits
        self.map = MapAgent(totalBandits)

        for i in range(totalInteractions):
            reward = self.act(i)
            self.reward += reward
        return self.reward

    def act(self, i):
        reward = 0
        p = random.uniform(0, 1)
        if p < self.greedyness:
            j = self.map.getMaxIndex()
        else:
            j = self.map.random()
        reward = self.env.pull(j)
        print((p < self.greedyness), " - ", j, " r=", reward)
        return reward

    def show(self):
        print('--------Agent--------')
        print(self.reward)


class Bandit:
    def __init__(self, prob, i):
        self.id = i
        self.sum = 0
        self.prob = prob
        self.N = 0
        self.mean = 0

    def pull(self):
        self.N += 1
        randomNumber = random.uniform(0, 1)
        reward = 0
        if self.prob > randomNumber:
            reward = 10
        self.sum += reward
        self.mean = self.sum/self.N
        return reward

    def show(self):
        print(self.id, ' mean = ', self.mean, ' N = ', self.N)


class Env:
    def set_bandit(self, totalBandits):
        self.bandits = []
        self.totalBandits = totalBandits
        self.create(totalBandits)
        self.currentBandit = self.bandits[0]
        self.index = 0

    def create(self, total):
        for i in range(total):
            prob = random.uniform(0, 1)
            bandit = Bandit(prob, i)
            self.bandits.append(bandit)

    def show(self):
        print('--------Env--------')
        for i in range(self.totalBandits):
            prob = self.bandits[i].prob
            print(i, ' ', prob)

    def pull(self, i):
        self.currentBandit = self.bandits[i]
        reward = self.currentBandit.pull()
        self.currentBandit.show()
        return reward

    def totalBandits(self):
        return self.totalBandits


if __name__ == "__main__":
    env = Env()
    env.set_bandit(10)
    env.show()
    total = 0
    for i in range(10):
        agent = Agent()
        agent.env = env
        reward = agent.run(1000)
        print(reward)
        total += reward
    print(total)
