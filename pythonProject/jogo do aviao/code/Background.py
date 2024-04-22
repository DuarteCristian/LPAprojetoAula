#!/usr/bin/python
# -*- coding: utf-8 -*-


class Background():
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def movaula_pratica_02e(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
