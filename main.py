from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)
    Maze(25, 25, 11, 15, 50, 50, win)
    win.wait_for_close()


main()