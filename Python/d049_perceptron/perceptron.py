import random
import math

class Perceptron():
    def __init__(self, data_size, learning_rate):
        self.weights = [random.uniform(-1, 1) for _ in range(data_size)]
        self.learning_rate = learning_rate
    
    def feedforward(self, data):
        guess = sum(data[i] * self.weights[i] for i in range(len(self.weights)))
        return 1 if guess > 0 else 0
    
    def train(self, data, answer):
        guess = self.feedforward(data)
        error = math.sqrt(guess**2 - answer**2)

        self.weights = [
            self.weights[i] + (data[i] * error * self.learning_rate)
            for i in range(len(self.weights))
        ]

        