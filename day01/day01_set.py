
from typing import List;
import os;
import time;
import matplotlib.pyplot as plt

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



inputs = read_input("input.txt")
known = set();
i = 0
current = 0;
times = []
n = []
start = time.time();
while True:
    current += inputs[i % len(inputs)]
    i += 1
    if current in known:
        break
    known.add(current)

    if i % 50:
        n.append(i)
        times.append(time.time()-start)


print(current)
# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data
ax.plot(n, times);
# Show the plot
plt.savefig('runtime.png')
