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