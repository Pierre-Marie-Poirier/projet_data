# 🗄️ Projet 3 — Construction d’une Base de Données & Premières Requêtes SQL

## 📝 Contexte

Dans ce projet, j’ai accompagné une entreprise d’assurance dans l’analyse du marché de l’assurance habitation. L’objectif était de construire une base de données complète à partir de fichiers bruts, de modéliser son schéma relationnel, puis d’effectuer des requêtes SQL pour répondre à des besoins métier.

Le projet était structuré en plusieurs étapes progressives : compréhension des données, modélisation, création de la base, analyses SQL puis restitution.

---

## 🎯 Objectifs pédagogiques

* Explorer et comprendre un jeu de données réel
* Construire un **dictionnaire des données**
* Concevoir un **schéma relationnel normalisé**
* Générer le **code SQL de création des tables**
* Créer et charger une base de données dans un SGBD (SQLite, MySQL ou PostgreSQL)
* Écrire des requêtes SQL pour répondre à des questions métier
* Présenter la méthodologie et les analyses dans un support professionnel

---

## 🔍 Étape 1 — Exploration des données & Dictionnaire des données

### 📌 Travail réalisé

* Analyse des fichiers CSV :

  * Données des contrats clients
  * Référentiel géographique des régions françaises
* Création d’un **dictionnaire des données complet** comprenant :

  * Nom des variables
  * Type de données (integer, varchar, date, etc.)
  * Contraintes (tailles, formats…)
  * Description précise de chaque colonne

### 🧰 Compétences mobilisées

* Exploration de données
* Typage des variables
* Compréhension métier

---

## 🗺️ Étape 2 — Conception du schéma relationnel

### 📌 Travail réalisé

À partir d’un premier schéma proposé :

* Ajout des colonnes manquantes
* Ajustement des types de données
* Définition des clés primaires, clés étrangères et contraintes
* Normalisation du modèle
* Génération du **script SQL de création des tables** via SQL Power Architect

### 📎 Livrables

* Schéma relationnel (.jpg)
* Script SQL de création de la base (fichier .sql / .txt)

---

## 🧱 Étape 3 — Création et chargement de la base de données

### 📌 Travail réalisé

* Installation d’un SGBD (SQLite / MySQL / PostgreSQL)
* Création des tables via le script SQL généré
* Chargement des données nettoyées dans les tables
* Vérification de la cohérence :

  * Nombre de lignes égal entre CSV et base
  * Intégrité des données maintenue

### 📎 Livrables

* Base de données fonctionnelle avec les données importées
* Capture d’écran vérifiant :

  * La présence des tables
  * Le nombre de lignes

---

## 🧮 Étape 4 — Rédaction des premières requêtes SQL (analyses 1 à 3)

### 📌 Travail réalisé

Pour chacune des analyses :

* Écriture de la requête SQL
* Explication du raisonnement utilisé
* Capture d’écran des résultats

Cette étape permettait d’apprendre à structurer une requête :
identifier les variables nécessaires, choisir les clauses appropriées et vérifier la cohérence du résultat.

---

## 📊 Étape 5 — Requêtes SQL avancées (analyses 4 à 12)

### 📌 Analyses réalisées

* Contrats avec les plus grandes surfaces
* Prix moyen de la cotisation mensuelle
* Répartition des contrats selon les catégories de prix
* Comptage des formules *integral* dans la région Pays de la Loire
* Recherche de contrats d’un département spécifique
* Surface moyenne des contrats à Paris
* Classement des départements selon le prix moyen de cotisation
* Liste de communes ayant au moins 150 contrats
* Nombre de contrats par région

Pour chaque requête :
✔ Code SQL
✔ Résultat obtenu
✔ Capture d’écran

---

## 🖥️ Étape 6 — Restitution & Présentation finale

### 📌 Travail réalisé

Création d’un **support de présentation professionnel** (≈10 slides) incluant :

* La méthodologie complète
* Le dictionnaire des données
* Le schéma relationnel
* La structure de la base de données
* Les requêtes SQL principales et leurs résultats

Respect des bonnes pratiques :

* Moins de 7 éléments par slide
* Clarté visuelle
* Synthèse et pédagogie

### 📎 Livrable

* Présentation finale (PDF)

---

## 🧰 Compétences mobilisées

* Modélisation de bases de données
* Normalisation & contraintes
* SQL (SELECT, JOIN, GROUP BY, HAVING, ORDER BY…)
* Gestion d’un SGBD
* Data cleaning & import
* Rédaction technique et communication
