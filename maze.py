from graphics import Line, Point
from cell import Cell
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        window,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = window
        self._cells = []
        self._create_cells()


    def _create_cells(self):
        #self._cells = [[Cell for _ in range(self.num_cols)] for _ in range(self.num_rows)]

        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i,j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        #cell x1 in relation to top left cell
        cx1 = i * self._cell_size_x
        #cell x1 in relation to top left maze
        cx1 = self._x1 + cx1

        cy1 = j * self._cell_size_y
        cy1 = self._y1 + cy1

        cx2 = cx1 + self._cell_size_x
        cy2 = cy1 + self._cell_size_y

        self._cells[i][j].draw(cx1, cy1, cx2, cy2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

        
            
        


    