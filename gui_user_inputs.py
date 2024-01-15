import tkinter as tk
from tkinter import Tk, BOTH, Canvas, simpledialog

class User_Input_App:
    def __init__(self, root):
        #self.width = 50
        #self.height = 50
        self.__root = root
        self.__root.title("User inputs")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", width=50, height=50)
        self.__canvas.pack(fill=tk.BOTH, expand=1)
        #self.__running = False

        self.label = tk.Label(root,text="Click to enter")
        self.label.pack(pady=10)

        self.button = tk.Button(root,text="Enter height:", command=self.get_user_input)
        self.button.pack(pady=10)
        self.button = tk.Button(root,text="Enter width:", command=self.get_user_input)
        self.button.pack(pady=10)

    def get_user_input(self):
        user_input = []
        user_input.append(simpledialog.askinteger("Input", "Height:"))
        user_input.append(simpledialog.askinteger("Input", "Width:"))
        if user_input:
            self.label.config(text=f"Height = {user_input[0]}")
            self.label.config(text=f"Width = {user_input[1]}")
            return user_input

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

 #   def draw_line(self, line, fill_colour="black"):
 #       line.draw(self.__canvas,fill_colour)

    def wait_for_close(self):
        # self.__running = True
        # while self.__running:
        #     self.redraw()
        # print("window closed...")
        self.__root.mainloop()

    def close(self):
        #self.__running = False
        self.__root.destroy()

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = User_Input_App(root)
#     root.wait_for_close()

class GUIWithMenu:
    def __init__(self,root):
        self.root = root
        self.root.title("GUI with Menu")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.root, bg="white", width=250, height=250)
        self.create_menu()

        self.value = dict(h = None, w= None)

    def create_menu(self):
        menu_bar = tk.Menu(self.root)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.root.destroy)
        menu_bar.add_cascade(label="File", menu=file_menu)

        input_menu = tk.Menu(menu_bar,tearoff=0)
        input_menu.add_command(label="Get Height",command=self.get_integer_h)
        input_menu.add_command(label="Get Width",command=self.get_integer_w)
        menu_bar.add_cascade(label="Maze Input", menu=input_menu)

        self.root.config(menu=menu_bar)

        self.button = tk.Button(self.root,text="Method", command=self.get_method)
        self.button.pack(pady=10)

        self.button = tk.Button(self.root,text="Random", command=lambda: self.set_method("Random"))
        self.button.pack(pady=10)

        self.button = tk.Button(self.root,text="Launch", command=self.start)
        self.button.pack(pady=10)

    def get_integer_h(self):
        self.value['h'] = simpledialog.askinteger("Input","Enter Height:")
        if self.value.get('h') is not None:
            print(self.value.get('h'))
            #return value_w
    
    def get_integer_w(self):
        self.value['w'] = simpledialog.askinteger("Input","Enter Width:")
        if self.value.get('w') is not None:
            print(self.value.get('w'))
            #return value_h

    def get_method(self):
        self.value['method'] = simpledialog.askstring("Input","Enter pathing algorthym:")
        if self.value.get('method') is not None:
            print(self.value.get('method'))

    def set_method(self,method):
        self.value['method'] = method
        self.start()


    def get_user_input(self):
        return self.value
    
    def start(self):
        self.close()

    def wait_for_close(self):
        self.root.mainloop()
    
    def close(self):
        self.root.destroy()