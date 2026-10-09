# ==============================================================================
# 📝 ÉNONCÉ : LE SIMULATEUR DE CALCUL D'IMPÔT SIMPLIFIÉ
# ==============================================================================
# Objectif : Créer un programme qui calcule le montant de l'impôt sur le revenu
# en fonction du salaire annuel et de la situation familiale (Célibataire / Marié).
# 
# CONTRAINTE : Utilisez uniquement des structures conditionnelles (if, elif, else).
# Pas de boucles (while/for) pour cet exercice.
# ==============================================================================

# ------------------------------------------------------------------------------
# Étape 1 : Saisie et Validation du Salaire
# ------------------------------------------------------------------------------
# 1. Demandez à l'utilisateur : "Entrez votre salaire annuel net (entier uniquement) : "
# 2. Vérifiez que la saisie ne contient QUE des chiffres (avec .isdigit()).
# 3. Si ce n'est pas le cas :
#    - Affichez : "Erreur : le salaire doit être un nombre entier."
#    - Arrêtez le programme immédiatement avec sys.exit().
# 4. Si c'est valide, convertissez immédiatement la variable en entier (int).

# ------------------------------------------------------------------------------
# Étape 2 : Saisie et Validation de la Situation
# ------------------------------------------------------------------------------
# 1. Demandez à l'utilisateur : "Êtes-vous célibataire ou marié ? (Tapez 'C' ou 'M') : "
# 2. Acceptez les majuscules comme les minuscules (Astuce : utilisez .upper()).
# 3. Si la saisie n'est ni 'C' ni 'M' :
#    - Affichez : "Erreur : option non reconnue."
#    - Arrêtez le programme immédiatement avec sys.exit().

# ------------------------------------------------------------------------------
# Étape 3 : Calcul du Taux d'Imposition
# ------------------------------------------------------------------------------
# Le pourcentage d'impôt dépend du salaire ET de la situation familiale.
#
# Cas A : L'utilisateur est Célibataire ('C')
#   - Salaire de 0 à 20 000 inclus             -> Taux = 0 %
#   - Salaire de 20 001 à 50 000 inclus        -> Taux = 15 %
#   - Salaire strictement supérieur à 50 000  -> Taux = 30 %
#
# Cas B : L'utilisateur est Marié ('M')
#   - Salaire de 0 à 30 000 inclus             -> Taux = 0 %
#   - Salaire de 30 001 à 75 000 inclus        -> Taux = 15 %
#   - Salaire strictement supérieur à 75 000  -> Taux = 30 %

# ------------------------------------------------------------------------------
# Étape 4 : Calcul Final et Affichage
# ------------------------------------------------------------------------------
# 1. Calculez le montant de l'impôt en euros.
#    (Formule : Impôt = Salaire * (Taux / 100))
# 2. Affichez le récapitulatif exact sous cette forme :
#
# Salaire déclaré : XXXX €
# Taux appliqué : XX %
# Montant de votre impôt : XXXX €

# ==============================================================================
# DEBUT DE VOTRE CODE CI-DESSOUS :
# ==============================================================================
import sys

liste_taux = [0, 15, 30]
taux = 0
impots = 0

salaire = input("Entrez votre salaire annuel net (entier uniquement) : ")
if salaire.isdigit():
    salaire = int(salaire)

    sit_mat = input("Êtes-vous célibataire ou marié ? (Tapez 'C' ou 'M') : ")
    sit_mat = sit_mat.upper()

    if sit_mat != "C" and sit_mat != "M":
        print("Erreur : option non reconnue.")
        sys.exit()

    elif sit_mat == "C":
        if 0 <= salaire <= 20000 : 
            taux = liste_taux[0]
        elif 20001 <= salaire <= 50000 :
            taux = liste_taux[1]
        elif  salaire > 50000 :
            taux = liste_taux[2]

    elif sit_mat == "M":
        if 0 <= salaire <= 30000 : 
            taux = liste_taux[0]
        elif 30001 <= salaire <= 75000 :
            taux = liste_taux[1]
        elif  salaire > 75000 :
            taux = liste_taux[2]

    impots = salaire * (taux / 100)

    
else:
    print("Erreur : le salaire doit être un nombre entier.")
    sys.exit()


print(f"Salaire déclaré : {salaire} €")
print(f"Taux appliqué : {taux} %")
print(f"Montant de votre impôt : {impots} €")