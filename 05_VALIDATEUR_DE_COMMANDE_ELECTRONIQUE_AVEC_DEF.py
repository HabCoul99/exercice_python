# ==============================================================================
# 📝 ÉNONCÉ : LE VALIDATEUR DE COMMANDE ÉLECTRONIQUE (AVEC DEF)
# ==============================================================================
# Objectif : Créer un système de validation de commande qui utilise 3 fonctions
# distinctes pour valider l'email, calculer les frais de port et l'assurance.
# ==============================================================================
import sys

# ------------------------------------------------------------------------------
# Étape 1 : Fonction de validation de l'email
# ------------------------------------------------------------------------------
# Créez une fonction nommée 'valider_email' qui prend un paramètre 'email'.
# LOGIQUE :
# 1. L'email est valide s'il contient le caractère "@" ET s'il se termine 
#    par ".com" ou ".fr" (Astuce : utilisez .endswith(".com") ou .endswith(".fr")).
# 2. Si c'est valide, retournez (return) la valeur booléenne True.
# 3. Sinon, retournez la valeur booléenne False.

# [ÉCRIVEZ VOTRE PREMIÈRE FONCTION ICI]
def valider_email(email):
    if "@" in email and (email.endswith(".com") or email.endswith(".fr")):
        return True
    else: 
        return False


# ------------------------------------------------------------------------------
# Étape 2 : Fonction de calcul des frais de port
# ------------------------------------------------------------------------------
# Créez une fonction nommée 'calculer_frais_port' qui prend deux paramètres :
# 'montant_panier' (un entier) et 'pays' (une chaîne de caractères).
# LOGIQUE :
# 1. Si le pays est "FRANCE" :
#    - Si le montant du panier est supérieur ou égal à 100 €, les frais sont de 0 €.
#    - Sinon, les frais sont de 5 €.
# 2. Si le pays est "EUROPE" :
#    - Les frais sont toujours de 12 €.
# 3. Retournez (return) le montant des frais de port.

# [ÉCRIVEZ VOTRE DEUXIÈME FONCTION ICI]

def calculer_frais_port (montant_pannier, pays):
    if pays == "FRANCE":    
        if montant_pannier >= 100:
            frais = 0
        else: 
            frais = 5
    else:
        frais = 12
    return frais

# ------------------------------------------------------------------------------
# Étape 3 : Fonction d'application de l'assurance
# ------------------------------------------------------------------------------
# Créez une fonction nommée 'appliquer_assurance' qui prend deux paramètres :
# 'montant_panier' (un entier) et 'choix_assurance' (une chaîne de caractères).
# LOGIQUE :
# 1. Si choix_assurance est "OUI" : l'assurance coûte 5% du montant du panier.
#    (Formule : montant_panier * 0.05)
# 2. Si choix_assurance est "NON" : l'assurance coûte 0 €.
# 3. Retournez (return) le coût de l'assurance.

# [ÉCRIVEZ VOTRE TROISIÈME FONCTION ICI]

def appliquer_assurance(montant_panier, choix_assurance):
    if choix_assurance == "OUI":
        montant_assurance = montant_panier * 0.05
    elif choix_assurance == "NON":
        montant_assurance = 0
    else: 
        print("Saisie incorrecte! (la reponsonse doit être OUI ou NON)")
    return montant_assurance
# ==============================================================================
# 🚀 PROGRAMME PRINCIPAL (L'utilisation et la connexion de vos fonctions)
# ==============================================================================

# 1. Demandez l'adresse email à l'utilisateur.
#    Appelez 'valider_email'. Si elle renvoie False -> message d'erreur + sys.exit()


# 2. Demandez le montant du panier.
#    Vérifiez qu'il ne contient que des chiffres (.isdigit()), puis convertissez-le en entier.
#    Si ce n'est pas un chiffre -> message d'erreur + sys.exit()


# 3. Demandez le pays de destination ("FRANCE" ou "EUROPE").
#    Pensez à utiliser .upper(). Si la saisie n'est ni l'un ni l'autre -> message d'erreur + sys.exit()


# 4. Demandez si l'utilisateur souhaite l'assurance ("OUI" ou "NON").
#    Pensez à utiliser .upper(). Si la saisie n'est ni l'un ni l'autre -> message d'erreur + sys.exit()


# 5. Appelez vos fonctions 'calculer_frais_port' et 'appliquer_assurance' 
#    avec les bonnes variables et stockez leurs retours dans des variables précises.


# 6. Calculez le Total Net à payer (Panier + Frais de port + Assurance).


# 7. Affichez le récapitulatif complet de la facture à l'écran.


adresse_email = input("Entrez l'adresse email: ")
verif_email = valider_email(adresse_email)
if verif_email is False:
    print("Email invalide! (l'adresse email doit contenir @ et doit se terminer par .com ou .fr)")
    sys.exit()
else: 
    montant_panier_saisi = input("Entrez le montant du panier: ")
    if montant_panier_saisi.isdigit():
        montant_panier_saisi = int(montant_panier_saisi)
    else:
        print("Erreur de saisie (le montant doit être uniquement un chiffre)")
        sys.exit()

    pays_saisi = input("Entrez le pays de destination: ").upper()
    if pays_saisi not in ["FRANCE", "EUROPE"]:
        print("Saisie incorrecte! (pays doit être FRANCE OU EUROPE)")
        sys.exit()

    saisie_assurance = input("Souhaitez vous l'assurance? (repondez par OUI ou par NON): ").upper()
    if saisie_assurance not in ["OUI", "NON"]:
        print("Saisie incorrecte! (vous devez repondre par 0UI ou par NON )" )
        sys.exit()


    frais_port = calculer_frais_port(montant_panier_saisi, pays_saisi)
    montant_assurance = appliquer_assurance(montant_panier_saisi, saisie_assurance)
    montant_total = montant_panier_saisi + frais_port + montant_assurance

    print(f"Pays de destination: {pays_saisi}")
    print(f"Montant du panier: {montant_panier_saisi} €")
    print(f"Montant de l'assurance: {montant_assurance} €") 
    print(f"Total Net à payer: {montant_total} €") 
    
