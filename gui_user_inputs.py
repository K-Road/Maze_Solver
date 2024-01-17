import tkinter as tk
from tkinter import Tk, BOTH, Canvas, simpledialog

class GUIWithMenu:
    def __init__(self,root):
        self.root = root
        self.root.title("GUI with Menu")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.running = False
        
        self.create_menu()
        self.buttons_dict = {}

        self.label = tk.Label(self.root, text="Create Maze")
        self.label.pack(pady=10, side='top')

        self.button_method = tk.Button(self.root,text="Method", command=self.get_method)
        self.button_method.pack(pady=5)

        self.buttons_dict['m-rand'] = tk.Button(self.root,text="Random", command=lambda: self.set_method("Random"))
        #self.buttons_dict['m-rand'].pack(pady=10)

        # self.button_launch = tk.Button(self.root,text="Launch", command=self.start)
        # self.button_launch.pack(pady=10)

        # button_texts = []
        # button_texts.append("Launch v2")
        #self.buttons.append(tk.Button(self.root,text='Launch v2', command=self.start))
        self.buttons_dict['run'] = tk.Button(self.root,text='Launch v2', command=self.start)

        for button in self.buttons_dict:
            self.buttons_dict[button].pack(pady=5, side='top')
    #      total_button_array_height += button.winfo_reqheight() + 10     
   
        self.input_fields = {'h':None,'w':None}

        self.label_height = tk.Label(self.root, text="Height:")
        self.label_width = tk.Label(self.root, text="Width:")
        self.input_fields['h'] = tk.Entry(self.root,width=10)
        self.input_fields['w'] = tk.Entry(self.root,width=10)
        self.label_height.pack(padx=5,pady=5, side='left')
        self.input_fields['h'].pack(padx=5,pady=0,side='left')
        self.label_width.pack(padx=5,pady=5, side='left')
        self.input_fields['w'].pack(padx=5,pady=0,side='left')
      #  total_entry_height = 50
            
      #  total_button_array_height = 0
        

       # total_button_height = sum(button.winfo_reqheight() + 10 for button in [self.button_method, self.button_launch, self.button_random])
       # total_button_height += total_button_array_height
       # total_button_height += total_entry_height

       # canvas_height = total_button_height + 20
      #  self.canvas = Canvas(self.root, bg="white", width=250, height=canvas_height)
       # self.canvas.pack(fill=tk.BOTH, expand=1)

        self.value = dict(h = None, w= None, method="LRBT")

    def create_menu(self):
        menu_bar = tk.Menu(self.root)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.root.destroy)
        menu_bar.add_cascade(label="File", menu=file_menu)

      #  input_menu = tk.Menu(menu_bar,tearoff=0)
      #  menu_bar.add_cascade(label="Maze Input", menu=input_menu)

        self.root.config(menu=menu_bar)

   # def get_integer_h(self):
        # try:
        #     self.value['h'] = simpledialog.askinteger("Input","Enter Height:")
        #     if self.value.get('h') is not None:
        #         self.label.config(text=f"Height = {self.value.get('h')}")
        #         print(self.value.get('h'))  ###DEBUG
        # except ValueError:
        #     tk.messagebox.showerror("Error", "Enter valid integer")
    
   # def get_integer_w(self):
        # try:
        #     self.value['w'] = simpledialog.askinteger("Input","Enter Width:")
        #     if self.value.get('w') is not None:
        #         self.label.config(text=f"Width = {self.value.get('w')}")
        #         print(self.value.get('w'))  ###DEBUG
        # except ValueError:
        #     tk.messagebox.showerror("Error", "Enter valid integer")

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
        return self.value, self.running
           
    def start(self):
        self.value['h'] = int(self.input_fields['h'].get())
        self.value['w'] = int(self.input_fields['w'].get())
        if self.value['h'] is not None:
            print(self.value['h'])
        self.running = True
        self.close()

    def wait_for_close(self):
        self.root.mainloop()
    
    def close(self):
        self.root.destroy()