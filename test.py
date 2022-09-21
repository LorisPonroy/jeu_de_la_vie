def test_tauto():
    assert(True)

def test_load_file():
    jeu = charger_fichier(example_petit.vie)
    jeu[0][0] = "."
    jeu[0][1] = "*"
    jeu[1][0] = "*"
    jeu[1][1] = "*"

def test_transition():
    jeu = charger_fichier(example_petit.vie)
    jeu2 = transition(jeu)
    jeu2[0][0] = "*"
    jeu2[0][1] = "*"
    jeu2[1][0] = "*"
    jeu2[1][1] = "*"
    jeu3 = transition(jeu2)
    jeu3[0][0] = "."
    jeu3[0][1] = "."
    jeu3[1][0] = "."
    jeu3[1][1] = "."
