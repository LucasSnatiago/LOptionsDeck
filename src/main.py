from tkinter import *
from utils import commands
 
class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
 
        self.title("Launcher Options Deck")
        self.minsize(800, 600)
 
root = Root()
root.mainloop()