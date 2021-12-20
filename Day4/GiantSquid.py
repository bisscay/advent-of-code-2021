#!/usr/bin/python3
"""GiantSquid.py
    Author: Bissallah Ekele - bAe
    Date: 19/12/2021
    Description: Beat squid at bingo.
"""

def check_boards(board_list, draw_set):
    # compare set against boar-list - contains?
    # move through board-list on diagonal, recursivelly
    # if not in set move to next diagonal
    # if in set, move on row
    # if row-cell not in set, move on column
    # if column-cell not in set, recurse to diagonal after row and column
    # for board in board_list:
    #     print(board)
    return 0   
    
def get_part_1(draw_list, board_list):
    """Play bingo

        Keyword argument:
        draw_list -- parameter description
        board_list -- parameter description

        Return:
        returned value
    """
    # Psuedocode
    # Place draw-list in set increamentally
    # compare set against boar-list - contains?
    
    draw_set = set()
    for draw in draw_list:
        print(draw_set)
        draw_set.add(draw)
        score = check_boards(board_list, draw_set)
        if score:
            return score

def get_part_2(input_list):
    pass

def main():
    test_input = "test-input"
    puzzle_input = "puzzle-input"

    file_name = test_input

    with open(file_name) as f:
        input_list = f.read().split("\n\n")

    input_list[0]= input_list[0].split(",")

    for index, board in enumerate(input_list[1:], start=1):
        input_list[index] = board.split("\n")
        for j, row in enumerate(input_list[index]):
            input_list[index][j] = row.split()

    print("Day_1 Part_1: " 
        + str(get_part_1(input_list[0], input_list[1:])) 
        + "\nPart_2: "
        + str(get_part_2(input_list)))

if __name__ == "__main__":
    main()