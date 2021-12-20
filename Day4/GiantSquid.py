#!/usr/bin/python3
"""GiantSquid.py
    Author: Bissallah Ekele - bAe
    Date: 19/12/2021
    Description: Beat squid at bingo.
"""

def get_unmarked_sum(board, draw_set):
    sum = 0
    for row in board:
        for cell in row:
            if cell not in draw_set:
                sum += int(cell)
    return sum

def get_row_sum(row, current_j, draw_set):
    sum = 0 # No need computing
    for j in range(len(row)):
        if row[j] in draw_set:
            sum += int(row[j])
        else:
            return (0, current_j + max(1, j-current_j))
    return (sum, len(row)-1)

def get_column_sum(board, current_i, j, draw_set):
    sum = 0 # No need computing
    for i in range(len(board)):
        if board[i][j] in draw_set:
            sum += int(board[i][j])
        else:            
            return (0, current_i + max(i-current_i, 1))
    return (sum, len(board)-1)

def check_board(i, j, board, draw_set): # Consider passing board-cell itself
    # move through boards on diagonal, recursivelly
    # if not in set move to next diagonal
    # if in set, move on row
    # if row-cell not in set, move on column
    # if column-cell not in set, recurse to diagonal after row and column
    if i >= len(board) or j >= len(board):
        return 0

    if board[i][j] not in draw_set:
        return check_board(i+1, j+1, board, draw_set)
    else:
        sum_row, next_j = get_row_sum(board[i], j, draw_set)
        if sum_row:
            return get_unmarked_sum(board, draw_set)
        sum_column, next_i = get_column_sum(board, i, j, draw_set)
        if sum_column:
            return get_unmarked_sum(board, draw_set)
        return check_board(next_i, next_j, board, draw_set)

def get_score(board_list, draw_set):
    # move through boards on diagonal, recursivelly
    # compare set against board-list - contains?
    unmarked_sum = 0
    for board in board_list:
        unmarked_sum = check_board(0, 0, board, draw_set)
        if unmarked_sum:
            return unmarked_sum
    return unmarked_sum
       
    
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
    # compare set against board-list - contains?
    score = 0
    draw_set = set()
    for draw in draw_list:
        draw_set.add(draw)
        score = get_score(board_list, draw_set)
        if score:
            return score * int(draw) # Multiply by draw here
    return score * int(draw)

def get_part_2(draw_list, board_list):
    pass

def main():
    test_input = "test-input"
    puzzle_input = "puzzle-input"

    file_name = puzzle_input#test_input

    with open(file_name) as f:
        input_list = f.read().split("\n\n")

    input_list[0]= input_list[0].split(",")

    for index, board in enumerate(input_list[1:], start=1):
        input_list[index] = board.split("\n")
        for j, row in enumerate(input_list[index]):
            input_list[index][j] = row.split()

    print("Day_4 Part_1: " 
        + str(get_part_1(input_list[0], input_list[1:])) 
        + "\nPart_2: "
        + str(get_part_2(input_list[0], input_list[1:])))

if __name__ == "__main__":
    main()