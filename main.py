from graphics import Window
from maze import Maze


def main():
    win = Window(1920, 1080)
    Maze(6, 25, 20, 38, 50, 50, win).solve() #1080p maze
    #Maze(25, 25, 11, 15, 50, 50, win).solve() #600p maze
    win.wait_for_close()
    

main()