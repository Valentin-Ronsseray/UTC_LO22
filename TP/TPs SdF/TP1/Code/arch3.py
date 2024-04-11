from fiabilipy import *
import pylab as p

# Architecture 3
HBA1 = Component('HBA1', 1.25e-6, 7e-3)
HBA2 = Component('HBA2', 1.25e-6, 7e-3)

LinkA = Component('LinkA', 2.52e-6, 3e-3)
LinkB = Component('LinkB', 2.52e-6, 3e-3)

Concentrateur1 = Component('Concentrateur1', 1.71e-6, 2e-3)
Concentrateur2 = Component('Concentrateur2', 1.71e-6, 2e-3)

LinkC = Component('LinkC', 2.52e-6, 3e-3)
LinkD = Component('LinkD', 2.52e-6, 3e-3)

Disque1 = Component('Disque1', 1e-5, 5e-4)
Disque2 = Component('Disque2', 1e-5, 5e-4)

S = System()
S['E'] = [HBA1, HBA2]

S[HBA1] = [LinkA]
S[HBA2] = [LinkB]

S[LinkA] = [Concentrateur1, Concentrateur2]
S[Concentrateur1] = [LinkC, LinkD]

S[LinkB] = [Concentrateur1, Concentrateur2]
S[Concentrateur2] = [LinkC, LinkD]

S[LinkC] = [Disque1]
S[LinkD] = [Disque2]

S[Disque1] = S[Disque2] = 'S'

timerange = range(0, 24*365*2, 100)

import os
# ecrire les resultats dans un fichier
if not os.path.exists('resultats'):
    os.makedirs('resultats')

with open('resultats/arch3.txt', 'w') as f:
    f.write("Avec taux de reparation\n")
    f.write("Disponibilité : " + str(S.availability(100000000000)) + "\n")

print(S.availability(100000000000))