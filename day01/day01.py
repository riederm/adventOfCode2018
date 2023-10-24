
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
        self.currentFrequency = 0
        self.uniqueFrequencies : List[int] = []

    def calibrate(self, num: int) -> bool:
        self.currentFrequency += num
        for frq in self.uniqueFrequencies:
            if frq ==  self.currentFrequency:
                return True
        #no match found, add frequency to list
        self.uniqueFrequencies.append(self.currentFrequency)
        #print(f"Pos: {len(self.uniqueFrequencies) + 1} Appended {self.currentFrequency}")
        return False

# put your inputs file next to this file!
lines = read_input('input1.txt')
# solve the problem here!

f = Frequency()

retVal = False
while False == retVal:
    for line in lines:
        retVal = f.calibrate(line)        
    print(f"Current is {f.currentFrequency}")

print(f.currentFrequency)

