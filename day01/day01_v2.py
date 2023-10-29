
from typing import List;
import os;
import time;
import numpy as np

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

def calibration(inputs):
    sums = np.zeros(len(inputs))
    i = 0
    a = 0
    csums = np.cumsum(inputs)
    for line in inputs:
        a += line
        sums[i] = a
        if (a != csums[i]):
            print("ERROR")
        i += 1
    
    return sums



def freq_calculations(inputs):
    cumlsum_inputs = calibration(inputs)# np.cumsum(inputs)
    print("The sum of all frequencies is ", cumlsum_inputs[-1])
    cumlsum_dict = {}
    i = 0
    while True:

        
        for line in cumlsum_inputs:
            
            if line in cumlsum_dict:
                print("The first repeating frequency is ", line)
                print(cumlsum_dict[line])
                return
            else:
                cumlsum_dict[line] = i
            i += 1
        cumlsum_inputs += cumlsum_inputs[-1]
        


inputs = read_input('input.txt')
freq_calculations(inputs)