from graphics import Window, Line, Point
from cell import Cell
from maze import Maze
from gui_user_inputs import User_Input_App, GUIWithMenu
import time
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    #app = User_Input_App(root)
    app = GUIWithMenu(root)
    app.wait_for_close()
    user_input = app.get_user_input()
    #root.destroy()

def main(user_input):
    
    #menu = User_Input_App()
    #h = app.get_user_input()
    print(user_input)
    h = user_input.get('h')
    w = user_input.get('w')
    #win = Window(800, 600)
    win = Window(h,w)
    x1 = 1
    y1 = 1
    num_rows = 10  #44 max
    num_cols = 10 #44 max
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
    time.sleep(0.0005)

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

main(user_input)