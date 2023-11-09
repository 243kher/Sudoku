import grille

def test_creation_grille():
    sudoku = grille.Grille(9)
    sudoku.creer_tableau()
    assert sudoku.tableau == [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0] ]

def test_validation_sudoku():
    sudoku_valide = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]]

    sudoku_invalide = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 7]]  # La dernière ligne contient deux 7
        
    sudoku = grille.Grille(9)
    assert sudoku.est_sudoku(sudoku_valide) == True
    assert sudoku.est_sudoku(sudoku_invalide)==False 
        
def test_completer_sudoku():
    sudoku = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    assert sudoku.completer_sudoku(sudoku)==[[5, 3, 4, 6, 7, 8, 9, 1, 2],
                                             [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                             [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                             [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                             [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                             [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                             [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                             [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                             [3, 4, 5, 2, 8, 6, 1, 7, 9]]

def test_creer_sudoku():
    sudoku = grille.Grille(9)
    sudoku_genere = sudoku.creer_sudoku()
    print("Sudoku généré",sudoku_genere)

def test_tableau_case_vides():
    sudoku = grille.Grille(9)
    tableau = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    
    cases_vides = sudoku.tableau_case_vides(tableau)
    assert cases_vides == [(0, 2), (0, 3), (0, 5), (0, 6), (0, 7), (0, 8), (1, 1), (1, 2), (1, 6), (1, 7), (1, 8), (2, 0), (2, 3), (2, 4), (2, 5), (2, 6), (2, 8), (3, 1), (3, 2), (3, 3), (3, 5), (3, 6), (3, 7), (4, 1), (4, 2), (4, 4), (4, 6), (4, 7), (5, 1), (5, 2), (5, 3), (5, 5), (5, 6), (5, 7), (6, 0), (6, 2), (6, 3), (6, 4), (6, 5), (6, 8), (7, 0), (7, 1), (7, 2), (7, 6), (7, 7), (8, 0), (8, 1), (8, 2), (8, 3), (8, 5), (8, 6)]



def test_choix_possibles():
    sudoku = grille.Grille(9)
    tableau = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    
    cases_vides = sudoku.tableau_case_vides(tableau)
    x, y = cases_vides[1]
    valeurs_possibles = sudoku.choix_possibles(tableau, x, y)
    assert valeurs_possibles == [2, 6]



if __name__ == "__main__":
    test_creation_grille()
    test_validation_sudoku()
    test_completer_sudoku()
    test_creer_sudoku()
    test_tableau_case_vides()
    test_choix_possibles()
