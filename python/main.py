colonnes = ["Composé","Synonyme", "Sous-Catégorie","Activité","Localisation","Milieu de vie","Auteur", "Source"]
tableau = []
def ajouter_lignes(valeur):
  if len(valeurs) != len(colonnes):
        print("Erreur : le nombre de valeurs ne correspond pas aux colonnes")
        return
    ligne = dict(zip(colonnes, valeurs))
    tableau.append(ligne)
def afficher_tableau():
    for ligne in tableau:
        print(ligne)

#le tableau vide est créé
#pour le remplir il suffit d'écrire la fonction "ajouter_lignes(les différentes valeurs de chaque colonne séparées par des virgules)"
#par exemple :

ajouter_lignes("Physcomitrium patens"," ", "Mousse", "Antibactérien et antioxydant", "Europe, Amérique du Nord, Japon", " "," ")

