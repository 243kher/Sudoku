import grille

def test_creer_tableau():
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
                              [0, 0, 0, 0, 0, 0, 0, 0, 0]]
def test_verifie_liste():
    sudoku = grille.Grille(9)
    sudoku_a = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]]
    assert sudoku.verifie_liste(sudoku_a[0])==True

def test_indices_region():
    sudoku = grille.Grille(9)
    sudoku_b = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]]
    assert sudoku.indices_region(0,0)==[(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]



def test_est_sudoku():
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


def test_tableau_case_non_vides():
    sudoku = grille.Grille(9)
    tableau = [
        [5, 0, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 4, 0, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 0, 0]]

    cases_non_vides = sudoku.tableau_case_non_vides(tableau)
    assert cases_non_vides == [(0, 0), (0, 4), (1, 0), (1, 5), (2, 1), (2, 2), (2, 7), (3, 8), (4, 3), (4, 5), (4, 8), (5, 0), (5, 4), (6, 6), (7, 3), (7, 5), (7, 8), (8, 4)]






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

def test_selectionner_case():
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

    case_a_remplir = sudoku.selectionner_case(tableau)
    assert case_a_remplir == (4, 4)





def test_ajouter_valeur():
    sudoku = grille.Grille(9)
    sudoku_d = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 0, 7, 9]]
    sudoku.ajouter_valeur(sudoku_d, 1, 8, 6)
    assert sudoku_d==[[5, 3, 4, 6, 7, 8, 9, 1, 2],
                      [6, 7, 2, 1, 9, 5, 3, 4, 8],
                      [1, 9, 8, 3, 4, 2, 5, 6, 7],
                      [8, 5, 9, 7, 6, 1, 4, 2, 3],
                      [4, 2, 6, 8, 5, 3, 7, 9, 1],
                      [7, 1, 3, 9, 2, 4, 8, 5, 6],
                      [9, 6, 1, 5, 3, 7, 2, 8, 4],
                      [2, 8, 7, 4, 1, 9, 6, 3, 5],
                      [3, 4, 5, 2, 8, 6, 1, 7, 9]]



def test_completer_sudoku():
    s = grille.Grille(9)
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
    assert s.completer_sudoku(sudoku)==(True,[[5, 3, 4, 6, 7, 8, 9, 1, 2],
                                        [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                        [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                        [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                        [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                        [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                        [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                        [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                        [3, 4, 5, 2, 8, 6, 1, 7, 9]])


def test_creer_sudoku_complet():
    sudoku = grille.Grille(9)
    tableau = sudoku.creer_sudoku_complet()
    assert sudoku.est_sudoku(tableau) == True




def test_creer_sudoku():
    sudoku = grille.Grille(9)
    tableau = sudoku.creer_sudoku()
    assert sudoku.completer_sudoku(tableau)[0] == True



def test_comptage_des_solution():
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

    assert (sudoku.comptage_des_solution(tableau)) == 1
    sudoku = grille.Grille(4)
    t = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]]

    assert (sudoku.comptage_des_solution(t)) == 288







if __name__ == "__main__":
    test_creer_tableau()
    test_verifie_liste()
    test_indices_region()
    test_est_sudoku()
    test_tableau_case_vides()
    test_tableau_case_non_vides()
    test_choix_possibles()
    test_selectionner_case()
    test_ajouter_valeur()
    test_completer_sudoku()
    test_creer_sudoku_complet()
    test_creer_sudoku()
    test_comptage_des_solution()

