import colours
import numpy as np
import pygame


def update(screen, cells, size, with_progress=False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]), dtype=int)

    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row - 1: row + 2, col - 1: col + 2]) - cells[row, col]
        colour = colours.ALIVE_NEXT if cells[row, col] > 0 else colours.BG
        if cells[row, col] == 1:
            if alive < 2 or alive > 3:
                if with_progress:
                    colour = colours.DIE_NEXT
            elif 2 <= alive <= 3:
                updated_cells[row, col] = 1
                if with_progress:
                    colour = colours.ALIVE_NEXT
        else:
            if alive == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    colour = colours.ALIVE_NEXT

        pygame.draw.rect(screen, colour, (col * size, row * size, size - 1, size - 1))
    return updated_cells
