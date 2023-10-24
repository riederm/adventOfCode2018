from typing import List;
import os;

def read_input(file_name):
    current_path = os.path.dirname(__file__)
    lines = []
    try:
        with open(os.path.join(current_path, file_name), 'r') as file:
            for line in file:
                lines.append(line.strip())  # Remove any leading or trailing whitespace
    except Exception as e:
        print(f"An error occurred: {e}")
    return lines


lines = read_input('input1.txt')
# solve the problem here!

count_2_same = 0
count_3_same = 0

for line in lines:
    char_count = {}
    
    for char in line:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    if 2 in char_count.values():
        count_2_same += 1
    if 3 in char_count.values():
        count_3_same += 1

result = count_2_same * count_3_same

print(f"Result: {result}")
