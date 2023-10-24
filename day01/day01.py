from typing import List;
import os;

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

    def calibrate(self, num: int):
        self.currentFrequency += num


# put your inputs file next to this file!
lines = read_input('input.txt')

# Part 1
f = Frequency()
for freq in lines:
    f.calibrate(freq)

print("Part 1:", f.currentFrequency)

# Part 2
f_ = Frequency()
foundDuplicate = False
freqSet = set()

while foundDuplicate == False: 
    for freq in lines:
        f_.calibrate(freq)

        if f_.currentFrequency in freqSet:
            foundDuplicate = True
            break

        freqSet.add(f_.currentFrequency)

print("Part 2:", f_.currentFrequency)