from fiabilipy import *
import pylab as p

# Architecture 2 avec taux de reparation
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

S[HBA1] = LinkA
S[HBA2] = LinkB

S[LinkA] = [Concentrateur1]
S[Concentrateur1] = [LinkC]

S[LinkB] = [Concentrateur2]
S[Concentrateur2] = [LinkD]

S[LinkC] = [Disque1]
S[LinkD] = [Disque2]

S[Disque1] = S[Disque2] = 'S'

# Architecture 2 sans taux de reparation
HBA1_ = Component('HBA1', 1.25e-6)
HBA2_ = Component('HBA2', 1.25e-6)

LinkA_ = Component('LinkA', 2.52e-6)
LinkB_ = Component('LinkB', 2.52e-6)

Concentrateur1_ = Component('Concentrateur1', 1.71e-6)
Concentrateur2_ = Component('Concentrateur2', 1.71e-6)

LinkC_ = Component('LinkC', 2.52e-6)
LinkD_ = Component('LinkD', 2.52e-6)

Disque1_ = Component('Disque1', 1e-5)
Disque2_ = Component('Disque2', 1e-5)

S_ = System()
S_['E'] = [HBA1_, HBA2_]

S_[HBA1_] = LinkA_
S_[HBA2_] = LinkB_

S_[LinkA_] = [Concentrateur1_]
S_[Concentrateur1_] = [LinkC_]

S_[LinkB_] = [Concentrateur2_]
S_[Concentrateur2_] = [LinkD_]

S_[LinkC_] = [Disque1_]
S_[LinkD_] = [Disque2_]

S_[Disque1_] = S_[Disque2_] = 'S'

timerange = range(0, 24*365*2, 100)

print("Avec taux de reparation")
print("Fiabilité : " + str(S.reliability(100000000000)))
print("Disponibilité : " + str(S.availability(100000000000)))
print("------------------------")
print("Sans taux de reparation")
print("Fiabilité : " + str(S_.reliability(100000000000)))
print("Disponibilité : " + str(S_.availability(100000000000)))

import os
# ecrire les resultats dans un fichier
if not os.path.exists('resultats'):
    os.makedirs('resultats')

with open('resultats/arch2.txt', 'w') as f:
    f.write("Avec taux de reparation\n")
    f.write("Fiabilité : " + str(S.reliability(100000000000)) + "\n")
    f.write("Disponibilité : " + str(S.availability(100000000000)) + "\n")
    f.write("------------------------\n")
    f.write("Sans taux de reparation\n")
    f.write("Fiabilité : " + str(S_.reliability(100000000000)) + "\n")
    f.write("Disponibilité : " + str(S_.availability(100000000000)) + "\n")

# # Avec taux de reparation
# reliability = [S.reliability(t) for t in timerange]
# availability = [S.availability(t) for t in timerange]

# # Sans taux de reparation
# reliability_ = [S_.reliability(t) for t in timerange]
# availability_ = [S_.availability(t) for t in timerange]

# # Architecture 2 avec un taux de reparation
# p.plot(timerange, reliability, color="#ff7f0e") # orange
# p.plot(timerange, availability, color="#1f77b4") # bleu

# # Architecture 2 sans taux de reparation
# p.plot(timerange, reliability_, color="#2ca02c") # vert
# p.plot(timerange, availability_, color="#e377c2") # rose

# p.show()

