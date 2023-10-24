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
# solve the problem here
# Part 1
def count_letter_occurrences():
    count_doubles = 0
    count_tripples = 0
    # Iterate through the input list
    for line in lines:
        letter_counts = {}

        for letter in line:
            if letter in letter_counts:
                letter_counts[letter] += 1            
            else:
                letter_counts[letter] = 1

        # Check if any letter appears exactly two or three times
        if 2 in letter_counts.values():
            count_doubles += 1
        if 3 in letter_counts.values():
            count_tripples += 1
    
    return count_doubles, count_tripples

def calc_checksum(num1, num2):
    return num1 * num2

double,tripple = count_letter_occurrences()

# Calculate the checksum by multiplying the counts
checksum = calc_checksum(double, tripple)
print(checksum)

# Part 2
# Function to find the common letters between two box IDs
def find_common_letters(line, line_):
    common_letter = []
    for letter, letter_ in zip(line, line_):
        if letter == letter_:
            common_letter.append(letter)

    if len(common_letter) == len(lines[0]) - 1:
        for letters in common_letter:
            print(letters, end="")
        return
    
# Iterate through the list to find the correct pair
i = 0
common_letters = []
while i < len(lines):
    j = i + 1
    while j < len(lines):
        find_common_letters(lines[i], lines[j])       
        j += 1
    i += 1