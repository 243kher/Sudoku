import random
import copy

class Grille :
    def __init__(self, nb_cases):
        self.nb_cases = nb_cases
        self.tableau =  []

    def creer_tableau(self):
        self.tableau =  [[0 for t in range(self.nb_cases)] for i in range(self.nb_cases)]

    def __str__(self):
        """
        Fonction qui renvoie le sudoku en forme de str

        Returns:
            str: sudoku 
        """
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

    def tableau_case_vides(self, tableau):
        """
        Fonction qui renvoie une liste des tuples correspondant aux coordonnées des cases vides dans le tableau.

        Args:
            tableau (list): Le tableau de Sudoku.

        Returns:
            list: Liste des tuples (x, y) correspondant aux coordonnées des cases vides.
        """
        
        liste = []
        for t in range(len(tableau)):
            for k in range(len(tableau)):
                if tableau[t][k] == 0:
                    liste.append((t, k))
        return liste

    def tableau_case_non_vides(self, tableau):
        """
        Fonction qui renvoie une liste des tuples correspondant aux coordonnées des cases non vides dans le tableau.

        Args:
            tableau (list): Le tableau de Sudoku.

        Returns:
            list: Liste des tuples (x, y) correspondant aux coordonnées des cases non vides.
        """
        
        liste = []
        for t in range(len(tableau)):
            for k in range(len(tableau)):
                if not tableau[t][k] == 0:
                    liste.append((t, k))
        return liste


    def choix_possibles(self, tableau, x, y):
        """
        Retourne une liste de valeurs possibles pour la case (x, y).

        Args:
            tableau (list): Le tableau de Sudoku.
            x (int): Coordonnée x de la case.
            y (int): Coordonnée y de la case.

        Returns:
            list: Liste des valeurs possibles pour la case (x, y).
        """


        # Ensemble de toutes les valeurs possibles dans un Sudoku
        valeurs_possibles = set(range(1, self.nb_cases + 1))

        # Ensemble des valeurs présentes dans la même ligne que la case (x, y)
        valeurs_ligne = {tableau[x][j] for j in range(self.nb_cases)}

        # Ensemble des valeurs présentes dans la même colonne que la case (x, y)
        valeurs_colonne = {tableau[i][y] for i in range(self.nb_cases)}

        # Ensemble des valeurs présentes dans la même région que la case (x, y)
        valeurs_region = {tableau[i][j] for i,j in self.indices_region(x,y)}

        # Exclusion des valeurs déjà présentes de l'ensemble des valeurs possibles
        valeurs_possibles -= valeurs_ligne | valeurs_colonne | valeurs_region

        return list(valeurs_possibles)

    def selectionner_case(self, tableau):

        """
        Retourne la prochaine case à remplir dans le tableau de Sudoku.

        Args:
            tableau (list): Le tableau de Sudoku.

        Returns:
            tuple: Coordonnées (x, y) de la case à remplir suivante, ou None si toutes les cases sont remplies.

        Description:
            Cette méthode identifie la case vide à remplir suivante dans le tableau de Sudoku.
            Elle utilise la méthode `tableau_case_vides` pour obtenir une liste de toutes les cases vides.
            Si aucune case vide n'est trouvée, la méthode renvoie None pour indiquer que toutes les cases sont remplies.
            Sinon, la méthode utilise la fonction `min` avec une fonction lambda pour déterminer la case vide ayant le moins d'options possibles.
            La fonction lambda renvoie la longueur de la liste des choix possibles pour chaque case vide, et `min` renvoie la case vide correspondante.
        """

        cases_vides = self.tableau_case_vides(tableau)
        if len(cases_vides) == 0:
            return None

        return min(cases_vides, key=lambda case: len(self.choix_possibles(tableau, case[0], case[1])))

    def ajouter_valeur(self, tableau, nb_ajouter, x, y):
        """
        Fonction qui ajoute une valeur donnée aux coordonnées spécifiées du tableau.

        Args:
            tableau (list): Le tableau de Sudoku.
            nb_ajouter (int): La valeur à ajouter.
            x (int): La coordonnée x de la case.
            y (int): La coordonnée y de la case.
        """

        tableau[x][y] = nb_ajouter

    def completer_sudoku(self, tableau):
        """
        Vérifie s'il est possible de compléter le Sudoku et retourne le tableau completé.

        Args:
            tableau (list): Le tableau de Sudoku à compléter.

        Returns:
            tuple: Un tuple (booléen, tableau) indiquant si le Sudoku a été complété avec succès et le tableau completé.

        Description:
            Cette méthode vérifie s'il est possible de compléter le Sudoku en utilisant une approche récursive.
            Elle utilise une fonction interne `completer` pour effectuer la vérification récursive.
            Si le Sudoku peut être complété, la méthode renvoie True et le tableau completé.
            Sinon, elle renvoie False et le tableau partiellement rempli.
        """


        def completer(tableau):
            """
            Fonction récursive interne pour compléter le Sudoku.

            Args:
                tableau (list): Le tableau de Sudoku à compléter.

            Returns:
                bool: True si le Sudoku a été complété avec succès, False sinon.
            """
            if not self.tableau_case_vides(tableau):
                return True
            else:
                x, y = self.selectionner_case(tableau)
            for t in self.choix_possibles(tableau, x, y):
                self.ajouter_valeur(tableau, t, x, y)
                if completer(tableau):
                    return True
                self.ajouter_valeur(tableau, 0, x, y)
            return False

        nouveau_tableau = copy.deepcopy(tableau)

        if completer(nouveau_tableau):
            return True, nouveau_tableau
        else:
            return False, nouveau_tableau


    def creer_sudoku_complet(self):
        """
        Fonction qui retourne un tableau de Sudoku complet.

        Returns:
            tableau (list): Tableau de Sudoku généré complété.

        Description:
            Cette méthode génère un tableau de Sudoku.
            Le tableau est généré en remplissant certaines cases avec des valeurs aléatoires et en vérifiant si le Sudoku peut être complété.
            Si le Sudoku est impossible à compléter, les valeurs des cases précédemment remplies sont réinitialisées à zéro.
        """

        tableau = [[0 for _ in range(self.nb_cases)] for _ in range(self.nb_cases)]  # Crée un tableau vide

        # Remplissage du tableau avec des valeurs aléatoires
        while not self.tableau_case_vides(tableau) == []:
            x , y = random.randint(0,self.nb_cases-1),random.randint(0,self.nb_cases-1) # Sélectionne une case aléatoire
            if tableau[x][y] == 0: # Vérifie si la case est vide
                tableau[x][y] = random.choice(self.choix_possibles(tableau, x, y)) # Remplit la case avec une valeur aléatoire parmi les choix possibles
                if not self.completer_sudoku(tableau)[0]:# Vérifie si le Sudoku peut être complété
                    tableau[x][y] = 0
                    
        return tableau

    def creer_sudoku(self):
        """
        Fonction qui retourne un tableau de Sudoku.

        Returns:
            tableau (list): Tableau de Sudoku généré.

        Description:
            Cette méthode génère un tableau de Sudoku avec une seule solution.
            A partir d'un sudoku complet genere par la methode creer_sudoku_complet(). 
            Les cases vont etre vidées, jusqu'a que le sudoku n'ait qu'une seul solution.
        """


        tableau = self.creer_sudoku_complet()  # Crée un tableau complet de Sudoku
        cases_non_vides=self.tableau_case_non_vides(tableau)
        x, y= random.choice(cases_non_vides)
        tableau[x][y] = 0
        cases_non_vides.remove((x,y))
        
        while self.comptage_des_solution(tableau) == 1:
            x, y= random.choice(cases_non_vides)
            nb=tableau[x][y]
            tableau[x][y] = 0
            cases_non_vides.remove((x,y))
        tableau[x][y]=nb
        return tableau
    
        
    def comptage_des_solution(self, tableau):
        """
        Fonction qui compte le nombre de solution d'un sudoku.

        Args:
            tableau (list): Tableau de Sudoku.

        Returns:
            comptage (int): Nombre de solutions

        Description:
            Cette méthode compte de maniere recursif le nombre de solution que un sudoku incomplet pourrait avoir.
        """
        if not self.completer_sudoku(tableau)[0]:
            return 0
        if len(self.tableau_case_vides(tableau)) == 0:
            return 1        
        x,y = self.tableau_case_vides(tableau)[0]
        comptage = 0
        for valeur in self.choix_possibles(tableau, x, y):
            tableau[x][y] = valeur 
            result = self.comptage_des_solution(tableau)
            comptage = comptage + result
            tableau[x][y] = 0
        return comptage
    

 
