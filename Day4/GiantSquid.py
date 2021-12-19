#!/usr/bin/python3
"""GiantSquid.py
    Author: Bissallah Ekele - bAe
    Date: 19/12/2021
    Description: Beat squid at bingo.
"""

def get_part_1(draw_list, board_list):
    """Function description

        Keyword argument:
        input_list -- parameter description

        Return:
        returned value
    """
    print(draw_list)
    print(board_list)

def get_part_2(input_list):
    pass

def main():
    test_input = "test-input"
    puzzle_input = "puzzle-input"

    file_name = test_input

    with open(file_name) as f:
        input_list = f.read().split("\n\n")

    print("Day_1 Part_1: " 
        + str(get_part_1(input_list[0], input_list[1:])) 
        + "\nPart_2: "
        + str(get_part_2(input_list)))

if __name__ == "__main__":
    main()