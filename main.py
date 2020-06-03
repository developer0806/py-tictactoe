import pygame
import logging


def main():
    global window, width, color, cellWidth, box_start_pos
    initialize_game()
    redraw()
    pygame.time.delay(5000)


def initialize_game():
    global box_start_pos, width, cellWidth, color, window
    pygame.init()
    box_start_pos = (1, 1)
    width = 300
    cellWidth = int(width / 3)
    color = (255, 255, 255)
    window = pygame.display.set_mode((width, width))


def draw_matrix():
    pygame.draw.line(window, color, (cellWidth, 0), (cellWidth, width - 1))
    pygame.draw.line(window, color, (cellWidth * 2, 0), (cellWidth * 2, width - 1))
    pygame.draw.line(window, color, (0, cellWidth), ((width - 1), cellWidth))
    pygame.draw.line(window, color, (0, cellWidth * 2), (width - 1, cellWidth * 2))


def drawX_in_cell(param):
    pygame.display.set_caption("This is text")
    font = pygame.font.Font('freesansbold.ttf', 80)
    text = font.render('O', True, color, (0, 0, 0))
    textRect = text.get_rect()
    start = get_start_cell(param)
    end = get_end_cell(param)
    print("X = [(" + str(start) + ")]  Y = [" + str(end) + "]")
    textRect.center = (((end[0] - start[0]) // 2) + (param[0] * cellWidth),
                       ((end[1] - start[1]) // 2) + (param[1] * cellWidth))
    print("centre is [" + str(textRect.center) + "]")
    window.blit(text, textRect)


def get_end_cell(param):
    return ((param[0] * cellWidth) + cellWidth), ((param[1] * cellWidth) + cellWidth)


def get_start_cell(param):
    return (param[0] * cellWidth), (param[1] * cellWidth)


def redraw():
    draw_border()
    draw_matrix()
    drawX_in_cell((1, 1))
    pygame.display.update()


def draw_border():
    logging.debug("width [" + str(width) + "] cell_width [" + str(cellWidth) + "]")
    pygame.draw.rect(window, color, (box_start_pos, ((width - 2), (width - 2))), 2)


main()
