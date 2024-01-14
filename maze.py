from graphics import Line, Point
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
        window=None,
        seed=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = window
        self._cells = []
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

        

    def _create_cells(self):
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
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        
        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1,self._num_rows-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            #check L (West)
            if i > 0 and self._cells[i-1][j].visited == False:
                    to_visit.append((i-1, j,'L'))
            #check R (East)
            if i < self._num_cols-1 and self._cells[i+1][j].visited == False:
                    to_visit.append((i+1,j,'R'))
            #check T (North)
            if j > 0 and self._cells[i][j-1].visited == False:
                    to_visit.append((i,j-1,'T'))
            #check B (South)
            if j < self._num_rows-1 and self._cells[i][j+1].visited == False:
                    to_visit.append((i,j+1,'B'))
            if len(to_visit) == 0:
                self._draw_cell(i,j)
                return
            
            direction = random.randrange(len(to_visit))
            next_cell = to_visit[direction]

            if next_cell[2] == 'L':
                self._cells[i][j].has_left_wall = False
                self._cells[next_cell[0]][next_cell[1]].has_right_wall = False
            if next_cell[2] == 'R':
                self._cells[i][j].has_right_wall = False
                self._cells[next_cell[0]][next_cell[1]].has_left_wall = False
            if next_cell[2] == 'T':
                self._cells[i][j].has_top_wall = False
                self._cells[next_cell[0]][next_cell[1]].has_bottom_wall = False
            if next_cell[2] == 'B':
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_cell[0]][next_cell[1]].has_top_wall = False
            
            self._break_walls_r(next_cell[0],next_cell[1])
            
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    #return True if current cell is end cell or leads to end cell
    def _solve_r(self, i, j, method):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols -1 and j == self._num_rows -1: #at end
             return True
        if method is None:
            method = "LRTB"
        #decide which direction is free, default choose LRTB
        if method.upper() == "LRTB":
            #check L (West)
            if self._solve_r_west(i,j,method):
                return True            
            #check R (East)
            if self._solve_r_east(i,j,method):
                return True
            #check T (North)
            if self._solve_r_north(i,j,method):
                return True              
            #check B (South)
            if self._solve_r_south(i,j,method):
                return True                      
            #no direction found
            return False
        
        if method.upper() == "RLBT":
            #check R (East)
            if self._solve_r_east(i,j,method):
                return True
            #check L (West)
            if self._solve_r_west(i,j,method):
                return True
            #check B (South)
            if self._solve_r_south(i,j,method):
                return True            
            #check T (North)
            if self._solve_r_north(i,j,method):
                return True                                      
            #no direction found
            return False
        
    def _solve_r_east(self,i,j,method):
        if i < self._num_cols-1 and self._cells[i+1][j].visited == False and self._cells[i][j].has_right_wall == False:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1,j,method):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j],True)

    def _solve_r_west(self,i,j,method):
        if i > 0 and self._cells[i-1][j].visited == False and self._cells[i][j].has_left_wall == False:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1,j,method):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j],True)

    def _solve_r_north(self,i,j,method):
        if j > 0 and self._cells[i][j-1].visited == False and self._cells[i][j].has_top_wall == False:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i,j-1,method):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1],True)        

    def _solve_r_south(self,i,j,method):
        if j < self._num_rows-1 and self._cells[i][j+1].visited == False and self._cells[i][j].has_bottom_wall == False:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i,j+1,method):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1],True)

    def _solve_r_rand(self,i,j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols -1 and j == self._num_rows -1: #at end
             return True   
        #if method.upper() == "RAND":
        while True:
            available_path = []
            #check R (East)
            if i < self._num_cols-1 and self._cells[i+1][j].visited == False and self._cells[i][j].has_right_wall == False:
                available_path.append((i+1,j,'R'))
            #check L (West)
            if i > 0 and self._cells[i-1][j].visited == False and self._cells[i][j].has_left_wall == False:
                available_path.append((i-1, j,'L'))
            #check B (South)
            if j < self._num_rows-1 and self._cells[i][j+1].visited == False and self._cells[i][j].has_bottom_wall == False:
                available_path.append((i,j+1,'B'))
            #check T (North)
            if j > 0 and self._cells[i][j-1].visited == False and self._cells[i][j].has_top_wall == False:
                available_path.append((i,j-1,'T'))

            if len(available_path) == 0: #no direction found
                return False
        
            direction = random.randrange(len(available_path))
            next_cell = available_path[direction]

            self._cells[i][j].draw_move(self._cells[next_cell[0]][next_cell[1]])

            if self._solve_r_rand(next_cell[0],next_cell[1]):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[next_cell[0]][next_cell[1]],True)




    
    def solve(self, method="LRTB"):
        print(method)
        if method == "LRTB" or method == "RLBT" or method is None:
            return self._solve_r(0,0, method)
        elif method == "RAND":
            return self._solve_r_rand(0,0)
        else:
            return
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.005)

        
            
        


    
