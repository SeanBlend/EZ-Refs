#  ##### BEGIN GPL LICENSE BLOCK #####
# 
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####

import pygame, sys
from pygame.locals import *
import tkinter
from tkinter import Tk
from tkinter.filedialog import askopenfilename

window = tkinter.Tk()

def GetFilePath():
    Tk().withdraw()
    path = askopenfilename()
    return path

def CheckEvent(events):
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def TextInput():
    userInput = int(str(tkinter.Entry(window, font=('freesansbold', 35))))
    return userInput