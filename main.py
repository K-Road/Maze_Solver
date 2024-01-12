from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    line1 = Line(Point(1,1),Point(5,5))
    win.draw_line(Line(Point(1,1),Point(400,100)),"red")
    win.wait_for_close()

main()