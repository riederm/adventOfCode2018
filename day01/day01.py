
from typing import List;
import os;
import time;
import matplotlib.pyplot as plt

mode = 0

class BinaryTree:
    def __init__(self):
        self.data = [];
    
    #returns the index of the element, or the index where it would belong
    def _binary_search(self, element, start, end):
        if start == end:
            return start
        else:
            mid = (start + end) // 2    #floor division
            if self.data[mid] == element:
                return mid
            elif self.data[mid] > element:
                return self._binary_search(element, start, mid)
            else:
                return self._binary_search(element, mid + 1, end)

    def add(self, element):
        if mode == 0:
            self.data.append(element)
            self.data.sort()
        else :
            idx = self._binary_search(element, 0, len(self.data))
            self.data.insert(idx, element)
              

    def __contains__(self, element):
        idx = self._binary_search(element, 0, len(self.data))
        return idx > 0 and idx < len(self.data) and self.data[idx] == element



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
        if mode == 2:
            self.known = set()
        elif mode == 3:
            self.known = []
        else:
            self.known = BinaryTree();
    

    def calibration(self, num: int):
        self.current_frequency  += num
        dup = self.current_frequency in self.known
        if mode == 3:
            self.known.append(self.current_frequency)
        else:
            self.known.add(self.current_frequency)
        return dup

f = Frequency()
inputs = read_input('input.txt')

for freq in inputs:
    f.calibration(freq)

print("The sum of all frequencies is ", f.current_frequency)

f = Frequency(); i = 0; start = time.time();
y1 = []; x = [];
y2 = []; 
y3 = []; 
y4 = []; 

mode = 0
while(not f.calibration(inputs[i % len(inputs)])):
    i += 1
    if i % 100 == 0:
        y1.append((time.time() - start))
print("1/4 done")

mode = 1
f = Frequency(); i = 0; start = time.time();
while(not f.calibration(inputs[i % len(inputs)])):
    i += 1
    if i % 100 == 0:
        y2.append((time.time() - start))
        x.append(i)
print("2/4 done")

mode = 2
f = Frequency(); i = 0; start = time.time();
while(not f.calibration(inputs[i % len(inputs)])):
    i += 1
    if i % 100 == 0:
        y3.append((time.time() - start))


print("3/4 done")


mode = 3
f = Frequency(); i = 0; start = time.time();
while(not f.calibration(inputs[i % len(inputs)])):
    i += 1
    if i % 100 == 0:
        y4.append((time.time() - start))


print("4/4 done")

print("The first repeating frequency is ", f.current_frequency)

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, y1);
ax.plot(x, y2);
ax.plot(x, y3);
ax.plot(x, y4);

# Customize the plot
ax.set_xlabel('n')
ax.set_ylabel('s')

# Show the plot
plt.show()
