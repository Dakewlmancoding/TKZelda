from tkinter import *

class gameWindow:
    #creates game window
    root = Tk()
    root.resizable(False, False)

    #creates the backdrop to draw everything on
    bkgrnd = Canvas(root, width = 1000, height = 1000)
    
