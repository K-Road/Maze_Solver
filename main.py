from graphics import Window, Line, Point
from cell import Cell
from maze import Maze
import time

def main():
    win = Window(800, 600)
    #line1 = Line(Point(1,1),Point(200,200))
    #win.draw_line(Line(Point(10,10),Point(400,100)),"red")
  #  win.draw_line(line1, "red")


    
  #  cell1 = Cell(win) #Point(20,20),Point(500,500),True,True,True,True)
    #cell2 = Cell(win,50,50,200,200,True,True,True,True)
  #  cell1.draw(150,150,200,200)
    

  #  cell2 = Cell(win) #Point(20,20),Point(500,500),True,True,True,True)
    #cell2 = Cell(win,50,50,200,200,True,True,True,True)
  #  cell2.draw(400,200,500,300)
    
  #  cell1.draw_move(cell2,True)

  #  c1 = Cell(win)
  #  c1.has_right_wall = False
  #  c1.draw(10,10,50,50)
  #  c2 = Cell(win)
  #  c2.has_left_wall = False
  #  c2.draw(50,10,100,50)

  #  c1.draw_move(c2)
    x1 = 1
    y1 = 1
    num_rows = 15  #44 max
    num_cols = 15 #44 max
    margin = 10
    cell_size_x = (win.width - 2 * margin) / num_cols
    cell_size_y = (win.height - 2 * margin) / num_rows
    #seed = 10
    method = None

   
    maze_create_start_time = time.time()
    m = Maze(margin,margin,num_rows, num_cols,cell_size_x,cell_size_y,win)
    maze_create_end_time = time.time()
    maze_create_time = maze_create_end_time - maze_create_start_time
    
    print(f"Maze created in {maze_create_time}")
    time.sleep(0.05)

    #Test 1
    maze_solve_start = time.time()
    is_solveable = m.solve()
    maze_solve_end = time.time()
    maze_solve_time = maze_solve_end - maze_solve_start
    
    if not is_solveable:
        print("Maze cannot be solved")
    else:
        print(f"Maze solved in {maze_solve_time}") 
      
    #Test 2
    time.sleep(0.05)
    m._reset_cells_visited()
    method = "RLBT"
    maze_solve_start = time.time()
    is_solveable = m.solve(method)
    maze_solve_end = time.time()
    maze_solve_time = maze_solve_end - maze_solve_start
    
    if not is_solveable:
        print("Maze cannot be solved")
    else:
        print(f"Maze solved in {maze_solve_time}")
   
    #Test 3
    time.sleep(0.05)
    m._reset_cells_visited()
    method = "RAND"
    maze_solve_start = time.time()
    is_solveable = m.solve(method)
    maze_solve_end = time.time()
    maze_solve_time = maze_solve_end - maze_solve_start
    
    if not is_solveable:
        print("Maze cannot be solved")
    else:
        print(f"Maze solved in {maze_solve_time}")
    win.wait_for_close()

main()