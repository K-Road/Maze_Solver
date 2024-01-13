from graphics import Line, Point

class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window

    def draw(self, x1,y1,x2,y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        wall = Line(Point(x1,y1),Point(x1,y2))
        if self.has_left_wall:
            self._win.draw_line(wall)
        else:
            self._win.draw_line(wall,"white")
        wall = Line(Point(x2,y1),Point(x2,y2))
        if self.has_right_wall:
            self._win.draw_line(wall)
        else:
            self._win.draw_line(wall,"white")
        wall = Line(Point(x1,y1),Point(x2,y1))
        if self.has_top_wall:
            self._win.draw_line(wall)
        else:
            self._win.draw_line(wall,"white")
        wall = Line(Point(x1,y2),Point(x2,y2))
        if self.has_bottom_wall:    
            self._win.draw_line(wall)
        else:
            self._win.draw_line(wall,"white")

    def draw_move(self, to_cell, undo=False): #adjacent cell move
        if self._win is None:
            return
        colour = "red"
        if undo:
            colour = "gray"

        x_mid = (self._x1 + self._x2) / 2
        y_mid = (self._y1 + self._y2) / 2

        t_x_mid = (to_cell._x1 + to_cell._x2) /2
        t_y_mid = (to_cell._y1 + to_cell._y2) /2

        #left
        if self._x1 > to_cell._x1:
            line = Line(Point(self._x1,y_mid), Point(x_mid,y_mid))
            self._win.draw_line(line,colour)
            line = Line(Point(t_x_mid,t_y_mid), Point(to_cell._x2, t_y_mid))
            self._win.draw_line(line,colour)

        #right
        elif self._x1 < to_cell._x1:
            line = Line(Point(x_mid,y_mid), Point(self._x2,y_mid))
            self._win.draw_line(line,colour)
            line = Line(Point(to_cell._x1, t_y_mid), Point(t_x_mid,t_y_mid))
            self._win.draw_line(line,colour)
        
        #up
        elif self._y1 > to_cell._y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self._y1))
            self._win.draw_line(line,colour)
            line = Line(Point(t_x_mid,to_cell._y2), Point(t_x_mid,t_y_mid))
            self._win.draw_line(line,colour)
        
        #down
        elif self._y1 < to_cell._y1:
            line = Line(Point(x_mid,y_mid),Point(x_mid,self._y2))
            self._win.draw_line(line,colour)
            line = Line(Point(t_x_mid,t_y_mid),Point(t_x_mid,to_cell._y1))
            self._win.draw_line(line,colour)
