from typing import List
from main import *

def test_tauto():
    assert(True)

example_jeu1 = [[False,True],[True,True]]
example_jeu2 = [[True,False],[True,False]]

def test_load_file():
    jeu = charger_fichier("example_petit.vie")
    jeu[0][0] = False
    jeu[0][1] = True
    jeu[1][0] = True
    jeu[1][1] = True

def test_compte_voisins():
    compte_voisins(example_jeu1,0,0) == 3
    compte_voisins(example_jeu1,0,1) == 2
    compte_voisins(example_jeu1,1,0) == 2
    compte_voisins(example_jeu1,1,1) == 2
    compte_voisins(example_jeu1,0,0) == 1
    compte_voisins(example_jeu1,0,1) == 2
    compte_voisins(example_jeu1,1,0) == 1
    compte_voisins(example_jeu1,1,1) == 2

def test_transition():
    jeu2 = transition(example_jeu1)
    jeu2[0][0] = True
    jeu2[0][1] = True
    jeu2[1][0] = True
    jeu2[1][1] = True
    jeu3 = transition(jeu2)
    jeu3 == jeu2
    jeu2 = transition(example_jeu2)
    jeu2[0][0] = False
    jeu3[0][0] = False
    jeu3[0][0] = False
    jeu3[0][0] = False

def test_plus_large():
    jeu = [[True,False,False],[True, True, False]]
    jeu2 = transition(jeu)
    jeu2 == [[True,True,False],[True,True,False]]
    