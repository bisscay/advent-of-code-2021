#!/usr/bin/python3
"""BinaryDiagnostic.py
    Author: Bissallah Ekele - bAe
    Date: 17/12/2021
    Description: Get consumed power from diagnostic report.
"""
# TODO: Consider class approach

def get_one_count(current_list):
    one_count = [0] * len(current_list[0])
    for diagnosis in current_list:
        for index, bit in enumerate(diagnosis):
            if bit == "1":
                one_count[index] += 1
    return one_count

def get_zero_count(current_list):
    zero_count = [0] * len(current_list[0])
    for diagnosis in current_list:
        for index, bit in enumerate(diagnosis):
            if bit == "0":
                zero_count[index] += 1
    return zero_count

def get_part_1(diagnosis_list):
    """Determine power consumed

        Keyword argument:
        diagnosis_list -- binary diagnosis string

        Return:
        product of gamma to epsilon rate
    """
    one_count = get_one_count(diagnosis_list)
    zero_count = get_zero_count(diagnosis_list)
    
    gamma = [None] * len(diagnosis_list[0])
    epsilon = [None] * len(diagnosis_list[0])
    for index in range(len(diagnosis_list[0])):
        if one_count[index] > zero_count[index]:
            gamma[index] = "1"
            epsilon[index] = "0"
        else:
            gamma[index] = "0"
            epsilon[index] = "1"
    
    gamma = "".join(gamma)
    epsilon = "".join(epsilon)

    return (int(gamma, 2) * int(epsilon, 2))

def get_oxygen_rate(current_list, index):
    filter_list = []
    one_count = get_one_count(current_list)
    zero_count = get_zero_count(current_list)

    if len(current_list) == 1:
        return current_list[0]
    
    for entry in current_list:
        if (((one_count[index] > zero_count[index]) and entry[index] == "1") or
            ((zero_count[index] > one_count[index]) and entry[index] == "0") or
            ((one_count[index] == zero_count[index]) and entry[index] == "1")):
            filter_list.append(entry)
    
    return get_oxygen_rate(filter_list, index+1)

def get_co2_rate(current_list, index):
    filter_list = []
    one_count = get_one_count(current_list)
    zero_count = get_zero_count(current_list)
    
    if len(current_list) == 1:
        return current_list[0]

    for entry in current_list:
        if (((one_count[index] < zero_count[index]) and entry[index] == "1") or
            ((zero_count[index] < one_count[index]) and entry[index] == "0") or
            ((one_count[index] == zero_count[index]) and entry[index] == "0")):
            filter_list.append(entry)
    
    return get_co2_rate(filter_list, index+1)

def get_part_2(diagnosis_list):
    """Determine life support rating

        Keyword argument:
        diagnosis_list -- binary diagnosis string

        Return:
        product of oxygen-generator to co2-scrubber rate
    """
    return (int("".join(get_oxygen_rate(diagnosis_list, 0)), 2)
            * int("".join(get_co2_rate(diagnosis_list, 0)), 2))

def main():
    test_input = "test-input"
    puzzle_input = "puzzle-input"

    file_name = puzzle_input

    with open(file_name) as f:
        diagnosis_list = f.read().splitlines()

    print("Day_1 Part_1: " 
        + str(get_part_1(diagnosis_list)) 
        + "\nPart_2: "
        + str(get_part_2(diagnosis_list)))

if __name__ == "__main__":
    main()