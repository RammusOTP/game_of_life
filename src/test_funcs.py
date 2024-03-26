import numpy as np
import pygame
from funcs import update
from colours import *


def test_update_without_progress():
    # Create a mock screen with dimensions 800x600
    screen = pygame.Surface((800, 600))

    # Create a mock grid of cells as a NumPy array
    cells = np.array([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ])

    # Set cell size
    size = 10

    # Test the update function without progress
    updated_cells = update(screen, cells, size)
    expected_updated_cells = np.array([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ])
    assert np.array_equal(updated_cells,
                          expected_updated_cells), f"Update without progress failed.\nExpected:\n{expected_updated_cells}\nActual:\n{updated_cells}"


def test_update_with_progress():
    # Create a mock screen with dimensions 800x600
    screen = pygame.Surface((800, 600))

    # Create a mock grid of cells as a NumPy array
    cells = np.array([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])

    # Set cell size
    size = 10

    # Test the update function with progress
    updated_cells = update(screen, cells, size, with_progress=True)

    # Get the colors of the cells from the screen
    colors = np.array([
        [screen.get_at((col * size + size // 2, row * size + size // 2))[:3]
         for col in range(cells.shape[1])]
        for row in range(cells.shape[0])
    ])

    # Define the expected colors based on the color constants
    expected_colors = np.array([
        [DIE_NEXT, BG, BG],
        [BG, ALIVE_NEXT, BG],
        [BG, BG, DIE_NEXT]
    ])

    # Assert if the colors of the cells match the expected colors
    assert np.array_equal(colors,
                          expected_colors), f"Update with progress failed. Expected:\n{expected_colors}\nActual:\n{colors}"


if __name__ == "__main__":
    test_update_without_progress()
    test_update_with_progress()
    print("All tests passed!")
