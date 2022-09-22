from typing import List

def charger_fichier(nom_fichier:str) -> List[List[bool]]:
    """Charge le fichier et renvoie le jeu correspondant"""
    pass
    #Vérifier que toutes les lignes font la bonne taille

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
            n = compte_voisins(jeu,i,j)
            if n == 2:
                cell = jeu[i][j]
            elif n == 3:
                cell = True 
            else:
                cell = False
            jeu_apres[i].append(cell)
    return jeu_apres
