import matplotlib.pyplot as plt
import time
from grille import Grille

s1 =[
    [0,8,0,0,3,0,0,7,0],
    [0,1,0,7,0,4,8,0,5],
    [7,3,0,5,0,8,2,0,0],
    [0,2,0,8,7,1,0,4,3],
    [8,0,1,0,0,0,0,0,7],
    [4,0,0,0,0,0,0,9,8],
    [5,0,8,0,0,0,0,1,0],
    [0,4,0,0,0,5,0,0,6],
    [1,0,7,0,8,3,4,5,2]]

s2 =[
    [0,6,0,0,0,0,0,0,9],
    [0,0,0,0,0,0,5,8,2],
    [4,0,3,2,9,0,0,6,0],
    [3,0,5,9,0,0,7,1,0],
    [8,0,6,1,0,0,0,9,3],
    [0,2,1,3,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [2,0,0,8,0,1,0,7,4],
    [7,0,4,5,0,0,8,0,6]]

s3 =[
    [7,0,0,4,0,0,0,0,5],
    [8,6,0,7,0,0,0,0,0],
    [3,0,0,9,0,2,0,0,0],
    [0,0,0,3,0,0,0,8,1],
    [1,0,9,0,0,0,6,3,2],
    [0,4,0,8,1,6,0,5,0],
    [9,3,0,2,8,5,7,0,0],
    [5,0,0,0,4,7,1,0,0],
    [4,0,0,0,0,0,0,0,0]]

s4 =[
    [0,4,9,2,0,0,8,0,0],
    [0,0,0,0,3,1,0,6,0],
    [0,8,0,4,7,9,0,0,0],
    [0,6,1,0,0,0,0,0,0],
    [5,3,0,9,0,0,0,0,4],
    [8,0,4,1,0,0,3,0,0],
    [0,0,7,0,0,0,0,0,0],
    [0,0,8,6,2,5,0,7,0],
    [6,5,3,0,0,0,9,2,0]]

s5 =[
    [0,0,3,0,6,0,7,0,4],
    [0,0,8,0,0,0,0,9,0],
    [0,6,0,5,7,0,0,1,0],
    [8,4,2,0,0,7,0,6,1],
    [9,0,0,0,2,0,3,0,0],
    [5,3,1,0,9,4,2,0,0],
    [0,0,0,0,0,6,4,0,0],
    [0,0,0,0,0,0,0,5,7],
    [0,0,0,0,1,0,0,8,2]]

s6 =[
    [6,3,0,8,0,0,0,0,0],
    [0,0,0,3,9,0,0,1,0],
    [1,0,0,0,0,0,9,0,2],
    [0,0,0,4,5,7,0,8,6],
    [0,4,0,0,0,0,2,0,0],
    [0,1,6,2,0,0,3,0,7],
    [9,0,0,0,0,6,8,0,0],
    [0,8,5,9,7,2,4,0,1],
    [0,0,0,0,3,0,0,5,0]]

s7 =[
    [7,0,0,0,0,0,0,0,0],
    [3,0,4,0,8,0,0,0,0],
    [0,0,9,0,7,0,2,8,0],
    [0,0,8,0,4,0,5,7,0],
    [0,0,0,9,0,0,0,6,0],
    [0,9,0,8,0,6,3,2,1],
    [5,0,6,2,0,0,1,9,4],
    [0,4,0,0,0,1,0,0,0],
    [0,2,1,5,0,0,7,3,6]]

s8 =[
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,1,2,0,3,6,0],
    [0,2,0,6,4,3,0,0,0],
    [0,0,0,0,0,6,0,0,3],
    [0,5,7,9,0,2,4,8,0],
    [0,8,4,0,0,1,0,0,9],
    [0,4,0,0,0,0,0,0,0],
    [5,0,9,7,6,0,0,0,8],
    [0,0,2,3,9,5,7,1,0]]

s9 =[
    [7,0,3,1,9,6,0,5,0],
    [0,1,0,7,0,0,8,6,0],
    [0,2,0,0,0,0,0,0,0],
    [1,0,7,8,2,0,0,0,0],
    [0,0,0,4,6,0,3,0,7],
    [0,4,0,9,0,5,6,1,8],
    [9,5,0,2,0,0,0,0,0],
    [8,0,0,0,0,0,0,0,0],
    [2,0,0,0,0,0,9,3,4]]

s10 =[
    [0,1,0,0,7,0,0,3,8],
    [3,0,7,0,0,6,0,0,0],
    [0,5,2,0,0,8,0,9,0],
    [0,0,9,8,1,2,4,6,0],
    [2,0,0,0,0,0,0,7,5],
    [0,0,0,0,0,0,0,1,0],
    [0,0,0,3,4,0,0,8,0],
    [6,9,0,5,0,0,7,0,4],
    [0,0,0,0,0,0,3,0,1]]

s11 =[
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,6,2,8,7,0,0],
    [0,0,0,0,0,0,0,9,3],
    [2,0,1,0,0,0,0,0,0],
    [7,0,8,4,0,0,0,0,9],
    [0,0,0,9,7,1,2,0,0],
    [0,0,0,0,0,0,0,0,7],
    [8,0,7,2,9,0,0,0,4],
    [4,3,0,8,5,0,0,0,0]]

