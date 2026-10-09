mdp = input("Entrez un mot de passe(min 8 caractères): ")
mdp_trop_court = "votre mot de passe est trop court."
nbre = len(mdp)

if nbre == 0:
    print(mdp_trop_court.upper())

elif nbre < 8:
    print(mdp_trop_court.lower())

elif mdp.isdigit():
    print("Votre mot de passe ne contient que des nombres") 

else:
    print("Accès autorisé!")

