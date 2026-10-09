# Énoncé : Le Système de Validation d'Identifiant et Code Promo
# Vous devez créer un script Python pour un site de e-commerce. Le programme demande à l'utilisateur de saisir un identifiant client puis un code promo. Le système doit valider ces deux éléments selon des règles strictes.
# Étape 1 : Saisie et Validation de l'Identifiant
# Le programme demande : "Entrez votre identifiant client (ex: ID-12345) : "
# • L'identifiant doit faire exactement 8 caractères.
# • Il doit impérativement commencer par les trois lettres ID-.
# • Indice : Pour vérifier le début, vous pouvez regarder les 3 premiers caractères avec identifiant[0:3] ou utiliser la fonction .startswith("ID-").
# • Si l'identifiant est incorrect, affichez un message d'erreur précis (ex: trop court, ou ne commence pas par ID-) et arrêtez le programme immédiatement.
# Étape 2 : Saisie et Validation du Code Promo
# Si l'identifiant est valide, le programme demande : "Entrez votre code promo : "
# • Un code promo ne doit contenir que des lettres (pas de chiffres, pas d'espaces).
# • Indice : La méthode pour vérifier si une chaîne ne contient que des lettres est .isalpha().
# • Si le code contient des chiffres ou des symboles, affichez : "Code promo invalide (lettres uniquement)." et attribuez une réduction de 0%.
# Étape 3 : Calcul de la Réduction (Bonus Logique)
# La valeur de la réduction dépend de la longueur du code promo valide :
# • Si le code fait moins de 5 caractères : Réduction de 5%.
# • Si le code fait entre 5 et 8 caractères inclus : Réduction de 10%.
# • Si le code fait plus de 8 caractères : Réduction de 20%.
# Étape 4 : Résultat Final
# À la fin, si tout est bon, affichez un message récapitulatif :
# Identifiant [ID-XXXXX] validé ! Vous bénéficiez de XX% de réduction.

import sys

identifiant = input("Entrez votre identifiant client (ex: ID-12345) : ")
long_identifiant = len(identifiant)
val_promo = 0

if long_identifiant == 8 and identifiant[0:3] == "ID-":
    code_promo = input("Entrez votre code promo : ")
    
    if code_promo.isalpha():
        long_promo = len(code_promo)
        
        if long_promo < 5: 
            val_promo = 5
        elif 5 <= long_promo <= 8:
            val_promo = 10
        elif long_promo > 8:
            val_promo = 20
            
    else: 
        val_promo = 0
        print("Code promo invalide (lettres uniquement).")
        
else: 
    print("Erreur : L'identifiant est trop court, trop long ou ne commence pas par ID-.")
    sys.exit()

print(f"Identifiant [{identifiant}] validé ! Vous bénéficiez de {val_promo}% de réduction.")
