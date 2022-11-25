import numpy.random as rd
import matplotlib.pyplot as plt


class Picker:
    def __init__(self, choices: list, pick_number=2000):
        self.choices = choices

        self.N = pick_number
        self.dictionary = {}
        self.generate_dictionnary()

    def generate_dictionnary(self):
        for choice in self.choices:
            self.dictionary[choice] = 0

    def pick(self):
        for i in range(self.N):
            choice = rd.choice(self.choices)
            self.dictionary[choice] += 1

        max_count = 0
        final_choice = ''
        for key, value in self.dictionary.items():
            max_count = max(value, max_count)
            if max_count == value:
                final_choice = key

        return final_choice

    def display_stats(self):
        values = self.dictionary.values()
        plt.plot(self.choices, values)
        plt.show()
