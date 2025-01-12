"""
Dungeon Brawler

Opprettet av: Frithjof Nilsen
Dato: 12.01.2025


settings.py bestemmer ulike konstanter i spillet.

For forklaring av spillet og koden, se READ_ME.md
"""

# Tall for oppbrettelse av vinduet
aspect_ratio = 16 / 9
WINDOW_SIZE = (int(600 * aspect_ratio), 600)

# Bestemmer hastigheten spillet kjøres på
FPS = 60

# Tall for å styre player
PLAYER_SIZE = (50, 80)
PLAYER_SPEED = 7
PLAYER_START_HEALTH = 5
IMMORTAL_TIME = 1000
HIT_SPEED = (15, -20)

# Bestemmer tall for bevegelse i y-retning
GRAVITY = 1.5
JUMP_STRENGTH = -20

# Tall for å styre enemy
ENEMY_SIZE = (62, 46)
ENEMY_SPEED = 3
SPAWN_DISTANCE_FROM_PLAYER = 200

# Tall for skalering og posisjonering av hjerter
HEART_SIZE = (50, 50)
HEART_POS = ((1.2 * HEART_SIZE[0]), 10)

# Tall for skalering av elementer på slutt-skjerm
YOU_DIED_SIZE = (WINDOW_SIZE[0], (346 / 1280) * WINDOW_SIZE[0])
TRY_AGAIN_SIZE = (400, (120 / 1162) * 400)

# Tall for skalering av tiles til backgrunnen
BACKGROUND_SIZE = (70, 79)

# Tall for skalering av tiles til bakken
GROUND_SIZE = (150, 50)

# Bestemmer bakkenivået
GROUND_LEVEL = WINDOW_SIZE[1] - GROUND_SIZE[1]
