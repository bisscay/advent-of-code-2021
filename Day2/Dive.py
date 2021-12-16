#!/usr/bin/python3
"""SonarSweep.py
    Author: Bissallah Ekele - bAe
    Date: 17/12/2021
    Description: Depth measurement.
"""

def get_part_1():
    pass

def get_part_2():
    pass

def main():
    test_input = "test-input"
    puzzle_input = "puzzle-input"

    file_name = test_input

    with open(file_name) as f:
        input_list = f.read().splitlines()

    print("Day_1 Part_1: " 
        + str(get_part_1(input_list)) 
        + "\nPart_2: "
        + str(get_part_2(input_list)))

if __name__ == "__main__":
    main()