from fiabilipy import *
import pylab as p

timerange = range(0, 24*365*5, 100)

P1 = Component('P1', 2.28e-4)
pros = Voter(P1, 2, 3)

M1 = Component('M1', 2.94e-4)
M2 = Component('M2', 2.94e-4)

Bus = Component('Bus', 1e-4)

Alim1 = Component('Alim', 2.28e-4)
Alim2 = Component('Alim', 2.28e-4)
Alim3 = Component('Alim', 2.28e-4)
Alim4 = Component('Alim', 2.28e-4)
Alim5 = Component('Alim', 2.28e-4)
Alim6 = Component('Alim', 2.28e-4)

# Système 
S = System()
S['E'] = [Alim1, Alim3, Alim5]
S[Alim1] = Alim2 
S[Alim2]= [pros]

S[Alim3] = Alim4
S[Alim4] = [pros]

S[Alim5] = Alim6
S[Alim6] = [pros]

S[pros] = [M1, M2]

S[M1] = S[M2] = [Bus]

S[Bus] = 'S'

import os
# ecrire les resultats dans un fichier
if not os.path.exists('resultats'):
    os.makedirs('resultats')

with open('resultats/architecture 3.txt', 'w') as f:
    f.write("Pour t = 100000000000\n")
    f.write("Disponibilité : " + str(S.availability(100000000000)) + "\n")

availability = [S.availability(t) for t in timerange]

# Architecture 1 avec un taux de reparation
p.plot(timerange, availability, color="#1f77b4", label="Disponibilité") # bleu

p.xlabel('Temps (heures)')
p.ylabel('Disponibilité')

p.legend()
p.show()

