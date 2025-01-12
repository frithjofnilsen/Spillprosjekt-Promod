"""
Dungeon Brawler

Opprettet av: Frithjof Nilsen
Dato: 12.01.2025

Dette er hovedfilen til spillet. Den styrer alt, og kaller på funksjoner fra de andre filene.

For forklaring av spillet og koden, se READ_ME.md
"""

# Importerer filene til prosjektet
import pygame
import enemy
import player
import settings as st
import utils


class Game:
    def __init__(self):  # Definerer variabler som blir brukt i funksjonene i Game klassen
        pygame.init()  # Starter pygame modulen
        self.clock = pygame.time.Clock()

        self.running = True
        self.background = None
        self.ground = None

        self.window = pygame.display.set_mode((st.WINDOW_SIZE[0], st.WINDOW_SIZE[1]))
        pygame.display.set_caption("Dungeon Brawler")

        self.player = player.Player()  # Lagrer Player-klassen i player.py til self.player
        self.enemy = enemy.Enemy()  # Lagrer Enemy-klassen i enemy.py til self.enemy

        # Parametere
        self.player.health = st.PLAYER_START_HEALTH
        self.last_collision_time = 0
        self.score = 0
        self.last_health_increase_score = -10

    def load_map(self):  # Laster inn bilder til bakgrunn og bakken
        # Bruker funksjon fra utils.py for å laste inn og skalere bilder
        self.background = utils.load_and_scale_image(
            "assets/images/background.png", st.BACKGROUND_SIZE[0], st.BACKGROUND_SIZE[1]
        )
        self.ground = utils.load_and_scale_image(
            "assets/images/ground.png", st.GROUND_SIZE[0], st.GROUND_SIZE[1]
        )

    def movement(self):  # Kaller på funkjonene som styrer bevegelse og spiller-fiende interaksjoner
        self.player.move()
        self.enemy.move()
        self.player_interaction()

    def draw(self):
        # Fyller skjermen med bakgrunnsbilder
        for y in range(0, st.WINDOW_SIZE[1], st.BACKGROUND_SIZE[1]):
            for x in range(0, st.WINDOW_SIZE[0], st.BACKGROUND_SIZE[0]):
                self.window.blit(self.background, (x, y))

        # Tegner bakken
        for x in range(0, st.WINDOW_SIZE[0], st.GROUND_SIZE[0]):
            self.window.blit(self.ground, (x, st.WINDOW_SIZE[1] - st.GROUND_SIZE[1]))

        # Kaller på ulile draw-funksjoner i klassene Player, Enemy og Game.
        self.player.draw(self.window)
        self.enemy.draw(self.window)

        self.draw_health()
        self.draw_score()
        self.draw_end_screen()

        pygame.display.flip()  # Oppdaterer skjermen

    def player_interaction(self):
        # Bruker .colliderect() fra pygame for å sjekke om player- og enemy-rektanglene kolliderer.
        current_time = pygame.time.get_ticks()  # Tid siden spillet startet
        if (self.player.rect().colliderect(self.enemy.rect()) and self.player.on_ground and not
        self.player.collision_detected):
            if current_time - self.last_collision_time > st.IMMORTAL_TIME:
                self.player.collision_detected = True
                self.last_collision_time = current_time
                self.player.health -= 1
                self.player.collision_detected = False

            # Kaller på ulike funksjoner i klassen Player i forhold til
            # hvilken side player og enemy treffer hverandre på.
            if self.player.pos.x > self.enemy.pos.x:
                self.player.hit_left()
            if self.player.pos.x < self.enemy.pos.x:
                self.player.hit_right()


        elif self.player.rect().colliderect(self.enemy.rect()) and not self.player.collision_detected:
            if current_time - self.last_collision_time > st.IMMORTAL_TIME:
                self.enemy.__init__()  # Restarter enemy-klassen
                self.score += 1
                self.last_collision_time = current_time
                self.player.velocity.y = -15
            else:
                self.player.velocity.y = -15

        if (self.score > 0 and self.score % 10 == 0 and self.player.health < st.PLAYER_START_HEALTH and
                self.score != self.last_health_increase_score):
            # Dersom spiller har færre liv en det man startet med vil man få tilbake et liv hvert 10. poeng man får.
            self.player.health += 1
            self.last_health_increase_score = self.score

    def draw_health(self):  # Tegner hjertene til spilleren.
        full_heart = utils.load_and_scale_image("assets/images/full_heart.png",
                                                st.HEART_SIZE[0], st.HEART_SIZE[1])
        empty_heart = utils.load_and_scale_image("assets/images/empty_heart.png",
                                                 st.HEART_SIZE[0], st.HEART_SIZE[1])

        for i in range(st.PLAYER_START_HEALTH):
            self.window.blit(empty_heart, (i * st.HEART_POS[0], st.HEART_POS[1]))
            for l in range(self.player.health):
                self.window.blit(full_heart, (l * st.HEART_POS[0], st.HEART_POS[1]))

    def draw_end_screen(self):  # Tegner sluttskjermen.
        if self.player.health <= 0:
            you_died = utils.load_and_scale_image("assets/images/you_died.png", st.YOU_DIED_SIZE[0],
                                                  st.YOU_DIED_SIZE[1])
            try_again = utils.load_and_scale_image("assets/images/try_again.png", st.TRY_AGAIN_SIZE[0],
                                                   st.TRY_AGAIN_SIZE[1])

            self.window.blit(you_died, (0, (st.WINDOW_SIZE[1] - st.YOU_DIED_SIZE[1]) / 2))
            self.window.blit(try_again, ((st.WINDOW_SIZE[0] - st.TRY_AGAIN_SIZE[0]) / 2,
                                         st.WINDOW_SIZE[1] - (3 * st.TRY_AGAIN_SIZE[1])))

    def draw_score(self):
        font = pygame.font.Font('freesansbold.ttf', 40)
        str_score = font.render(str(self.score), False, (10, 230, 10))
        self.window.blit(str_score, (st.WINDOW_SIZE[0] - 100, 10))

    def restart(self):  # Starter hele spillet på nytt dersom man trykker på "enter" knappen.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.player.restart()
            self.enemy.restart()
            self.player.health = st.PLAYER_START_HEALTH
            self.score = 0

    def run(self):
        self.load_map()
        while self.running:  # Dette er "game-loopen". Den går så lenge self.running == True.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Sjekk om brukeren trykker på "lukk"-knappen
                    self.running = False
            self.draw()  # Tegn spillet i hver iterasjon av løkken
            self.movement()  # Oppdaterer bevegelser i spillet
            self.clock.tick(st.FPS)  # Begrenser spillhastigheten til 60 FPS
            self.restart()  # Sjekker om brukeren trykker "enter"
        pygame.quit()


if __name__ == "__main__":  # Starter spillet dersom man kjører programmet
    game = Game()
    game.run()
