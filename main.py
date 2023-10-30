#main

from random import *

class Grille :
    def __init__(self, nb_cases):
        self.nb_cases = nb_cases
        self.tableau =  []

    def creer_tableau(self):
        self.tableau =  [[0 for t in range(self.nb_cases)] for i in range(self.nb_cases)]

    def __str__(self):
        tableau = ""
        for t in range(self.nb_cases):
            tableau += "| "
            for k in range(self.nb_cases):
                tableau += str(self.tableau[t][k])+ " | "
            tableau += "\n"
            for k in range(self.nb_cases):
                tableau += "-"*self.nb_cases
            tableau += "\n"
        return tableau
    
    def verifie_liste(self, liste):
        """
        Fonction qui renvoie True s'il y a n chiffres, de 1 à n, dans la liste,
        sinon la fonction renvoie False.

        Args:
            liste (list): La liste à vérifier.

        Returns:
            bool: True si la liste contient les chiffres de 1 à n, False sinon.
        """

        n = 0
        for t in range(1, len(liste) + 1):
            if t in liste:
                n += 1
        return n == self.nb_cases
    
    def indices_region(self, i, j):
        """
        Renvoie les indices des cases dans la même région (3x3) que la case (i, j).

        Args:
            i (int): Coordonnée i de la case.
            j (int): Coordonnée j de la case.

        Returns:
            list: Liste des tuples (x, y) correspondant aux indices des cases dans la même région.
        """
        taille_region = int(self.nb_cases ** 0.5)
        region_i, region_j = i // taille_region, j // taille_region
        indices = []
        for x in range(region_i * taille_region, (region_i + 1) * taille_region):
            for y in range(region_j * taille_region, (region_j + 1) * taille_region):
                if (x, y) != (i, j):
                    indices.append((x, y))
        return indices
    
    def est_sudoku(self, tableau):

        """
        Fonction qui vérifie si un tableau donné est un Sudoku valide.

        Args:
            tableau (list): Le tableau à vérifier.

        Returns:
            bool: True si le tableau est un Sudoku valide, False sinon.
        """
        for ligne in tableau:
            assert isinstance(ligne, list), "Chaque ligne du tableau doit être une liste"
            assert len(ligne) == 9, "Chaque ligne du tableau doit contenir 9 éléments"

            assert all(isinstance(element, int) for element in ligne), "Chaque élément du tableau doit être un entier"

        # Vérification des lignes et des colonnes
        for t in range(len(tableau)):
            liste = []
            for k in range(len(tableau)):
                liste.append(tableau[k][t])
                if not self.verifie_liste(tableau[t]):
                    return False
            if not self.verifie_liste(liste):
                return False

        # Vérification des régions
        taille_region = int(self.nb_cases ** 0.5)
        for t in range(len(tableau)):
            liste=[tableau[taille_region * (t % taille_region)][taille_region * (t // taille_region)]]
            for l in range(len(tableau)-1):
                x,y=self.indices_region(taille_region * (t % taille_region),taille_region * (t // taille_region))[l]
                liste.append(tableau[x][y])
            if not self.verifie_liste(liste):
                return False

        return True



t=Grille(9)
t.creer_tableau()
#Exemple pour voir si ca marche
sudoku_valide = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]

t.est_sudoku(sudoku_valide)
print(t.est_sudoku(sudoku_valide))
