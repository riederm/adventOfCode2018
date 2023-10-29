
from typing import List;
import os;
import time;

def read_input(file_name):
    current_path = os.path.dirname(__file__)
    lines : List[int] = []
    try:
        with open(os.path.join(current_path, file_name), 'r') as file:
            for line in file:
                lines.append(int(line.strip()))  
    except Exception as e:
        print(f"An error occurred: {e}")
    return lines


class Frequency:
    def __init__(self):
        self.current_frequency = 0
        self.first_rep = None

    def calibration(self, num: int):
        self.current_frequency  += num

    def detect_first_rep(self, inputs):
        freq_dict = {}
        self.current_frequency = 0

        while (1):
            for freq in inputs:
                self.calibration(freq)
                if self.current_frequency in freq_dict:
                    self.first_rep = self.current_frequency
                    return
                else:
                    freq_dict[self.current_frequency] = None


f = Frequency()
inputs = read_input('input.txt')

for freq in inputs:
    f.calibration(freq)

print("The sum of all frequencies is ", f.current_frequency)

f.detect_first_rep(inputs)

print("The first repeating frequency is ", f.first_rep)