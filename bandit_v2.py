import numpy as np
import random
from random import randint


class Agent:
    def __init__(self, env, totalItems, epsilon):
        self.env = env
        self.totalItems = totalItems
        self.epsilon = epsilon
        self.sumRewardTotal = 0
        self.sumReward = [0]*totalItems
        self.historyReward = [0]*totalItems
        self.meanReward = [0]*totalItems
        self.choice = [0]*totalItems
        self.exploreChoice = 0
        self.greedyChoice = 0

    def play(self):        
        choice = 0
        if self.isGreedy():
            choice = self.exploit()
        else:
            choice = self.explore()
        reward = self.env.action(choice)
        self.compute(choice, reward)
        return reward

    def isGreedy(self):
        p = random.uniform(0, 1)
        if p < self.epsilon:
            return True
        return False

    def explore(self):        
        choice = randint(0, self.totalItems-1)
        self.exploreChoice+=1
        return choice

    def exploit(self):
        choice = np.argmax(self.meanReward)
        self.greedyChoice+=1
        return choice

    def compute(self, choice, reward):
        self.sumRewardTotal += reward
        self.sumReward[choice]+= reward
        self.choice[choice]+=1
        self.meanReward[choice] =self.sumReward[choice]/self.choice[choice]
          

    def show(self):
        print('E= ', self.epsilon,' sum ',self.sumRewardTotal)
        print('choice ',self.choice)
        print('Explore ', self.exploreChoice,' vs Greedy ', self.greedyChoice)

class Bandit:
    def __init__(self, prob, i):
        self.id = i
        self.prob = prob

    def action(self):
        randomNumber = random.uniform(0, 1)
        reward = self.prob*randomNumber*10
        return reward

class Env:
    def __init__(self, totalItems):
        self.totalItems = totalItems
        self.items = self.createItems(self.totalItems)        

    def action(self, i):
        return self.items[i].action()

    def createItems(self, totalItems):
        bandits = []
        for i in range(totalItems):
            prob = random.uniform(0, 1)
            bandit = Bandit(prob, i)
            bandits.append(bandit)

        return bandits

    def show(self):
        probArray = [i.prob for i in self.items]
        print('prob ', probArray)
        print('best choice = ',np.argmax(probArray), ' = ',probArray[np.argmax(probArray)])        

if __name__ == "__main__":
    totalItems = 100
    totalPlays = 10000
    epsilon = 0.1

    env = Env(totalItems)
    agents = [  Agent(env, totalItems, epsilon*1),
                Agent(env, totalItems, epsilon*2),
                Agent(env, totalItems, epsilon*3),
                Agent(env, totalItems, epsilon*4),
                Agent(env, totalItems, epsilon*5),
                Agent(env, totalItems, epsilon*6),
                Agent(env, totalItems, epsilon*7),
                Agent(env, totalItems, epsilon*8),
                Agent(env, totalItems, epsilon*9),
                Agent(env, totalItems, epsilon*9.2),
                Agent(env, totalItems, epsilon*9.5),
                Agent(env, totalItems, epsilon*9.9)] 

    for i in range(totalPlays):
        for agent in agents:
            agent.play()
    for agent in sorted(agents, key=lambda x: x.sumRewardTotal, reverse=True):
        agent.show()
    env.show()
