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
    
    def (self):



t=Grille(4)
t.creer_tableau()
print(t)
