import datetime
import example_plot
from binsearch import bin_search


# Open the file input.txt in read mode
with open('input.txt', 'r') as file:
    # Read the file content
    data = file.read()

# Split the file content by new lines into an array
lines = data.split('\n')

# Print the length of the array
print("read " + str(len(lines)) + " lines")

frequency = 0
last_seen = []
frequency_found = False
currentTime = datetime.datetime.now()
n1 = []
t1 = []

#put your solution here ... 
while not frequency_found:
    print("lastseen = " + str(len(last_seen)))
    for line in lines:

        if len(last_seen) % 10000 == 0:
            t1.append((datetime.datetime.now() - currentTime).total_seconds())
            n1.append(len(last_seen))

        curr = int(line)
        frequency += curr
        if frequency in last_seen:
            frequency_found = True
            print(f"f = {frequency} was already seen!")
            break
        else:
            last_seen.append(frequency)

frequency = 0
last_seen = []
frequency_found = False
currentTime = datetime.datetime.now()
n2 = []
t2 = []

while not frequency_found:
    print("lastseen = " + str(len(last_seen)))
    for line in lines:

        if len(last_seen) % 10000 == 0:
            t2.append((datetime.datetime.now() - currentTime).total_seconds())
            n2.append(len(last_seen))

        curr = int(line)
        frequency += curr

        if bin_search(last_seen, frequency):
            frequency_found = True
            print(f"f = {frequency} was already seen!")
            break
        else:
            last_seen.append(frequency)
            last_seen.sort()

frequency = 0
last_seen = set()
frequency_found = False
currentTime = datetime.datetime.now()
n3 = []
t3 = []

while not frequency_found:
    print("lastseen = " + str(len(last_seen)))
    for line in lines:

        if len(last_seen) % 100 == 0:
            t3.append((datetime.datetime.now() - currentTime).total_seconds())
            n3.append(len(last_seen))

        curr = int(line)
        frequency += curr

        if frequency in last_seen:
            frequency_found = True
            print(f"f = {frequency} was already seen!")
            break
        else:
            last_seen.add(frequency)


example_plot.plot(n1, t1, n2, t2, n3, t3, filename="n-t-Diagram.png")
