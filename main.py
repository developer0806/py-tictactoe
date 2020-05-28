import pygame
import logging


def main():
    global window, width, color, cellWidth, box_start_pos
    pygame.init()
    box_start_pos = (1, 1)
    width = 300
    cellWidth = int(width / 3)
    color = (255, 255, 255)
    window = pygame.display.set_mode((width, width))
    redraw()
    pygame.time.delay(5000)


def draw_matrix():
    pygame.draw.line(window, color, (cellWidth, 0), (cellWidth, width - 1))
    pygame.draw.line(window, color, (cellWidth * 2, 0), (cellWidth * 2, width - 1))
    pygame.draw.line(window, color, (0, cellWidth), ((width - 1), cellWidth))
    pygame.draw.line(window, color, (0, cellWidth * 2), (width - 1, cellWidth * 2))


def drawX_in_cell(param):
    pygame.display.set_caption("This is text")
    font = pygame.font.Font('freesansbold.ttf', 80)
    text = font.render('X', True, color, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (((param[0] * cellWidth) + cellWidth) // 2, ((param[1] * cellWidth) + cellWidth) // 2)
    window.blit(text, textRect)



def redraw():
    draw_border()
    draw_matrix()
    drawX_in_cell((0, 0))
    pygame.display.update()


def draw_border():
    logging.debug("width [" + str(width) + "] cell_width [" + str(cellWidth) + "]")
    pygame.draw.rect(window, color, (box_start_pos, ((width - 2), (width - 2))), 2)


main()
