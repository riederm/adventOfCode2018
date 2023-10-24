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
        self.uniqueFrequencies = set()

    def calibrate(self, num):
        self.currentFrequency += num
        if self.currentFrequency in self.uniqueFrequencies:
            return True
        self.uniqueFrequencies.add(self.currentFrequency)
        #print(f"Pos: {len(self.uniqueFrequencies) + 1} Appended {self.currentFrequency}")
        return None

# put your inputs file next to this file!
lines = read_input('input1.txt')
# solve the problem here!

f = Frequency()

retVal = None
while retVal is None:
    for line in lines:
        retVal = f.calibrate(line)
        if retVal is True:
            break        
    print(f"Current is {f.currentFrequency}, uniqueFrqs: {len(f.uniqueFrequencies)}")

print(f.currentFrequency)
