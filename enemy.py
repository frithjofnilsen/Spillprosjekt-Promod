"""
Dungeon Brawler

Opprettet av: Frithjof Nilsen
Dato: 12.01.2025


enemy.py styrer beveglse og tegning av fienden.

For forklaring av spillet og koden, se READ_ME.md
"""

# Importerer filene til prosjektet
from random import choice, randint
import pygame
import player
import settings as st
import utils


class Enemy:
    def __init__(self):
        self.player = player.Player()
        # Lagrer posisjonen til enemy i en pygame vektor, slik som med player
        self.pos = pygame.Vector2(self.player.pos.x + st.SPAWN_DISTANCE_FROM_PLAYER * choice([-1, 1]),
                                  st.GROUND_LEVEL - st.ENEMY_SIZE[1])
        self.enemy_image = utils.load_and_scale_image("assets/characters/enemy.png", st.ENEMY_SIZE[0],
                                                      st.ENEMY_SIZE[1])
        # Setter enemy_speed til en varierende hastighet, i tilfeldig retning
        self.enemy_speed = st.ENEMY_SPEED * choice([-1, 1]) * randint(1, 5)
        self.enemy_rect = None
        self.alive = True

    def move(self):  # Oppdaterer posisjonen til enemy
        self.pos.x += self.enemy_speed
        self.keep_within_screen()

    def keep_within_screen(self):
        # Holder enemy innenfor skjermen og bytter retningen til farten når enemy treffer kanten av vinduet
        if self.pos.x + st.ENEMY_SIZE[0] > st.WINDOW_SIZE[0]:
            self.pos.x = st.WINDOW_SIZE[0] - st.ENEMY_SIZE[0]
            self.enemy_speed *= -1
        if self.pos.x < 0:
            self.pos.x = 0
            self.enemy_speed *= -1

    def draw(self, window):  # Tegner enemy, og kaller på funksjonen rect
        window.blit(self.enemy_image, (self.pos.x, self.pos.y, st.ENEMY_SIZE[0], st.ENEMY_SIZE[1]))
        self.rect()

    def rect(self):  # Lager et pygame rektangel for enemy for å sjekke kollisjoner med player
        self.enemy_rect = pygame.Rect(self.pos.x, self.pos.y, st.ENEMY_SIZE[0], st.ENEMY_SIZE[1])
        return self.enemy_rect

    def restart(self):  # Starter player-klassen på nytt
        self.__init__()
