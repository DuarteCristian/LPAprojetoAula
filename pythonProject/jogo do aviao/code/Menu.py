#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WITHE, COLOR_BLACK, COLOR_RED


class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf = pygame.image.load('./asset/menuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        menu_opition = 0

        while True:
            #desenhar na tela
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, 'GAME', COLOR_BLACK, (WIN_WIDTH / 2, 30))
            self.menu_text(50, 'of', COLOR_BLACK, (WIN_WIDTH / 2, 60))
            self.menu_text(50, 'PLANE', COLOR_BLACK, (WIN_WIDTH / 2, 90))

            for i in range(len(MENU_OPTION)):
                if i == menu_opition:
                    self.menu_text(30, MENU_OPTION[i], COLOR_RED, ((WIN_WIDTH / 2), 200 + 35 * i))
                else:
                    self.menu_text(30, MENU_OPTION[i], COLOR_WITHE, ((WIN_WIDTH / 2), 200 + 35 * i))
            # verificar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_opition < len(MENU_OPTION) -1:
                            menu_opition += 1
                        else:
                            menu_opition = 0

                    if event.key == pygame.K_UP:
                         if menu_opition > 0:
                            menu_opition -= 1
                         else:
                            menu_opition = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                         return MENU_OPTION[menu_opition]

            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="lucida sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
