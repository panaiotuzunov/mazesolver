class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self._create_cells(num_cols, num_rows)


    def _create_cells(self, num_cols, num_rows):
        self._cells = []
        for i in range(num_cols):
            for j in range(num_rows):
                pass


        