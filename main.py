from graphics import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)
    line1 = Line(Point(1,1),Point(200,200))
    #win.draw_line(Line(Point(10,10),Point(400,100)),"red")
    win.draw_line(line1, "red")


    
    cell1 = Cell(win) #Point(20,20),Point(500,500),True,True,True,True)
    #cell2 = Cell(win,50,50,200,200,True,True,True,True)
    cell1.draw(50,50,300,300)
    

    cell2 = Cell(win) #Point(20,20),Point(500,500),True,True,True,True)
    #cell2 = Cell(win,50,50,200,200,True,True,True,True)
    cell2.draw(400,50,500,400)
    
    
    win.wait_for_close()

main()