"""
Dungeon Brawler

Opprettet av: Frithjof Nilsen
Dato: 12.01.2025


player.py styrer beveglse og tegning av spilleren.

For forklaring av spillet og koden, se READ_ME.md
"""

# Importerer filene til prosjektet
import pygame
import settings as st
import utils


class Player:
    def __init__(self):
        window_size = pygame.display.get_window_size()
        # Lagrer posisjonen til player som en todimensjonal pygame vektor.
        # Dette er mest for at koden skal være mer oversiktlig.
        self.pos = pygame.Vector2(window_size[0] // 2 - st.PLAYER_SIZE[0] // 2,
                                  window_size[1] // 2 - st.PLAYER_SIZE[1] // 2)
        # Lagrer også hastigheten til player som en todimensjonal pygame vektor.
        self.velocity = pygame.Vector2(0, 0)
        self.on_ground = False
        self.player_image = utils.load_and_scale_image("assets/characters/player.png", st.PLAYER_SIZE[0],
                                                       st.PLAYER_SIZE[1])
        self.player_rect = None
        self.collision_detected = False
        self.health = st.PLAYER_START_HEALTH

    def move(self):
        if self.health > 0:  # Fryser spilleren dersom man går tom for liv
            self.handle_input()
            self.posx()
            self.gravity()
            self.check_ground_collision()
            self.keep_player_within_screen()

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.velocity.x = -st.PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.velocity.x = st.PLAYER_SPEED
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity.y = st.JUMP_STRENGTH
            self.on_ground = False

    def gravity(self):
        if not self.on_ground:
            self.velocity.y += st.GRAVITY
            self.pos.y += self.velocity.y

    def check_ground_collision(self):  # Holder player over ground level
        if self.pos.y + st.PLAYER_SIZE[1] >= st.GROUND_LEVEL:
            self.pos.y = st.GROUND_LEVEL - st.PLAYER_SIZE[1]
            self.on_ground = True
            if not self.collision_detected:
                self.velocity = pygame.Vector2(0, 0)

        elif self.pos.y + st.PLAYER_SIZE[1] > 0:
            self.on_ground = False

    def keep_player_within_screen(self):  # Holder player innenfor skjermen i x-retning
        if self.pos.x + st.PLAYER_SIZE[0] > st.WINDOW_SIZE[0]:
            self.pos.x = st.WINDOW_SIZE[0] - st.PLAYER_SIZE[0]
        if self.pos.x < 0:
            self.pos.x = 0

    def draw(self, window):  # Tegner spilleren når health er over 0
        if self.health > 0:
            window.blit(self.player_image, (self.pos.x, self.pos.y, st.PLAYER_SIZE[0], st.PLAYER_SIZE[1]))

    def rect(self):  # Lager et pygame rektangel for å sjekke kollisjoner med enemy
        self.player_rect = pygame.Rect(self.pos.x, self.pos.y, st.PLAYER_SIZE[0], st.PLAYER_SIZE[1])
        return self.player_rect

    def hit_left(self):  # Beveger spilleren opp og til høyre dersom man blir truffet fra venstre
        self.velocity.y = st.HIT_SPEED[1]
        self.pos.y += self.velocity.y
        self.velocity.x = st.HIT_SPEED[0]
        if not self.on_ground:
            self.pos.x += self.velocity.x

    def hit_right(self):  # Beveger spilleren opp og til venstre om man blir truffet fra høyre
        self.velocity.y = st.HIT_SPEED[1]
        self.pos.y += self.velocity.y
        self.velocity.x = -1 * st.HIT_SPEED[0]
        if not self.on_ground:
            self.pos.x += self.velocity.x

    def posx(self):  # Oppdaterer spillerposisjonen i x-retning
        self.pos.x += self.velocity.x

    def restart(self):  # Restarter Player-klassen
        self.__init__()
