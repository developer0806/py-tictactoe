import pygame


def updated_highlighted_cell(key):
    global highlighted_cell, selected_cell
    highlighted_cell_x = highlighted_cell[0]
    highlighted_cell_y = highlighted_cell[1]
    if key == "return":
        selected_cell = highlighted_cell
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
    print("highlighted_cell is [" + str(highlighted_cell) + "]")


def main():
    initialize_game()
    count = 20
    redraw()

    while who_won == "none":
        event = pygame.event.poll()
        if event.type == pygame.KEYUP:
            key = pygame.key.name(event.key)
            print("Key is [" + key + "]")
            updated_highlighted_cell(key)
            count -= 1
            if count == 0:
                break
            redraw()
    pygame.time.delay(2000)


def initialize_game():
    pygame.init()


def draw_matrix():
    pygame.draw.line(window, color, (cellWidth, 0), (cellWidth, width - 1))
    pygame.draw.line(window, color, (cellWidth * 2, 0), (cellWidth * 2, width - 1))
    pygame.draw.line(window, color, (0, cellWidth), ((width - 1), cellWidth))
    pygame.draw.line(window, color, (0, cellWidth * 2), (width - 1, cellWidth * 2))


def draw_highlighted_cell(param):
    start = get_start_cell(param)
    end = get_end_cell(param)
    pygame.draw.rect(window, (255, 255, 0), (start, (cellWidth, cellWidth)), 2)


def draw_char_in_cell(param, char):
    pygame.display.set_caption("This is text")
    font = pygame.font.Font('freesansbold.ttf', 80)
    text = font.render(char, True, color, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = get_center(param)
    window.blit(text, text_rect)


def get_center(param):
    start = get_start_cell(param)
    end = get_end_cell(param)
    # print("X = [(" + str(start) + ")]  Y = [" + str(end) + "]")
    return (((end[1] - start[1]) // 2) + (param[1] * cellWidth),
            ((end[0] - start[0]) // 2) + (param[0] * cellWidth))


def get_end_cell(param):
    return ((param[1] * cellWidth) + cellWidth), ((param[0] * cellWidth) + cellWidth)


def get_start_cell(param):
    return (param[1] * cellWidth), (param[0] * cellWidth)


def redraw():
    draw_border()
    draw_matrix()
    draw_highlighted_cell(highlighted_cell)
    draw_char_in_cell(selected_cell, "X")
    pygame.display.update()


def draw_border():
    pygame.draw.rect(window, color, (box_start_pos, ((width - 2), (width - 2))), 2)


box_start_pos = (0, 0)
who_won = "none"
highlighted_cell = (1, 1)
selected_cell = (-1, -1)
width = 300
cellWidth = int(width / 3)
color = (255, 255, 255)
window = pygame.display.set_mode((width, width))
main()
