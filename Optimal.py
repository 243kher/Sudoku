# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 09:23:54 2023

@author: aya24
"""

from  Grille import Grille
import time 

class Optimal:
    def __init__(self, type_sudoku):
        self.type_sudoku = type_sudoku
        
    def chiffres_min(self):
        grille = Grille(self.type_sudoku)
        continuer = True
        minimum = self.type_sudoku**2
        while continuer :
            tableau= grille.creer_sudoku()
            n = len(grille.tableau_case_vides(tableau))
            if n < minimum:
                minimum = n 
            arreter = input("Arreter")
            if arreter == 'oui':
                continuer = False
                
        return f"Le nombre minimal moyen de valeurs d'un sudoku nouveau est de {minimum}"
            
    def temps_generer_sudoku(self):
        grille = Grille(self.type_sudoku)
        continuer = True
        minimum = time.time()
        while continuer :
            temps_a = time.time()
            tableau= grille.creer_sudoku()
            temps_b = time.time()
            n = temps_b -  temps_a
            if n < minimum:
                minimum = n 
            arreter = input("Arreter")
            if arreter == 'oui':
                continuer = False
            print(minimum)
        return f"Le temps minimal moyen pour generer un sudoku nouveau est de {minimum}secondes"


    def temps_completer_sudoku(self):
        grille = Grille(self.type_sudoku)
        continuer = True
        temps_a = time.time()
        tableau= grille.creer_sudoku_complet()
        temps_b = time.time()
        n = temps_b -  temps_a
            
        return f"Le temps pour completer un sudoku vide est de {n} secondes"

n= Optimal(9)
print(n.temps_completer_sudoku())

