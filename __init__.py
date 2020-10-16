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


import pygame, tkinter
from tkinter import messagebox, Tk, Checkbutton, IntVar, W
from classes import *
from constants import *
from functions import *

pygame.init()
pygame.display.set_caption("EZ Refs - by Tools With Code")

def DrawWindow(window, canvas):
    window.fill(BLACK)
    canvas.Draw()


def Main():
    Tk().withdraw()
    scrolling = IntVar()
    width, height = WIDTH, HEIGHT
    DISPLAY = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    uploadPic = Button((width - 200 - 10, 10), (200, 50), pygame.font.SysFont('freesansbold', 40), "Upload Image", GRAY, BLACK, 5, BLACK)
    instructions = Button((width - 200 - 10, 70), (200, 50), pygame.font.SysFont('freesansbold', 40), "Instructions", GRAY, BLACK, 5, BLACK)
    settings = Button((width - 140 - 10, 130), (140, 50), pygame.font.SysFont('freesansbold', 40), "Settings", GRAY, BLACK, 5, BLACK)
    canvas = Canvas()
    while True:
        uploadPic.ChangeLoc((width - 200 - 10, 10))
        instructions.ChangeLoc((width - 200 - 10, 70))
        settings.ChangeLoc((width - 140 - 10, 130))
        DrawWindow(DISPLAY, canvas)
        uploadPic.Draw(DISPLAY)
        instructions.Draw(DISPLAY)
        settings.Draw(DISPLAY)
        events = pygame.event.get()
        if uploadPic.Clicked(events):
            canvas.AddImage(pygame.image.load(GetFilePath()))
        if instructions.Clicked(events):
            messagebox.showinfo("Instructions", "- Scroll on an image to scale the image\n- Click and drag to move the image")
        if settings.Clicked(events):
            window = Tk()
            Checkbutton(window, text="Invert Scrolling", variable=scrolling).grid(row=0, sticky=W)
            tkinter.mainloop()
        canvas.Update(events, scrolling)
        for event in events:
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.VIDEORESIZE:
                width, height = event.w, event.h
                DISPLAY = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        pygame.display.update()


Main()
