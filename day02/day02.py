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


lines = read_input('input.txt')
cnt_two = 0
cnt_three = 0

flag_two = False
flag_three = False

for idn in lines:
    char_dict = {}
    for char in idn:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    if 2 in char_dict.values():
        cnt_two += 1
    if 3 in char_dict.values():
        cnt_three += 1

print("checksum: ", cnt_two * cnt_three)