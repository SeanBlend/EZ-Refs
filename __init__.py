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


import pygame, sys, os
from pygame.locals import *
from functions import functions, Test
pygame.init()

cls = lambda: os.system("cls")

width = 1920
height = 1080
cls()
pygame.display.set_caption("EZ Refs - 1.0.0")
DISPLAY = pygame.display.set_mode((0, 0), RESIZABLE)
path = functions.GetFilePath()
image = pygame.image.load(path)
boxx = Test.TextInput("Boxx")
boxy = Test.TextInput("Boxy")
imgWidth = pygame.Surface.get_width(image)
imgHeight = pygame.Surface.get_height(image)
imageRect = image.get_rect()
imageRect.center = (width / 2, height / 2)
black = (0, 0, 0)
mouseClicked = pygame.mouse.get_pressed()
mousePos = pygame.mouse.get_pos()
DISPLAY.fill(black)
while True:
    mousePos = pygame.mouse.get_pos()
    events = pygame.event.get()
    boxx.update(events, True)
    boxy.update(events, True)
    DISPLAY.blit(boxx.get_surface(), (0, 0))
    DISPLAY.blit(boxy.get_surface(), (0, 0))
    image = pygame.image.load(path)
    imageRect = image.get_rect()
    imageRect.center = (width / 2, height / 2)
    DISPLAY.blit(image, imageRect)
    pygame.display.update()
    functions.CheckEvent(events)