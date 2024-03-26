import numpy as np
import pygame
from funcs import update
from colours import *


def test_update_without_progress():
    """
    Test the update function without progress visualization.

    Raises an assertion error if the test array does not match the expected one

    :return: None
    """
    screen = pygame.Surface((800, 600))

    cells = np.array([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ])

    size = 10

    updated_cells = update(screen, cells, size)
    expected_updated_cells = np.array([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ])
    assert np.array_equal(updated_cells,
                          expected_updated_cells), (f"Update without progress failed.\nExpected:"
                                                    f"\n{expected_updated_cells}\nActual:\n{updated_cells}")


def test_update_with_progress():
    """
    Test the update function with progress visualization

    Raises an assertion error if the test array does not match the colours expected.

    :return:
    """
    screen = pygame.Surface((800, 600))

    cells = np.array([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])

    size = 10

    update(screen, cells, size, with_progress=True)

    colors = np.array([
        [screen.get_at((col * size + size // 2, row * size + size // 2))[:3]
         for col in range(cells.shape[1])]
        for row in range(cells.shape[0])
    ])

    expected_colors = np.array([
        [DIE_NEXT, BG, BG],
        [BG, ALIVE_NEXT, BG],
        [BG, BG, DIE_NEXT]
    ])

    assert np.array_equal(colors,
                          expected_colors), (f"Update with progress failed. Expected:"
                                             f"\n{expected_colors}\nActual:\n{colors}")


if __name__ == "__main__":
    test_update_without_progress()
    test_update_with_progress()
    print("All tests passed!")
