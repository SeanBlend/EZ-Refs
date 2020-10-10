import pygame, sys, os
from pygame.locals import *
from tkinter import Tk
from tkinter.filedialog import askopenfilename
pygame.init()

cls = lambda: os.system("cls")
held = True

width = 1920
height = 1080
cls()
pygame.display.set_caption("EZ Ref - 1.0.0")
display = pygame.display.set_mode((0, 0), RESIZABLE)
Tk().withdraw()
path = askopenfilename()
image = pygame.image.load(path)
imgWidth = pygame.Surface.get_width(image)
imgHeight = pygame.Surface.get_height(image)
imageRect = image.get_rect()
imageRect.center = (int(width / 2), int(height / 2))
mouse = pygame.mouse.get_pos()
black = (0, 0, 0)
display.fill(black)
while True:
    image = pygame.image.load(path)
    imageRect = image.get_rect()
    imageRect.center = (int(width / 2), int(height / 2))
    display.blit(image, imageRect)
    cls()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse[0] >= imageRect.center[0] - imgWidth / 2 and mouse[0] <= imageRect.center[0] + imgWidth / 2:
                if mouse[1] >= imageRect.center[1] + imgHeight / 2 and mouse[1] <= imageRect.center[1] + imgHeight / 2:
                    if held:
                        imageRect.center = (mouse[0], mouse[1])