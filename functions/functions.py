from tkinter import Tk
from tkinter.filedialog import askopenfilename

def getFilePath():
    Tk().withdraw()
    path = askopenfilename()
    return path