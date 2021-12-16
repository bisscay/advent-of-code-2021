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
        if depth_list[index] < depth_list[index+1]:
            count += 1
    return count

def compute_sliding_window(depth_list):
    """Derive sliding window sums

        Keyword argument:
        depth_list -- list of measured depths

        Return:
        list of sliding window sums
    """
    window_list =  [None] * (len(depth_list)-2)
    for index in range(2, len(depth_list)):
        window_list[index-2] = (depth_list[index-2]
                                + depth_list[index-1]
                                + depth_list[index])
    return window_list

def get_part_2(depth_list):
    """Count increasing depths on sliding window sums

        Keyword argument:
        depth_list -- list of measured depths

        Return:
        increased depth count
    """
    return get_part_1(compute_sliding_window(depth_list))

def main():
    test_input = "test-input"
    puzzle_input = "puzzle-input"

    file_name = puzzle_input

    with open(file_name) as f:
        depth_list = f.read().splitlines()

    for index, character in enumerate(depth_list):
        depth_list[index] = int(character)

    print("Day_1 Part_1: " 
        + str(get_part_1(depth_list)) 
        + "\nPart_2: "
        + str(get_part_2(depth_list)))

if __name__ == "__main__":
    main()