from graphics import Window, Line, Point
from cell import Cell


def main():
    win = Window(800, 600)
    cell_1 = Cell(win)
    cell_1.has_top_wall, cell_1.has_left_wall, cell_1.has_right_wall = True, True, True
    cell_1.draw(10, 10, 50, 50)
    cell_2 = Cell(win)
    cell_2.has_bottom_wall, cell_2.has_left_wall, cell_2.has_right_wall = True, True, True
    cell_2.draw(10, 50, 50, 100)
    cell_1.draw_move(cell_2, True)

    win.wait_for_close()


main()