# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 09:23:54 2023

@author: aya24
"""

from  Grille import Grille
import time 

class Optimal:
    def __init__(self, nb_sudokus, taille_grille):
        self.nb_sudokus = nb_sudokus
        self.taille_grille = taille_grille
        self.sudokus = []

    def generer_sudoku(self):
        """
        Génère un sudoku incomplet et compte le nombre de valeurs.
        """
        grille = Grille(self.taille_grille)
        sudoku = grille.creer_sudoku()

        # Compte le nombre de valeurs dans un sudoku
        nb_valeurs = sum(rangee.count(0) for rangee in sudoku)

        return sudoku, nb_valeurs

    def generer_et_sauvegarder_sudokus(self, nom_fichier):
        """
        Génère et enregistre les sudokus dans un fichier trié par nombre de valeurs.
        """
        n=0
        for _ in range(self.nb_sudokus):
            n=n+1
            print(n)
            sudoku, nb_valeurs = self.generer_sudoku()
            self.sudokus.append((sudoku, nb_valeurs))

        # Trie les sudokus par nombre de valeurs
        self.sudokus.sort(key=lambda x: x[1])

        # Enregistre les sudokus dans le fichier
        with open(nom_fichier, 'w') as fichier:
            for sudoku, nb_valeurs in self.sudokus:
                fichier.write(f"Le nombre de valeurs est:{nb_valeurs}\n")
                for rangee in sudoku:
                    fichier.write(" ".join(map(str, rangee)) + "\n")
                fichier.write("\n")


    def completer_et_mesurer_temps(self, sudokus, nom_fichier):
        """
        Methode qui va effectuer les sudokus et mesurez le temps nécessaire dans chaque cas en millisecondes.
        Et enregistrer les résultats dans un fichier classé.
        """
        resultats = []

        for sudoku, nb_valeurs in sudokus:
            debut_temps = time.time()

            # Essaye de compléter le sudoku et mesure le temps.
            reussite, sudoku_termine = Grille(self.taille_grille).completer_sudoku(sudoku)

            fin_temps = time.time()
            temps_ecoule = (fin_temps - debut_temps) * 1000  # Convertir en millisecondes
            print(temps_ecoule)
            if reussite:
                resultats.append((sudoku_termine, temps_ecoule, nb_valeurs))


        # Enregistre les résultats dans le fichier
        with open(nom_fichier, 'w') as fichier:
            for sudoku_termine, temps_ecoule, nb_valeurs in resultats:
                fichier.write(f"Nb valeurs: {nb_valeurs}, Temps ecoule: {temps_ecoule:.2f} milliseconds\n")
                for rangee in sudoku_termine:
                    fichier.write(" ".join(map(str, rangee)) + "\n")
                fichier.write("\n")

if __name__ == "__main__":
    optimal = Optimal(nb_sudokus=30, taille_grille=9)
    optimal.generer_et_sauvegarder_sudokus("sudokus.txt")

    # Lee los sudokus generados
    with open("sudokus2.txt", 'r') as fichier:
        sudokus = []
        lignes = fichier.readlines()
        i = 0
        while i < len(lignes):
            nb_valeurs = int(lignes[i].split(":")[1].strip())
            sudoku = [list(map(int, lignes[j].split())) for j in range(i + 1, i + 10)]
            sudokus.append((sudoku, nb_valeurs))
            i += 11



    optimal.completer_et_mesurer_temps(sudokus, "resultats2.txt")

