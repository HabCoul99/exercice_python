# ==============================================================================
# 📝 ÉNONCÉ : LE CALCULATEUR DE MOYENNE SCOLAIRE
# ==============================================================================

# Étape 1 : Définir la fonction analyser_notes(liste_notes)
# Étape 2 : Écrire la boucle for pour calculer la somme des notes
# Étape 3 : Calculer la moyenne
# Étape 4 : Déterminer la mention ("Admis" ou "Ajourné")
# Étape 5 : Retourner la moyenne et la mention

# [ÉCRIVEZ VOTRE FONCTION ICI]

def analyser_note(liste_notes):
    somme_note = 0
    for note in liste_notes:
        somme_note = somme_note + note
    nbre_note = len(liste_notes)
    moyenne = somme_note / nbre_note

    if moyenne >= 10 : 
        mention = "Admis"
    else:
        mention = "Ajourné"

    return moyenne, mention

# ==============================================================================
# 🚀 PROGRAMME PRINCIPAL
# ==============================================================================

mes_notes = [12, 8, 14, 7, 15, 11]

# Étape 6 : Appeler la fonction avec la liste 'mes_notes'
# Étape 7 : Afficher les résultats sous la forme : "Moyenne : XX.XX / Mention : XXXX"

resultat = analyser_note(mes_notes)
print(f"Moyenne : {resultat[0]} / Mention: {resultat[1]}") 
