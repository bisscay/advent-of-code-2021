#!/usr/bin/python3
"""SonarSweep.py
    Author: Bissallah Ekele - bAe
    Date: 17/12/2021
    Description: Position measurement.
"""

def get_part_1(course_list):
    """Multiply depth by horizontal position

        Keyword argument:
        course_list -- list of planned course

        Return:
        Product of depth by horizontal position
    """
    forward = 0
    depth = 0
    for course in course_list:
        if course[0] == "f":
            forward += int(course[8:])
        if course[0] == "d":
            depth += int(course[5:])
        if course[0] == "u":
            depth -= int(course[3:])
    return forward * depth

def get_part_2(course_list):
    pass

def main():
    test_input = "test-input"
    puzzle_input = "puzzle-input"

    file_name = puzzle_input

    with open(file_name) as f:
        course_list = f.read().splitlines()

    print("Day_1 Part_1: " 
        + str(get_part_1(course_list)) 
        + "\nPart_2: "
        + str(get_part_2(course_list)))

if __name__ == "__main__":
    main()