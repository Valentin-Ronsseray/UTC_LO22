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
- **Fiabilité** : continuité du service
- **Disponibilité** : fait d'être prêt à l'utilisation
	- Restriction aux défaillances perturbantes
- **Maintenabilité** : aptitude aux réparations
- **Sécurité** : aptitude à éviter de provoquer des problèmes.

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
- La cause de la défaillance est une *erreur* affectant une partie de l'état du système (*par exemple une variable erronée*)
- La cause de l'erreur est une *faute* (*par exemple un emplacement mémoire corrompu*)
$$
\mathrm{Faute} \implies \mathrm{Erreur} \implies \mathrm{Défaillance}
$$
On peut avoir une arborescence d'implications. On parle alors de *propagation*.

