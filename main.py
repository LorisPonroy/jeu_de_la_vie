from typing import List

def charger_fichier(nom_fichier:str) -> List[List[bool]]:
    """Charge le fichier et renvoie le jeu correspondant"""
    fichier = open(nom_fichier)
    nb_lignes, nb_colonnes = fichier.readline().split(" ")
    nb_lignes = int(nb_lignes)
    nb_colonnes = int(nb_colonnes)
    jeu = []
    for i in range(nb_lignes):
        line = fichier.readline()
        jeu.append([False if c == "." else True for c in line[:nb_colonnes]])
    return jeu
    #Vérifier que toutes les lignes font la bonne taille

def string_from_jeu(jeu : List[List[bool]]) -> str:
    s = ""
    for i in range(len(jeu)):
        for j in range(len(jeu[0])):
            if jeu[i][j]:
                s += "*"
            else:
                s += "."
        s+= "\n"
    return s

def sauvegarder_fichier(nom_fichier:str, jeu: List[List[bool]]) -> None:
    """Sauvegarde le jeu dans un fichier dans le dossier sauvegarde"""
    fichier = open(nom_fichier, "w")
    fichier.write(string_from_jeu(jeu))

def compte_voisins(jeu : List[List[bool]], x, y) -> int:
    """Donne le nombre de voisins de la cellule x,y dans le jeu"""
    nb_voisins = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if 0 <= x+i < len(jeu) and 0 <= y+j < len(jeu[0]):
                if (i!=0 or j!= 0) and jeu[x+i][y+j]:
                    nb_voisins += 1
    return nb_voisins

def transition(jeu : List[List[bool]]) -> List[List[bool]]:
    """Renvoie le jeu après une transition"""
    jeu_apres = []
    for i in range(len(jeu)):
        jeu_apres.append([])
        for j in range(len(jeu[0])):
            # Selon le nombre de voisins la cellule est:
            n = compte_voisins(jeu,i,j)
            if n == 2:
                cell = jeu[i][j]    # maintenu dans son état précédent, ou bien,
            elif n == 3:
                cell = True         # vivante, ou bien,
            else:
                cell = False        # en vie
            jeu_apres[i].append(cell)
    return jeu_apres

if __name__=="__main__":
    jeu = charger_fichier("example_petit.vie")
    print(string_from_jeu(jeu))
    jeu = transition(jeu)
    print(string_from_jeu(jeu))
    sauvegarder_fichier("sauvegarde/example_petit2.vie", jeu)

