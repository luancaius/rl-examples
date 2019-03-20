import numpy as np
import matplotlib.pyplot as plt


class Env:
    def __init__(self, totalBandits, totalInteractions):
        self.totalInteractions = totalInteractions
        self.bandits = createBandits(totalBandits)

    def createBandits(total):


class Bandit:
    def __init__(self, prob):
        self.mean = 0
        self.prob = prob