s12 =[
    [5,0,0,0,0,1,0,0,6],
    [0,0,0,0,0,0,3,0,2],
    [0,0,4,5,0,0,0,0,0],
    [0,8,3,0,0,0,0,0,0],
    [6,7,0,0,1,0,4,0,0],
    [0,2,0,0,8,0,0,0,0],
    [0,0,0,3,5,7,0,0,0],
    [0,0,9,4,2,0,8,0,0],
    [0,0,0,0,0,0,0,0,7]]

s13 =[
    [0,0,0,0,7,3,0,0,5],
    [1,0,0,0,0,0,0,0,0],
    [0,0,0,0,9,8,4,0,0],
    [0,0,5,0,0,4,6,0,7],
    [0,0,0,8,0,0,0,0,0],
    [0,0,2,0,0,0,9,0,3],
    [0,0,3,0,0,5,0,6,2],
    [0,9,0,0,0,0,0,0,0],
    [4,0,1,0,0,0,0,3,0]]

s14 =[
    [3,8,0,0,0,7,0,0,0],
    [0,0,0,0,0,3,6,9,2],
    [0,0,6,9,0,0,7,0,0],
    [0,0,3,1,6,0,0,4,0],
    [0,0,0,0,0,5,8,7,0],
    [0,4,0,0,0,0,5,0,0],
    [0,3,0,0,0,0,0,0,0],
    [0,0,9,0,0,0,0,0,6],
    [1,0,5,2,4,0,0,0,0]]

s15 =[
    [1,0,0,9,2,5,0,0,0],
    [0,0,0,0,0,0,0,9,0],
    [0,0,8,0,0,3,5,0,0],
    [0,0,0,0,1,0,0,0,2],
    [3,8,0,0,0,4,0,0,0],
    [0,0,0,7,0,0,1,0,9],
    [0,0,7,1,0,9,4,0,0],
    [0,0,6,0,0,0,0,0,0],
    [0,5,0,6,4,0,0,3,0]]

s16 =[
    [0,2,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,6,7,0],
    [7,6,4,0,0,0,5,9,2],
    [8,0,0,0,0,6,0,0,0],
    [0,7,0,0,0,0,0,0,6],
    [1,5,0,0,4,9,0,0,8],
    [9,0,0,0,0,0,4,0,7],
    [4,0,0,0,0,0,0,0,0],
    [0,0,0,3,8,0,0,0,0]]
s17 =[
    [7,0,8,0,6,0,0,0,0],
    [0,3,0,5,0,0,0,7,0],
    [0,0,0,0,0,0,0,4,1],
    [0,0,3,7,0,0,2,1,0],
    [8,0,0,0,0,9,3,0,0],
    [9,0,4,1,0,0,7,5,0],
    [1,0,5,0,0,0,4,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,7,4,2,0,1,0,0]]

s18 =[
    [0,0,0,0,9,2,0,0,0],
    [0,0,4,3,0,5,0,8,0],
    [0,8,0,0,0,0,0,0,6],
    [0,0,0,0,0,0,0,0,0],
    [0,0,7,0,0,0,0,6,0],
    [3,0,0,0,0,4,1,7,0],
    [0,9,0,0,0,6,7,0,0],
    [0,5,0,0,0,0,0,3,1],
    [0,0,1,9,4,0,0,0,0]]
s19 =[
    [0,0,0,6,1,0,0,0,3],
    [5,8,0,0,0,0,6,7,0],
    [1,0,0,0,0,0,0,0,0],
    [0,0,0,0,3,9,0,0,0],
    [0,0,0,0,0,0,0,1,0],
    [4,1,0,0,0,0,0,8,0],
    [0,0,4,0,0,6,0,0,0],
    [0,0,0,2,0,7,0,9,6],
    [0,0,9,0,0,0,5,0,0]]
s20 =[
    [0,0,0,0,9,0,0,2,0],
    [0,0,0,0,0,0,0,0,0],
    [4,0,3,0,1,0,5,0,0],
    [1,0,0,0,0,6,0,5,0],
    [9,5,0,3,8,0,4,0,0],
    [0,6,0,0,0,0,8,0,0],
    [0,1,0,0,2,7,0,0,0],
    [0,0,0,0,0,0,3,4,2],
    [0,0,0,0,0,0,9,0,0]]


resultats = []
sudokus = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20]
nbsolution = []
for sudoku in sudokus:

    debut_temps = time.time()
    # Essaye de compléter le sudoku et mesure le temps.
    reussite, sudoku_termine = Grille(9).completer_sudoku(sudoku)

    fin_temps = time.time()
    temps_ecoule = (fin_temps - debut_temps) * 1000  # Convertir en millisecondes
    nbsolution.append(Grille(9).comptage_des_solution(sudoku))
    if reussite:
        resultats.append(temps_ecoule)

print(nbsolution)
plt.plot(resultats, '+')
plt.show()