#!/usr/bin/python3
"""BinaryDiagnostic.py
    Author: Bissallah Ekele - bAe
    Date: 17/12/2021
    Description: Get consumed power from diagnostic report.
"""

def get_part_1(diagnosis_list):
    """Determine power consumed

        Keyword argument:
        input_list -- parameter description

        Return:
        product of gamma to epsilon rate
    """
    one_count = [0] * len(diagnosis_list[0])
    zero_count = [0] * len(diagnosis_list[0])
    for diagnosis in diagnosis_list:
        for index, bit in enumerate(diagnosis):
            if bit == "0":
                zero_count[index] += 1
            if bit == "1":
                one_count[index] += 1
    
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

def get_part_2(input_list):
    pass

def main():
    test_input = "test-input"
    puzzle_input = "puzzle-input"

    file_name = test_input

    with open(file_name) as f:
        diagnosis_list = f.read().splitlines()

    print("Day_1 Part_1: " 
        + str(get_part_1(diagnosis_list)) 
        + "\nPart_2: "
        + str(get_part_2(diagnosis_list)))

if __name__ == "__main__":
    main()