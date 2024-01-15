import tkinter as tk
from tkinter import Tk, BOTH, Canvas, simpledialog

class GUIWithMenu:
    def __init__(self,root):
        self.root = root
        self.root.title("GUI with Menu")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        
        self.create_menu()

        self.label = tk.Label(self.root, text="Click to enter")
        self.label.pack(pady=10)

        self.button_method = tk.Button(self.root,text="Method", command=self.get_method)
        self.button_method.pack(pady=10)

        self.button_random = tk.Button(self.root,text="Random", command=lambda: self.set_method("Random"))
        self.button_random.pack(pady=10)

        self.button_launch = tk.Button(self.root,text="Launch", command=self.start)
        self.button_launch.pack(pady=10)
        total_button_height = sum(button.winfo_reqheight() + 10 for button in [self.button_method, self.button_launch, self.button_random])

        canvas_height = total_button_height + 20
        self.canvas = Canvas(self.root, bg="white", width=250, height=canvas_height)
        self.canvas.pack(fill=tk.BOTH, expand=1)

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

    def get_integer_h(self):
        try:
            self.value['h'] = simpledialog.askinteger("Input","Enter Height:")
            if self.value.get('h') is not None:
                self.label.config(text=f"Height = {self.value.get('h')}")
                print(self.value.get('h'))  ###DEBUG
        except ValueError:
            tk.messagebox.showerror("Error", "Enter valid integer")
    
    def get_integer_w(self):
        try:
            self.value['w'] = simpledialog.askinteger("Input","Enter Width:")
            if self.value.get('w') is not None:
                self.label.config(text=f"Width = {self.value.get('w')}")
                print(self.value.get('w'))  ###DEBUG
        except ValueError:
            tk.messagebox.showerror("Error", "Enter valid integer")

    def get_method(self):
        self.value['method'] = simpledialog.askstring("Input","Enter pathing algorthym:")
        if self.value.get('method') is not None:
            print(self.value.get('method'))  ###DEBUG

    def set_method(self,method):
        self.value['method'] = method
        if self.value.get('h') is None or self.value.get('w') is None:
            tk.messagebox.showerror("Error", "Enter valid Height and/or Width")
        else:
            self.start()


    def get_user_input(self):
        return self.value
    
    def start(self):
        self.close()

    def wait_for_close(self):
        self.root.mainloop()
    
    def close(self):
        self.root.destroy()