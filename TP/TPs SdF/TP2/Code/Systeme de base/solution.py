from fiabilipy import *
import pylab as p

timerange = range(0, 24*365*5, 100)

P1 = Component('P1', 2.28e-4)
pros = Voter(P1, 2, 3)

Bus = Component('Bus', 1e-4)

M1 = Component('M1', 2.94e-4)
M2 = Component('M2', 2.94e-4)
M3 = Component('M3', 2.94e-4) # ajout d'une troisème mémoire

S = System()
S['E'] = [pros]

S[pros] = [M1, M2, M3]

S[M1] = S[M2] = S[M3] = [Bus]

S[Bus] = 'S'

import os
# ecrire les resultats dans un fichier
if not os.path.exists('resultats'):
    os.makedirs('resultats')

with open('resultats/sol.txt', 'w') as f:
    f.write("Pour t = 100000000000\n")
    f.write("Disponibilité : " + str(S.availability(100000000000)) + "\n")

availability = [S.availability(t) for t in timerange]

# Architecture 1 avec un taux de reparation
p.plot(timerange, availability, color="#1f77b4", label="Disponibilité") # bleu

p.xlabel('Temps (heures)')
p.ylabel('Disponibilité')

p.legend()
p.show()
