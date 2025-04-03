from cell import Cell
import time
import random

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)


    def _create_cells(self): # Can be combined with _draw_cell. Check back later
        for i in range(self._num_cols):
            row = []
            for j in range(self._num_rows):
                row.append(Cell(self._win))
            self._cells.append(row)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

        
    def _draw_cell(self, i, j):
        if not self._win:
            return
        x1 = self._x1 + (i * self._cell_size_x)
        y1 = self._y1 + (j * self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()


    def _animate(self):
        self._win.redraw()
        time.sleep(0.01) 


    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)


    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while(True):
            to_visit = []
            left_neighbor_pos = [i - 1, j]
            right_neighbor_pos = [i + 1, j]
            top_neighbor_pos = [i, j - 1]
            bottom_neighbor_pos = [i, j + 1]
            
            if left_neighbor_pos[0] >= 0 and not self._cells[left_neighbor_pos[0]][left_neighbor_pos[1]].visited:  
                left_neighbor_pos.append("left")
                to_visit.append(left_neighbor_pos)
            if right_neighbor_pos[0] <= self._num_cols - 1 and not self._cells[right_neighbor_pos[0]][right_neighbor_pos[1]].visited:  
                right_neighbor_pos.append("right")
                to_visit.append(right_neighbor_pos)
            if top_neighbor_pos[1] >= 0 and not self._cells[top_neighbor_pos[0]][top_neighbor_pos[1]].visited: 
                top_neighbor_pos.append("top")
                to_visit.append(top_neighbor_pos)
            if bottom_neighbor_pos[1] <= self._num_rows - 1 and not self._cells[bottom_neighbor_pos[0]][bottom_neighbor_pos[1]].visited:  
                bottom_neighbor_pos.append("bottom")
                to_visit.append(bottom_neighbor_pos)

            if not to_visit:
                self._draw_cell(i, j)
                return

            next_cell_pos = to_visit[random.randrange(len(to_visit))]
            next_i, next_j, direction = next_cell_pos

            if direction == "top":
                self._cells[i][j].has_top_wall = False
                self._cells[next_i][next_j].has_bottom_wall = False
            elif direction == "bottom":
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_i][next_j].has_top_wall = False
            elif direction == "left":
                self._cells[i][j].has_left_wall = False
                self._cells[next_i][next_j].has_right_wall = False
            elif direction == "right":
                self._cells[i][j].has_right_wall = False
                self._cells[next_i][next_j].has_left_wall = False
            
            self._break_walls_r(next_i, next_j)
            


