from graphics import Window
from maze import Maze

def main():
    win = Window(1920, 1080)
    Maze(6, 25, 20, 38, 50, 50, win)
    win.wait_for_close()
    

main()