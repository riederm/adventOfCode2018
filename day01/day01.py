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
        self.currentFrequency_1 = 0
        self.currentFrequency_2 = 0
        self.uniqueFrequencies = set()

    def calibrate_task1(self, num):
        self.currentFrequency_1 += num

    def calibrate_task2(self, num):
        self.currentFrequency_2 += num
        if self.currentFrequency_2 in self.uniqueFrequencies:
            return True
        self.uniqueFrequencies.add(self.currentFrequency_2)
        return None

# put your inputs file next to this file!
lines = read_input('input1.txt')
# solve the problem here!

f = Frequency()

for line in lines:
    f.calibrate_task1(line)
print(f"Task 1: frq {f.currentFrequency_1}")


retVal = None
while retVal is None:
    for line in lines:
        retVal = f.calibrate_task2(line)
        if retVal is True:
            break        
print(f"Task 2: Current is {f.currentFrequency_2}, uniqueFrqs: {len(f.uniqueFrequencies)}")