# 🍷 Projet 6 — Nettoyage, Consolidation & Analyse des Données (BottleNeck)

## 🎯 Objectif du projet

L’objectif de ce projet était de **nettoyer, consolider et analyser le stock et les ventes** d’un marchand de vin haut de gamme, **BottleNeck**, afin d’aider l’entreprise à mieux comprendre ses performances commerciales et la qualité de ses données.

Ce travail se déroulait en deux grandes phases :

1. **Agréger et nettoyer les données** issues de plusieurs systèmes (ERP, site web, table de liaison)
2. **Réaliser des analyses commerciales** destinées au comité de direction (CODIR)

---

## 🧠 Compétences développées

### ✔️ Manipulation & nettoyage de données

* Détection d’erreurs :

  * valeurs incohérentes
  * erreurs de saisie
  * types incorrects
  * duplications
  * problèmes de jointure
* Création d’un pipeline de nettoyage reproductible
* Organisation du travail dans un **notebook Python**

### ✔️ Analyses exploratoires & statistiques

* Analyses univariées
* Détection de **valeurs aberrantes** (Z-Score, IQR, boxplot)
* Calculs métiers :

  * chiffre d’affaires
  * marges
  * rotation de stock
  * mois de couverture
* Analyse de corrélation entre variables quantitatives

### ✔️ Fusion & harmonisation des données

* Jointures multi‐sources
* Consolidation via une table de correspondance
* Mise en cohérence des SKUs / références ERP

### ✔️ Présentation & communication

* Présentation synthétique (20 slides)
* Recommandations pour :

  * amélioration du système ERP
  * fiabilisation des données
  * continuité du projet de data visualisation

---

# 🏢 Contexte du projet

Vous commencez une mission en tant que **Data Analyst chez BottleNeck**, un marchand de vin réputé.
Votre manager, **Nicolas**, vous confie un projet essentiel : améliorer le suivi des stocks et fournir des analyses fiables pour le comité de direction.

Problème actuel de l'entreprise :

* outils artisanaux
* bases non harmonisées
* références incohérentes entre l’ERP et le site web
* difficulté à analyser les ventes

Votre travail servira de point de départ au futur projet de data visualisation de l’entreprise.

---

# 🗂️ Phase 1 — Agrégations & Nettoyage des données

### 📥 Sources de données

* Extraction **ERP** (références, stock, prix)
* Extraction **site web** (SKU, ventes, descriptions)
* **Table de liaison** ERP ↔ WordPress (mise à jour par le stagiaire)
* Données d’octobre (stock au 31/10, ventes du 01/10 au 31/10)

### 🔧 Travail réalisé (Python)

* Fusion des jeux de données via la table de correspondance
* Détection d’au moins **8 types d’erreurs**, notamment :

  * valeurs manquantes
  * incohérences entre références
  * types incorrects
  * erreurs de calcul
  * doublons
  * mauvaises correspondances dans les jointures
  * erreurs de prix
  * quantités aberrantes
* Propositions d'améliorations pour :

  * le système ERP
  * la saisie
  * la structuration des données

### 📌 Livrable Phase 1 :

Notebook Python clair, documenté, incluant :

* nettoyage
* justification des corrections
* contrôle de cohérence
* explication des choix RGPD
* formalisation du processus de nettoyage

---

# 🗂️ Phase 2 — Analyses pour la direction

### 📊 Analyses réalisées

1. **Calcul du chiffre d’affaires**

   * par produit
   * total général

2. **Analyse des top références**

   * Pareto (20/80)
   * produits stars vs produits dormants

3. **Détection des valeurs aberrantes**

   * Z‐score
   * Interquartile (IQR)
   * Visualisation via boxplot
   * Conclusion : identification d’erreurs de prix

4. **Analyse financière**

   * marge brute
   * taux de marge
   * prix HT vs prix d’achat

5. **Analyse du stock**

   * état du stock
   * rotation des stocks
   * mois de stock restant

6. **Corrélations quantitatives**

   * prix
   * prix d’achat
   * stock
   * ventes
   * marge
     (Heatmap ou matrice de corrélation pour l’interprétation)

7. **Analyses complémentaires**

   * Détection de ruptures potentielles
   * Produits sous-margés
   * Recommandations stratégiques pour l’entreprise

---

# 🚀 Restitution & Recommandations

### 🎤 Support de présentation (20 slides max)

La présentation contient :

* Contexte & objectifs
* Pipeline de nettoyage
* Erreurs trouvées & correctifs recommandés
* Analyse du chiffre d’affaires
* Analyse des stocks
* Valeurs aberrantes (méthode + résultats)
* Corrélations
* Nos recommandations pour :

  * améliorer l’ERP
  * fiabiliser les data flows
  * structurer les identifiants produits
  * automatiser les contrôles

---

# 📦 Livrables finaux

* ✔️ **Notebook Python complet** (nettoyage + analyse)
* ✔️ **Présentation (max 20 slides)** comprenant :

  * nettoyage et consolidation
  * analyses
  * recommandations pour l’ERP
