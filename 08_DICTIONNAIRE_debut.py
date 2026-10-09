import requests
from bs4 import BeautifulSoup
import sys

# URL de recherche immobilière globale à Abidjan sur CoinAfrique
SITE_COINAFRIQUE = "https://coinafrique.com"
BUDGET_MAX = 120000

print("Lancement du robot immo (Cible : CoinAfrique Côte d'Ivoire)...")

# Configuration de base pour la requête
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

reponse = requests.get(SITE_COINAFRIQUE, headers=headers)

if reponse.status_code == 200:
    soup = BeautifulSoup(reponse.text, "html.parser")
    
    # Sur CoinAfrique, chaque carte d'annonce de logement est contenue dans une balise div avec la classe spécifique 'card-flex' ou 'ad-card'
    cartes_logements = soup.select(".card-flex, .ad-card, .card")
    leads_immobiliers = 0

    zones_recherche = ["cocody", "angre", "plateau", "palmeraie", "baoule", "dokui"]
    types_logement = ["chambre", "salon", "2 pieces", "2 pièces", "studio"]

    with open("opportunites_coinafrique.txt", "w", encoding="utf-8") as fichier:
        fichier.write("==================================================\n")
        fichier.write(f"   ALERTE RAPPORT IMMO : COINAFRIQUE (MAX {BUDGET_MAX} F)\n")
        fichier.write("==================================================\n\n")

        for carte in cartes_logements:
            # Récupération du titre, du prix et de la localisation/date
            balise_titre = carte.select_one(".card-title, .title, h3")
            balise_prix = carte.select_one(".card-price, .price")
            balise_infos = carte.select_one(".card-location, .location") # Contient souvent le quartier et le temps

            if balise_titre and balise_prix:
                titre = balise_titre.text.strip()
                prix_brut = balise_prix.text.strip()
                infos = balise_infos.text.strip() if balise_infos else "Abidjan"

                texte_complet = (titre + " " + infos).lower()

                # 1. FILTRE DE QUARTIER ET DE TYPE DE BIEN
                match_zone = any(zone in texte_complet for zone in zones_recherche)
                match_type = any(t in texte_complet for t in types_logement)

                if match_zone and match_type:
                    # 2. NETTOYAGE ET FILTRAGE DU PRIX NUMÉRIQUE
                    prix_propre = prix_brut.replace("CFA", "").replace("FCFA", "").replace(" ", "").replace(" ", "")
                    
                    if prix_propre.isdigit():
                        prix_entier = int(prix_propre)
                        
                        # Si le prix dépasse le budget max de votre ami, on rejette
                        if prix_entier > BUDGET_MAX or prix_entier < 10000:
                            continue
                    else:
                        continue

                    # Structure Dictionnaire Pro
                    maison = {
                        "designation": titre,
                        "loyer": prix_entier,
                        "details_zone": infos
                    }

                    # Sauvegarde dans le rapport d'affaires
                    fichier.write(f"🏠 LOGEMENT : {maison['designation']}\n")
                    fichier.write(f"💰 LOYER : {maison['loyer']} FCFA / mois\n")
                    fichier.write(f"📍 INFOS SITE : {maison['details_zone']}\n")
                    fichier.write("--------------------------------------------------\n")
                    
                    leads_immobiliers += 1

        fichier.write(f"\nFin de l'extraction. Total opportunités qualifiées : {leads_immobiliers}\n")

    print("\n[SUCCÈS DU SCAN COINAFRIQUE]")
    print(f"-> {leads_immobiliers} appartements chambre-salon valides ont été trouvés.")
    print("-> Ouvrez 'opportunites_coinafrique.txt' pour extraire les données de votre ami !")

else:
    print(f"Erreur d'accès au site CoinAfrique. Code HTTP : {reponse.status_code}")
