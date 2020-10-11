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
from functions import functions
pygame.init()

cls = lambda: os.system("cls")

width = 1920
height = 1080
cls()
pygame.display.set_caption("EZ Refs - 1.0.0")
DISPLAY = pygame.display.set_mode((0, 0), RESIZABLE)
path = functions.GetFilePath()
image = pygame.image.load(path)
boxx = int(input("Boxx: "))
boxy = int(input("Boxy: "))
imgWidth = pygame.Surface.get_width(image)
imgHeight = pygame.Surface.get_height(image)
imageRect = image.get_rect()
imageRect.center = (boxx, boxy)
mouse = pygame.mouse.get_pos()
black = (0, 0, 0)
mouseClicked = pygame.mouse.get_pressed()
mousePos = pygame.mouse.get_pos()
DISPLAY.fill(black)
while True:
    image = pygame.image.load(path)
    imageRect = image.get_rect()
    imageRect.center = (boxx, boxy)
    DISPLAY.blit(image, imageRect)
    cls()
    pygame.display.update()
    functions.CheckEvent()