# ==============================================================================
# 📝 ÉNONCÉ : CONVERTISSEUR DE CENTIMES (COMPRÉHENSION DE LISTE)
# ==============================================================================

# Liste de départ (en centimes)
prix_en_centimes = [150, 500, 2450, 990, 100]

# Étape 1 : Créez une NOUVELLE liste nommée 'prix_en_euros'.
# Vous devez utiliser UNE SEULE LIGNE avec la compréhension de liste pour 
# diviser chaque élément de 'prix_en_centimes' par 100.

# [ÉCRIVEZ VOTRE LIGNE DE COMPRÉHENSION DE LISTE ICI]


# Étape 2 : Affichez la nouvelle liste 'prix_en_euros' pour vérifier le résultat.


prix_en_euro = [prix / 100 for prix in prix_en_centimes]
print(prix_en_euro)


# Partie 2
# ==============================================================================
# 📝 ÉNONCÉ : FILTRE DES ARTICLES DE LUXE
# ==============================================================================

# Liste de départ (en euros)
prix_en_euro = [1.5, 5.0, 24.5, 9.9, 1.0]

# Étape 1 : Créez une NOUVELLE liste nommée 'articles_luxe'.
# Utilisez UNE SEULE LIGNE avec la compréhension de liste pour ne garder 
# que les prix de 'prix_en_euro' qui sont STRICTEMENT supérieurs à 8.

# [ÉCRIVEZ VOTRE COMPRÉHENSION DE LISTE FILTRÉE ICI]


# Étape 2 : Affichez la liste 'articles_luxe'.

article_de_luxe = [prix for prix in prix_en_euro if prix > 8]
print(article_de_luxe)
