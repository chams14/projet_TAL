# DEFT2013 Tâche 2 : NOMEQUIPE (optionnel)
LE LANNIC Maëlle - GIRAUD Thomas

## Description de la tâche
1 ou 2 exemples de documents (avec leur identifiant)

## Statistiques corpus
Nombre de document de train/dev/test
Répartition des étiquettes dans chacun des sous-ensemble

test.cvs
- Entrée : 337
- Plat principal : 644
- Dessert : 407

train.csv
- Entrée : 2909
- Plat principal : 5802
- Dessert : 3762

On a séparer le fichier train en deux fichiers : un train et un validation
train = 90% des données 
- Entrée : 2615
- Plat principal : 5230
- Dessert : 3380

validation = 10% restant
- Entrée : 294
- Plat principal : 572
- Dessert : 382

## Méthodes proposées
### Run1: baseline (méthode de référence)
Description de la méthode:
- classifieur utilisé : prédiction de manière aléatoire

### Run2: TF_IDF 
Description de la méthode:
- descripteurs utilisés : TF-IDF
- classifieur utilisé : SVC 

### Run3: Word2Vec
Description de la méthode:
- descripteurs utilisés : Word2Vec
- classifieur utilisé : SVC

### Run4: MLP
Description de la méthode:
- descripteurs utilisés : Word2Vec
- classifieur utilisé : MLP

## Résultats
| Run                | Accuracy |     f1 Score   |
| ------------------ | --------:| --------------:|
| baseline           |   0.38   | 0.31 0.23 0.5  |
| SVC                |   0.88   | 0.99 0.75 0.88 |
| Word2Vec           |   0.86   | 0.99 0.69 0.85 |
| MLP                |   0.84   | 0.97 0.69 0.84 |

### Analyse de résultats
Pistes d'analyse:
* Combien de documents ont un score de 0 ? de 0.5 ? de 1 ? (Courbe ROC)
* Y-a-t-il des régularités dans les document bien/mal classifiés ?

#### Où est-ce que l'approche se trompe ? (matrice de confusion)
On remarque que la plus part des modèles se trompe pour les entrée. Ils sont souvent classés entant que Plat Principal 

#### Quels sont les descripteurs les plus décisifs 
En observant les résultats obtenus avec le RUN n°2 et le RUN n°3, les deux ayant été classifié par un modèle SVC, on remarque que le descripteurs TF-IDF semble être plus précis. 