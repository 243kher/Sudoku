# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 18:27:18 2023

@author: aya24
"""

import tkinter as tk
from tkinter import messagebox
from Grille import Grille

class SudokuGUI:
    def __init__(self, interface):
        self.interface = interface
        self.interface.title("Sudoku")
        self.dimension = tk.IntVar()
        self.sudoku_jeu = None
        self.fenetre = None
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self.interface, text="Sélectionnez la taille du Sudoku :")
        label.pack(pady=10)

        bouton_4x4 = tk.Button(self.interface, text="Jeu 4x4", command=lambda: self.demarrer_jeu(4))
        bouton_4x4.pack(pady=5)

        bouton_9x9 = tk.Button(self.interface, text="Jeu 9x9", command=lambda: self.demarrer_jeu(9))
        bouton_9x9.pack(pady=5)

    def demarrer_jeu(self, dimension):
        self.dimension.set(dimension)
        if self.fenetre:
            self.fenetre.destroy()

        self.fenetre = tk.Toplevel(self.interface)
        self.fenetre.title("Sudoku")

        self.sudoku_jeu = Grille(self.dimension.get())
        sudoku_tableau = self.sudoku_jeu.creer_sudoku()

        for i in range(self.dimension.get()):
            for j in range(self.dimension.get()):
                entree = tk.Entry(self.fenetre, width=4, font=('Roboto', 16), justify='center')
                entree.grid(row=i, column=j)
                entree.insert(0, str(sudoku_tableau[i][j]))

        verifier_bouton = tk.Button(self.fenetre, text="Vérifier la solution", command=lambda: self.verifier_solution(sudoku_tableau))
        verifier_bouton.grid(row=self.dimension.get(), column=0, columnspan=self.dimension.get(), pady=10)

        resoudre_bouton = tk.Button(self.fenetre, text="Résoudre", command=lambda: self.solve_puzzle(sudoku_tableau))
        resoudre_bouton.grid(row=self.dimension.get() + 1, column=0, columnspan=self.dimension.get(), pady=10)

        nouveau_jeu_bouton = tk.Button(self.fenetre, text=f"Nouveau jeu {dimension}x{dimension}", command=lambda: self.demarrer_jeu(dimension))
        nouveau_jeu_bouton.grid(row=self.dimension.get() + 2, column=0, columnspan=self.dimension.get(), pady=10)

    def verifier_solution(self, tableau):
        tableau_final = [int(entree.get()) for entree in self.fenetre.winfo_children() if isinstance(entree, tk.Entry)]
        solution_utilisateur = [tableau_final[i:i + self.dimension.get()] for i in range(0, len(tableau_final), self.dimension.get())]
    
        if len(solution_utilisateur) != self.dimension.get():
            messagebox.showerror("Erreur", "Une solution existe déjà.")
            return
    
        if self.sudoku_jeu.est_sudoku(solution_utilisateur):
            messagebox.showinfo("Résultat", "C'est exact ! Vous avez résolu le Sudoku correctement.")
        else:
            messagebox.showerror("Résultat", "Il y a quelque chose qui ne va pas. Réessayez !")

    def solve_puzzle(self, tableau):
        tableau_resolu = self.sudoku_jeu.completer_sudoku(tableau)[1]

        for i, row in enumerate(tableau_resolu):
            for j, valeur in enumerate(row):
                entree = tk.Entry(self.fenetre, width=4, font=('Arial', 16), justify='center')
                entree.grid(row=i, column=j)
                entree.insert(0, str(valeur))
                entree.config(state='disabled')

if __name__ == "__main__":
    interface = tk.Tk()
    app = SudokuGUI(interface)
    interface.mainloop()
