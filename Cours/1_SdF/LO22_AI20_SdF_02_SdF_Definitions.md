#Cours #LO22 #P24
# LO22 : Sûreté de Fonctionnement ^toc

- [[#LO22 : Sûreté de Fonctionnement ^toc|LO22 : Sûreté de Fonctionnement]]
	- [[#I. Introduction|I. Introduction]]
		- [[#I.1. Introduction|I.1. Introduction]]
				- [[#Définition (*Sûreté de fonctionnement*)|Définition (*Sûreté de fonctionnement*)]]
					- [[#Exemple|Exemple]]
		- [[#I.2. Génie logiciel|I.2. Génie logiciel]]
		- [[#I.3. Bugs célèbres|I.3. Bugs célèbres]]
		- [[#I.4. Debugging|I.4. Debugging]]
		- [[#I.5. Vertus de l'organisation|I.5. Vertus de l'organisation]]
		- [[#I.6. Qualités d'un logiciel|I.6. Qualités d'un logiciel]]
	- [[#II. Définitions Sûreté de fonctionnement|II. Définitions Sûreté de fonctionnement]]
		- [[#II.1. Définitions|II.1. Définitions]]
				- [[#Définition (*Sûreté de fonctionnement*)|Définition (*Sûreté de fonctionnement*)]]
				- [[#Définition (*Sûreté de fonctionnement en anglais : Dependability*)|Définition (*Sûreté de fonctionnement en anglais : Dependability*)]]
					- [[#Attention|Attention]]
				- [[#Définition (fautes, erreurs, défaillances)|Définition (fautes, erreurs, défaillances)]]
		- [[#II.2. Fiabilité : Reliability $R(t)$|II.2. Fiabilité : Reliability $R(t)$]]
		- [[#II.3. Maintenabilité $M(t)$|II.3. Maintenabilité $M(t)$]]
		- [[#II.4. Disponibilité : Availability $A(t)$|II.4. Disponibilité : Availability $A(t)$]]
		- [[#II.5. Taux de défaillance : $\lambda(t)$|II.5. Taux de défaillance : $\lambda(t)$]]

Venir en TP la semaine prochaine (semaine A). Si pas possible, prévenir par email.

## I. Introduction

### I.1. Introduction

##### Définition (*Sûreté de fonctionnement*)
Propriété qui permet à ses utilisateurs de placer une confiance justifiée dans le service délivré par un système

###### Exemple
- Ariane 5
- Les commandes des avions, trains sont assistés informatiquement

Deux aspects :
- Défaillances aléatoires du support matériel (électronique, redondances etc.)
- Défaillances systématiques liées à des erreurs de conception (bugs logiciel)

### I.2. Génie logiciel

> *There is no need to be a software genius*

### I.3. Bugs célèbres

- Mariner 2 : lanceur détruit 5mn après lancement
- Alunissage d'Apollo 11
- Therac 25 Canada en 1985
- Anti-Missile
- Ariane 5
- Mars Climate Orbiter

### I.4. Debugging

### I.5. Vertus de l'organisation

Juvénal (346 ap. J-C)

### I.6. Qualités d'un logiciel

## II. Définitions Sûreté de fonctionnement

### II.1. Définitions

##### Définition (*Sûreté de fonctionnement*)
Propriété qui permet à ses utilisateurs de placer une confiance justifiée dans le service délivré par un système
Attributs de la Sûreté de Fonctionnement : **FDMS** :
- **Fiabilité** : *continuité* du service
- **Disponibilité** : fait d'être prêt à l'*utilisation*
	- Restriction aux défaillances perturbantes
- **Maintenabilité** : aptitude aux *réparations*
- **Sécurité** : aptitude à éviter de provoquer des événements *catastrophiques*

##### Définition (*Sûreté de fonctionnement en anglais : Dependability*)
Propriété qui permet à ses utilisateurs de placer une confiance justifiée dans le service délivré par un système
Attributs de la Sûreté de Fonctionnement : **RAMSS** :
- **Reliability**
- **Availability**
- **Maintainability**
- **Safety** : sécurité *technique* (pas de catastrophe en cas de pannes)
- **Security** : sécurité *règlementaire* : vis-à-vis des *comportements humains* (respect du code du travail, anti-intrusion, résistance aux malveillances)

###### Attention
Sûreté != Sécurité != Safety

##### Définition (fautes, erreurs, défaillances)
Selon cette même terminologie :
- Une *défaillance* survient lorsque le service délivré par le système dévie de ce quoi il est destiné (*par exemple le non accomplissement d'une fonction requise*)
- La cause de la défaillance est une *erreur* affectant une partie de l'état du système (*par exemple une variable erronée (vitesse trop élevée*)
- La cause de l'erreur est une *faute* (*par exemple un emplacement mémoire corrompu*)
$$
\mathrm{Faute} \implies \mathrm{Erreur} \implies \mathrm{Défaillance}
$$
On peut avoir une arborescence d'implications. On parle alors de *propagation*.

> [!PDF|yellow] [[LO22_AI20_SdF_02_SdF_Definitions.pdf#page=29&selection=16,0,16,9&color=yellow|LO22_AI20_SdF_02_SdF_Definitions, page 29]]
> > attributs
> 
> Ce qui caractérisent

> [!PDF|red] [[LO22_AI20_SdF_02_SdF_Definitions.pdf#page=31&selection=6,0,10,12&color=red|LO22_AI20_SdF_02_SdF_Definitions, page 31]]
> > L’arbre de la SdF informatique

> [!PDF|note] [[LO22_AI20_SdF_02_SdF_Definitions.pdf#page=31&selection=44,0,48,9&color=note|LO22_AI20_SdF_02_SdF_Definitions, page 31]]
> > Sécurité - Innocuité
> 
> Signifie *safety*

> [!PDF|red] [[LO22_AI20_SdF_02_SdF_Definitions.pdf#page=45&selection=71,0,73,12&color=red|LO22_AI20_SdF_02_SdF_Definitions, page 45]]
> > Croissance de fiabilité
> 
> Bof bof selon le prof... Souvent assimilé au développement du logiciel

### II.2. Fiabilité : Reliability $R(t)$

> [!PDF|yellow] [[LO22_AI20_SdF_02_SdF_Definitions.pdf#page=46&selection=14,0,14,4&color=yellow|LO22_AI20_SdF_02_SdF_Definitions, page 46]]
> > $R(t)$
> 
> Probabilité de fonctionner sans défaillance

> [!PDF|yellow] [[LO22_AI20_SdF_02_SdF_Definitions.pdf#page=47&selection=34,7,34,11&color=yellow|LO22_AI20_SdF_02_SdF_Definitions, page 47]]
> > N(t)
> 
> Nombre de survivants. De plus on pose $N_{0} := N(0)$.

### II.3. Maintenabilité $M(t)$

> [!PDF|yellow] [[LO22_AI20_SdF_02_SdF_Definitions.pdf#page=49&selection=48,4,48,52&color=yellow|LO22_AI20_SdF_02_SdF_Definitions, page 49]]
> > Rien n'est irréparable dans le domaine technique
> 
> Quelqu'un finira par venir le réparer au bout d'un certain moment...

### II.4. Disponibilité : Availability $A(t)$

### II.5. Taux de défaillance : $\lambda(t)$

> [!PDF|yellow] [[LO22_AI20_SdF_02_SdF_Definitions.pdf#page=52&selection=28,0,28,28&color=yellow|LO22_AI20_SdF_02_SdF_Definitions, page 52]]
> > On démontre facilement que :
> 
>###### Démonstration
> Soit $X$ une variable aléatoire réelle mesurant la durée de vie de l'objet. Alors
> $$
> \begin{align}
> \lambda(t) \mathrm{d}t & = \mathbb{P}(\text{"Défaillance sur $[t, t + \mathrm{d}t]$" | "Pas de défaillance sur [0, t]"}) \\
> & = \mathbb{P}(X \leqslant t + \mathrm{d}t \mid X \geqslant t) \\
> & = 1 - \mathbb{P}(X \geqslant t + \mathrm{d}t \mid X \geqslant t) \\
> & = 1 - \frac{\mathbb{P}(X \geqslant t + \mathrm{d}t)}{\mathbb{P}(X \geqslant t)} \\
> & = \frac{\mathbb{P}(X \geqslant t) - \mathbb{P}(X \geqslant t+\mathrm{d}t)}{\mathbb{P}(X \geqslant t)} \\
> & = - \frac{R(t + \mathrm{d}t) - R(t)}{R(t)} \\
> & = - \frac{\mathrm{d}R(t)}{R(t)}
> \end{align}
> $$
> D'où
> $$
> \boxed{ \lambda(t) = - \frac{1}{R} \frac{\mathrm{d}R}{\mathrm{d}t} }
> $$

> [!PDF|important] [[LO22_AI20_SdF_02_SdF_Definitions.pdf#page=52&selection=6,1,9,3&color=important|LO22_AI20_SdF_02_SdF_Definitions, page 52]]
> > Taux de défaillance : $l(t)$
> 
> La courbe ci-contre représente $R(t)$.

> [!PDF|yellow] [[LO22_AI20_SdF_02_SdF_Definitions.pdf#page=54&selection=6,0,6,48&color=yellow|LO22_AI20_SdF_02_SdF_Definitions, page 54]]
> > Taux de défaillance des composants électroniques
> 
> Pour rester dans le creux : déverminage et remplacement préventif

> [!PDF|note] [[LO22_AI20_SdF_02_SdF_Definitions.pdf#page=55&selection=6,0,6,40&color=note|LO22_AI20_SdF_02_SdF_Definitions, page 55]]
> > Taux de défaillance des êtres humains...
> 
> Ne pas confondre périodicité et probabilité.

> [!PDF|yellow] [[LO22_AI20_SdF_02_SdF_Definitions.pdf#page=56&selection=56,0,56,34&color=yellow|LO22_AI20_SdF_02_SdF_Definitions, page 56]]
> > Intégration par parties immédiates
> 
> $$\mathrm{MTTF} = \int_{0}^{\infty} t\left( -\frac{\mathrm{d}R}{\mathrm{d}t} \right) \, \mathrm{d}t = [-tR(t)]_{0}^{+\infty} + \int_{0}^{\infty} R(t) \, \mathrm{d}t = \int_{0}^{\infty} R(t) \, \mathrm{d}t$$

> [!PDF|yellow] [[LO22_AI20_SdF_02_SdF_Definitions.pdf#page=56&selection=56,35,56,73&color=yellow|LO22_AI20_SdF_02_SdF_Definitions, page 56]]
> > (R rapidement décroissante à l'infini)
> 
> $R(t) \xrightarrow[t \to +\infty]{}0$

> [!PDF|yellow] [[LO22_AI20_SdF_02_SdF_Definitions.pdf#page=68&selection=83,0,92,1&color=yellow|LO22_AI20_SdF_02_SdF_Definitions, page 68]]
> > La disponibilité asymptotique vaut donc μ/(l+μ).
> 
> On a intérêt à avoir $\mu \gg \lambda$ pour augmenter la disponibilité asymptotique.

> [!PDF|yellow] [[LO22_AI20_SdF_02_SdF_Definitions.pdf#page=69&selection=16,0,16,7&color=yellow|LO22_AI20_SdF_02_SdF_Definitions, page 69]]
> > gravité
> 
> *severity* en anglais

> [!PDF|yellow] [[LO22_AI20_SdF_02_SdF_Definitions.pdf#page=69&selection=28,1,28,28&color=yellow|LO22_AI20_SdF_02_SdF_Definitions, page 69]]
> > taux d'occurrence par heure
> 
> Une fréquence laisse suggérer une périodicité tandis qu'un taux d'occurence est une notion probabiliste.

