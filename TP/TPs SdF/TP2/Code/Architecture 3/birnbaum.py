from fiabilipy import *
import pylab as p

timerange = range(0, 24*365*5, 100)

P1 = Component('P1', 0)
P2 = Component('P2', 2.28e-4)
P3 = Component('P3', 2.28e-4)
P4 = Component('P4', 0)
P5 = Component('P5', 2.28e-4)
P6 = Component('P6', 2.28e-4)

M1 = Component('M1', 2.94e-4)
M2 = Component('M2', 2.94e-4)

Bus = Component('Bus', 1e-4)

Alim = Component('Alim', 2.28e-4)
alims = Voter(Alim, 2, 3)

# Système 
S = System()
S['E'] = [alims]
S[alims]= [P1, P4, P5]

S[P1] = [P2]
S[P2] = [M1, M2]

S[P4] = [P3]
S[P3] = [M1, M2]

S[P5] = [P6]
S[P6] = [M1, M2]

S[M1] = S[M2] = [Bus]

S[Bus] = 'S'

# Autre système : facteur de birnbaum processeurs
P1_ = Component('P1', 100000000000000000)
P4_ = Component('P4', 100000000000000000)

S_ = System()
S_['E'] = [alims]
S_[alims] = [P1_, P4_, P5]

S_[P1_] = [P2]
S_[P2] = [M1, M2]

S_[P4_] = [P3]
S_[P3] = [M1, M2]

S_[P5] = [P6]
S_[P6] = [M1, M2]

S_[M1] = S_[M2] = [Bus]

S_[Bus] = 'S'

def I1(t):
    return S.reliability(t) - S_.reliability(t)

p.plot(timerange, [I1(t) for t in timerange], label='Processeurs', color="#ff7f0e") # orange

# Autre système : facteur de birnbaum bus
P1 = Component('P1', 2.28e-4)
P4 = Component('P4', 2.28e-4)

Bus = Component('Bus', 0)
Bus_ = Component('Bus', 100000000000000000)

S = System()
S['E'] = [alims]
S[alims]= [P1, P4, P5]

S[P1] = [P2]
S[P2] = [M1, M2]

S[P4] = [P3]
S[P3] = [M1, M2]

S[P5] = [P6]
S[P6] = [M1, M2]

S[M1] = S[M2] = [Bus]

S[Bus] = 'S'

S_ = System()
S_['E'] = [alims]
S_[alims] = [P1, P4, P5]

S_[P1] = [P2]
S_[P2] = [M1, M2]

S_[P4] = [P3]
S_[P3] = [M1, M2]

S_[P5] = [P6]
S_[P6] = [M1, M2]

S_[M1] = S_[M2] = [Bus_]

S_[Bus_] = 'S'

def I2(t):
    return S.reliability(t) - S_.reliability(t)

p.plot(timerange, [I2(t) for t in timerange], label='Bus', color="#2ca02c") # vert

# Autre système : facteur de birnbaum mémoires
Bus = Component('Bus', 1e-4)
M1 = Component('M1', 0)
M1_ = Component('M1', 100000000000000000)

S = System()
S['E'] = [alims]
S[alims] = [P1, P4, P5]

S[P1] = [P2]
S[P2] = [M1, M2]

S[P4] = [P3]
S[P3] = [M1, M2]

S[P5] = [P6]
S[P6] = [M1, M2]

S[M1] = S[M2] = [Bus]

S[Bus] = 'S'

S_ = System()
S_['E'] = [alims]
S_[alims] = [P1, P4, P5]

S_[P1] = [P2]
S_[P2] = [M1_, M2]

S_[P4] = [P3]
S_[P3] = [M1_, M2]

S_[P5] = [P6]
S_[P6] = [M1_, M2]

S_[M1_] = S[M2] = [Bus]
S_[Bus] = 'S'

def I3(t):
    return S.reliability(t) - S_.reliability(t)

p.plot(timerange, [I3(t) for t in timerange], label='Mémoires', color="#d62728") # rouge

# Autre système : facteur de birnbaum alimentation
M1 = Component('M1', 2.94e-4)

P1 = Component('P1', 2.28e-4)
pros = Voter(P1, 2, 3)

Alim1 = Component('Alim', 0)
Alim1_ = Component('Alim', 100000000000000000)
Alim2 = Component('Alim', 2.28e-4)
Alim3 = Component('Alim', 2.28e-4)

Alim4 = Component('Alim', 0)
Alim4_ = Component('Alim', 100000000000000000)
Alim5 = Component('Alim', 2.28e-4)
Alim6 = Component('Alim', 2.28e-4)

S = System()
S['E'] = [Alim1, Alim3, Alim5]

S[Alim1] = Alim2
S[Alim2] = [pros]

S[Alim3] = Alim4
S[Alim4] = [pros]

S[Alim5] = Alim6
S[Alim6] = [pros]

S[pros] = [M1, M2]

S[M1] = S[M2] = [Bus]

S[Bus] = 'S'

S_ = System()
S_['E'] = [Alim1_, Alim3, Alim5]
S_[Alim1_] = Alim2
S_[Alim2] = [pros]

S_[Alim3] = Alim4_
S_[Alim4_] = [pros]

S_[Alim5] = Alim6
S_[Alim6] = [pros]

S_[pros] = [M1_, M2]
S_[M1_] = S[M2] = [Bus]

S_[Bus] = 'S'

def I4(t):
    return S.reliability(t) - S_.reliability(t)

p.plot(timerange, [I4(t) for t in timerange], label='Alimentation', color="#9467bd") # violet

p.xlabel('Temps (heures)')
p.ylabel('Facteur de Birnbaum')

# Affichage de la légende
p.legend()

# Affichage du graphique
p.show()
