# ==============================================================================
# 📝 ÉNONCÉ : LE CONVERTISSEUR DE DEVISES ORGANISÉ (AVEC DEF)
# ==============================================================================
# Objectif : Créer un convertisseur de devises Euros (€) vers Dollars (USD) ou 
# Livres (GBP) en séparant la logique du code dans deux fonctions réutilisables.
# ==============================================================================
import sys

# ------------------------------------------------------------------------------
# Étape 1 : Définition de la fonction de validation
# ------------------------------------------------------------------------------
# Créez une fonction nommée 'valider_montant' qui prend un paramètre 'saisie'.
# LOGIQUE :
# 1. Vérifiez si 'saisie' ne contient que des chiffres avec .isdigit().
# 2. Si c'est valide : retournez (return) le montant converti en entier (int).
# 3. Si ce n'est pas valide : affichez un message d'erreur et coupez le programme.

# [ÉCRIVEZ VOTRE PREMIÈRE FONCTION ICI]

def valider_montant (saisie):
    if saisie.isdigit(): 
        saisie = int(saisie)
    else: 
        print("Erreur de saisie! (montant doit être saisie en chiffre uniquement)")
        sys.exit()
    return saisie

# ------------------------------------------------------------------------------
# Étape 2 : Définition de la fonction de calcul
# ------------------------------------------------------------------------------
# Créez une fonction nommée 'calculer_conversion' qui prend deux paramètres : 
# 'montant' (un entier) et 'devise' (une chaîne de caractères).
# LOGIQUE :
# 1. Si la 'devise' est "USD", multipliez le 'montant' par 1.10.
# 2. Si la 'devise' est "GBP", multipliez le 'montant' par 0.85.
# 3. Retournez (return) le résultat de ce calcul (le montant converti).

# [ÉCRIVEZ VOTRE DEUXIÈME FONCTION ICI]
def calculer_conversion (montant, devise) :
    if devise == "USD" :
        montant = montant * 1.10
    elif devise == "GBP" :
        montant = montant * 0.85

    return montant

    
# ==============================================================================
# 🚀 PROGRAMME PRINCIPAL (L'utilisation de vos fonctions)
# ==============================================================================

# 1. Demandez le montant en Euros à l'utilisateur
# montant_brut = input("Entrez le montant en Euros (€) : ")

# 2. Appelez votre fonction 'valider_montant' en lui envoyant 'montant_brut'
#    Stockez le résultat du return dans une variable (ex: montant_propre)


# 3. Demandez la devise cible à l'utilisateur
# devise_cible = input("Choisissez la devise cible (USD ou GBP) : ").upper()

# 4. Vérifiez que la devise est bien "USD" ou "GBP" (avec votre condition habituelle)
#    Si ce n'est pas le cas, affichez une erreur et faites un sys.exit()


# 5. Appelez votre fonction 'calculer_conversion' en lui donnant les deux ingrédients :
#    le montant validé et la devise choisie. Stockez le résultat (ex: resultat_final)


# 6. Affichez le résultat final proprement (ex: "XX € vaut XX USD")


montant_saisie = input("Entrez le montant en Euros (€) : ")

montant_valide = valider_montant(montant_saisie)

devise_saisie = input("Choisissez la devise cible (USD ou GBP) : ").upper()
if devise_saisie == "USD" or devise_saisie == "GBP" :
    montant_convertit = calculer_conversion(montant_valide, devise_saisie)

else:
    print("Erreur de saisie ! (devise doit être unisuement USD ou GBP)")
    sys.exit()

print(f"{montant_saisie} € vaut {montant_convertit} {devise_saisie} ")