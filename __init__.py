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


import pygame
from classes import *
from constants import *

pygame.init()
pygame.display.set_caption("EZ Refs - 1.0.0")


def DrawWindow(window):
    window.fill(WHITE)


def Main():
    nameText = TextInput(size=(500, 50), max_string_length=37)

    while True:
        DrawWindow(DISPLAY)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return

        nameText.update(events, True)
        nameText.draw(DISPLAY)

        pygame.display.update()


Main()