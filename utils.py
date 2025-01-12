"""
Dungeon Brawler

Opprettet av: Frithjof Nilsen
Dato: 12.01.2025


Dette er en funksjon som laster inn og skalerer bilder.
Den brukes i både main.py og player.py.
Derfor var det best å ha funksjonen i en annen fil slik at man slipper å ha identiske funksjoner i begge filene.
Dersom man skal utvide spillet, og ha flere felles funksjoner, kan man også legge de her.


For ytteligere forklaring av spillet og koden, se READ_ME.md
"""

# Importerer filene til prosjektet
import pygame


def load_and_scale_image(path, width, height):
    image = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(image, (width, height))
