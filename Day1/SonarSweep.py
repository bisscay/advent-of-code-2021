#!/usr/bin/python3
"""SonarSweep.py
    Author: Bissallah Ekele - bAe
    Date: 16/12/2021
    Description: Depth measurement.
"""

def get_part_1(depth_list):
    """Count increasing depths

        Keyword argument:
        depth_list -- list of measured depths

        Return:
        increased depth count
    """
    count = 0
    for index in range(len(depth_list)-1):
        if int(depth_list[index]) < int(depth_list[index+1]):
            count += 1
    return count

def get_part_2(depth_list):
    pass

def main():
    test_input = "test-input"
    puzzle_input = "puzzle-input"

    file_name = test_input

    with open(file_name) as f:
        depth_list = f.read().splitlines()

    print("Day_1 Part_1: " 
        + str(get_part_1(depth_list)) 
        + "\nPart_2: "
        + str(get_part_2(depth_list)))

if __name__ == "__main__":
    main()