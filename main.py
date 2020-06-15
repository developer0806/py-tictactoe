import pygame
from board import *


def get_char_for_move():
    if (move_count % 2) == 0:
        return "X"
    else:
        return "O"


def get_num_for_move():
    if (move_count % 2) == 0:
        return 0
    else:
        return 1


def updated_highlighted_cell(key):
    global highlighted_cell, selected_cell
    highlighted_cell_x = highlighted_cell[0]
    highlighted_cell_y = highlighted_cell[1]

    if key == "return":
        determine_winner()
    if key == "space":
        on_key_event_space()
    if key == "up":
        if highlighted_cell_x > 0:
            highlighted_cell_x -= 1
    if key == "down":
        if highlighted_cell_x < 2:
            highlighted_cell_x += 1
    if key == "left":
        if highlighted_cell_y > 0:
            highlighted_cell_y -= 1
    if key == "right":
        if highlighted_cell_y < 2:
            highlighted_cell_y += 1
    highlighted_cell = (highlighted_cell_x, highlighted_cell_y)
    # print("highlighted_cell is [" + str(highlighted_cell) + "]")
    # print_board()


def on_key_event_space():
    global selected_cell, move_count
    try:
        # print("cell [" + str(get_num_for_move()) + "] selected_cell [" + format(selected_cell) + "]")
        selected_cell = highlighted_cell
        assign_cell(get_num_for_move(), selected_cell)
        move_count += 1
    except Exception as e:
        print("Cell is already used! Error [" + format(e) + "]")


def is_winner_in_rows():
    global who_won
    rows = len(board)
    for i in range(rows):
        # print("Row [" + str(i) + "] value [" + format(board[i]) + "]")
        if is_winner_in_array(board[i]):
            return True
    return False


def is_winner_in_columns():
    columns = len(board[0])
    rows = len(board)
    for j in range(columns):
        column = array("b", [])
        for i in range(rows):
            column.insert(i, board[i][j])
        # print("column [" + str(j) + "] value [" + format(column) + "]")
        if is_winner_in_array(column):
            return True
    return False


def is_winner_in_diagonals():
    diagonal_1 = array("b", [board[0][0], board[1][1], board[2][2]])
    # print("Diagonal_1 [" + str(diagonal_1) + "] ")
    if not is_winner_in_array(diagonal_1):
        diagonal_2 = array("b", [board[0][2], board[1][1], board[2][0]])
        # print("Diagonal_2 [" + str(diagonal_2) + "] ")
        return is_winner_in_array(diagonal_2)
    else:
        return True


def is_winner_in_array(my_array):
    global who_won
    if my_array == array("b", [0, 0, 0]):
        who_won = "O"
        return True
    if my_array == array("b", [1, 1, 1]):
        who_won = "X"
        return True


def determine_winner():
    if not is_winner_in_rows():
        if not is_winner_in_columns():
            is_winner_in_diagonals()


def main():
    initialize_game()
    redraw()

    while who_won == "none":
        event = pygame.event.poll()
        handle_event(event)
        if are_all_cells_filled():
            print("All cells are filled!")
            break
    print("Game Over. \n who won [" + who_won + "]")


def handle_event(event):
    if event.type == pygame.KEYUP:
        key = pygame.key.name(event.key)
        # print("Key is [" + key + "]")
        updated_highlighted_cell(key)
        redraw()
    determine_winner()


def initialize_game():
    pygame.init()
    initialize_board()


def draw_matrix():
    pygame.draw.line(window, color, (cellWidth, 0), (cellWidth, width - 1))
    pygame.draw.line(window, color, (cellWidth * 2, 0), (cellWidth * 2, width - 1))
    pygame.draw.line(window, color, (0, cellWidth), ((width - 1), cellWidth))
    pygame.draw.line(window, color, (0, cellWidth * 2), (width - 1, cellWidth * 2))


def draw_highlighted_cell(param):
    start = get_start_cell(param)
    pygame.draw.rect(window, (255, 255, 0), (start, (cellWidth, cellWidth)), 2)


def draw_cell_border(cell_location):
    start = get_start_cell(cell_location)
    pygame.draw.rect(window, get_cell_color(cell_location), (start, (cellWidth, cellWidth)), 2)


def get_cell_color(cell_location):
    cell_color = color
    if cell_location == highlighted_cell:
        cell_color = (255, 255, 0)
    return cell_color


def translate_content(content):
    if content == -1:
        return " "
    if content == 1:
        return "X"
    if content == 0:
        return "O"


def draw_current_game_state():
    rows = len(board)
    columns = len(board[0])
    for i in range(rows):
        for j in range(columns):
            draw_cell((i, j), translate_content(board[i][j]))


def draw_cell_content(cell_location, content):
    font = pygame.font.Font('freesansbold.ttf', 80)
    text = font.render(content, True, color, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = get_center(cell_location)
    window.blit(text, text_rect)


def draw_cell(cell_location, content):
    draw_cell_border(cell_location)
    draw_cell_content(cell_location, content)


def get_center(param):
    start = get_start_cell(param)
    end = get_end_cell(param)
    return (((end[1] - start[1]) // 2) + (param[1] * cellWidth),
            ((end[0] - start[0]) // 2) + (param[0] * cellWidth))


def get_end_cell(param):
    return ((param[1] * cellWidth) + cellWidth), ((param[0] * cellWidth) + cellWidth)


def get_start_cell(param):
    return (param[1] * cellWidth), (param[0] * cellWidth)


def redraw():
    pygame.display.set_caption("Tic Tac Toe")
    draw_current_game_state()
    pygame.display.update()


move_count = 1
box_start_pos = (0, 0)
who_won = "none"
highlighted_cell = (1, 1)
selected_cell = (-1, -1)
width = 300
cellWidth = int(width / 3)
color = (255, 255, 255)
window = pygame.display.set_mode((width, width))
main()
