# DEFT2013 Tâche 2 : NOMEQUIPE (optionnel)
LE LANNIC Maëlle - GIRAUD Thomas

## Description de la tâche
1 ou 2 exemples de documents (avec leur identifiant)

## Statistiques corpus
Nombre de document de train/dev/test
Répartition des étiquettes dans chacun des sous-ensemble

## Méthodes proposées
### Run1: baseline (méthode de référence)
Description de la méthode:
- classifieur utilisé : prédiction de manière aléatoire

### Run2: SVC 
Description de la méthode:
- descripteurs utilisés : TF-IDF
- classifieur utilisé : SVC 

### Run3: Word2Vec
Description de la méthode:
- descripteurs utilisés : Word2Vec
- classifieur utilisé : 

### Run4: MLP
Description de la méthode:
- descripteurs utilisés : By Pair Encoding
- classifieur utilisé : MLP

## Résultats
| Run                | f1 Score |
| ------------------ | --------:|
| baseline           |  15,2    |
| SVC                |   6,8    |
| Word2Vec           |  50,8    |
| MLP                |  70,2    |

### Analyse de résultats
Pistes d'analyse:
* Combien de documents ont un score de 0 ? de 0.5 ? de 1 ? (Courbe ROC)
* Y-a-t-il des régularités dans les document bien/mal classifiés ?
* Où est-ce que l'approche se trompe ? (matrice de confusion)
* Si votre méthode le permet: quels sont les descripteurs les plus décisifs ?