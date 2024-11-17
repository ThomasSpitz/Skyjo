"""Jeu de Skyjo
"""

##########

import random as rd
import pygame
from pygame.locals import *

import affichages
import jeu

##########

NBR_PLAYER = 2
NBR_BOT = 0

##########

def main():
    game = jeu.Jeu(NBR_PLAYER,NBR_BOT)

if __name__ == '__main__': main()