
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
        self.input_file = "input.txt"
        self.currentFrequency = 0
        self.lines = read_input(self.input_file)

    def calibrate(self, num: int):
        self.currentFrequency += num

    def compare(self):
        buf = int[len(self.lines)]

        


# put your inputs file next to this file!
lines = read_input('input.txt')
# solve the problem here!
f = Frequency()

for freq in lines:
    f.calibrate(freq) 

print(f.currentFrequency)

