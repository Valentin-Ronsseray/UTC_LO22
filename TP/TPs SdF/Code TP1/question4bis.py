from fiabilipy import *
import pylab as p

HBA1 = Component('HBA1', 0)
HBA2 = Component('HBA2', 1.25e-6)

LinkA = Component('LinkA', 2.52e-6)
LinkB = Component('LinkB', 2.52e-6)

Concentrateur1 = Component('Concentrateur1', 1.71e-6)
Concentrateur2 = Component('Concentrateur2', 1.71e-6)

LinkC = Component('LinkC', 2.52e-6)
LinkD = Component('LinkD', 2.52e-6)

Disque1 = Component('Disque1', 1e-5)
Disque2 = Component('Disque2', 1e-5)

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

HBA1_ = Component('_', 10000000000000000)

S_ = System()
S_['E'] = [HBA1_, HBA2]

S_[HBA1_] = LinkA
S_[HBA2] = LinkB

S_[LinkA] = [Concentrateur1]
S_[Concentrateur1] = [LinkC]

S_[LinkB] = [Concentrateur2]
S_[Concentrateur2] = [LinkD]

S_[LinkC] = [Disque1]
S_[LinkD] = [Disque2]

S_[Disque1] = S_[Disque2] = 'S'

timerange = range(0, 24*365*25, 100)

def I1(t):
    return S.reliability(t) - S_.reliability(t)

p.plot(timerange, [I1(t) for t in timerange], label='Composants HBA')

HBA1 = Component('HBA1', 1.25e-6)
LinkA = Component('LinkA', 0)

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

LinkA_ = Component('_', 10000000000000000)

S_ = System()
S_['E'] = [HBA1, HBA2]

S_[HBA1] = LinkA_
S_[HBA2] = LinkB

S_[LinkA_] = [Concentrateur1]
S_[Concentrateur1] = [LinkC]

S_[LinkB] = [Concentrateur2]
S_[Concentrateur2] = [LinkD]

S_[LinkC] = [Disque1]
S_[LinkD] = [Disque2]

S_[Disque1] = S_[Disque2] = 'S'

def I2(t):
    return S.reliability(t) - S_.reliability(t)

p.plot(timerange, [I2(t) for t in timerange], label='Composants Link')

LinkA = Component('LinkA', 2.52e-6)
Concentrateur1 = Component('Concentrateur1', 0)

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

Concentrateur1_ = Component('_', 10000000000000000)

S_ = System()
S_['E'] = [HBA1, HBA2]

S_[HBA1] = LinkA
S_[HBA2] = LinkB

S_[LinkA] = [Concentrateur1_]
S_[Concentrateur1_] = [LinkC]

S_[LinkB] = [Concentrateur2]
S_[Concentrateur2] = [LinkD]

S_[LinkC] = [Disque1]
S_[LinkD] = [Disque2]

S_[Disque1] = S_[Disque2] = 'S'

def I3(t):
    return S.reliability(t) - S_.reliability(t)

p.plot(timerange, [I3(t) for t in timerange], label='Composants Concentrateur')

Concentrateur1 = Component('Concentrateur1', 1.71e-6)
Disque1 = Component('Disque1', 0)

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

Disque1_ = Component('_', 10000000000000000)

S_ = System()
S_['E'] = [HBA1, HBA2]

S_[HBA1] = LinkA
S_[HBA2] = LinkB

S_[LinkA] = [Concentrateur1]
S_[Concentrateur1] = [LinkC]

S_[LinkB] = [Concentrateur2]
S_[Concentrateur2] = [LinkD]

S_[LinkC] = [Disque1_]
S_[LinkD] = [Disque2]

S_[Disque1_] = S_[Disque2] = 'S'

def I4(t):
    return S.reliability(t) - S_.reliability(t)

p.plot(timerange, [I4(t) for t in timerange], label='Composants Disque')
p.legend()
p.show()

# courbe orange : Link
# courbe bleue : HBA
# courbe verte : Concentrateur
# courbe rouge : Disque