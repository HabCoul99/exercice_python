import sys

def valider_saisie(saisie):
    if saisie.isdigit(): 
        return True
    else:
        return False

print("BIENVENUE DANS LE JEU")
print("C'est parti !")

while True:
    saisie = input("Entrez un nombre (chiffres uniquement) : ")
    
    if valider_saisie(saisie) is False:
        print("Chiffres uniquement !")
        # Le mot-clé 'continue' force Python à passer DIRECTEMENT au tour suivant
        # sans lire les lignes d'en dessous. Très pratique ici !
        continue 
        
    saisie = int(saisie)
    
    if saisie == 42:
        print("Bravo !")
        break
    elif saisie < 42:
        print("C'est PLUS")
    elif saisie > 42:
        print("C'est MOINS")
