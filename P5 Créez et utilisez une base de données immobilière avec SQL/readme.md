# 🏡 Projet 5 — Modéliser, construire et interroger une base de données (DATAImmo)

## 🎯 Objectif du projet

L’objectif de ce projet était de **concevoir, normaliser et implémenter une base de données relationnelle** afin d’aider l’entreprise *Laplace Immo* à analyser les transactions immobilières en France.
Ce travail s’inscrit dans le projet interne **DATAImmo**, piloté par la CTO, visant à mieux comprendre et prédire les prix immobiliers.

Il s’agissait de :

* Concevoir un **schéma relationnel respectant la 3NF**
* Construire une **base de données SQL complète**
* Importer des fichiers CSV et gérer les **contraintes et relations**
* Établir un **dictionnaire de données conforme RGPD**
* Rédiger des **requêtes SQL avancées** pour analyser le marché immobilier
* Produire une présentation claire et professionnelle des résultats

---

## 🧠 Compétences développées

### ✔️ Conception de bases de données

* Identification des données clés
* Création d’un **schéma relationnel normalisé (3NF)**
* Définition des **clés primaires, étrangères et contraintes**

### ✔️ Manipulation de données

* Analyse de fichiers DVF, INSEE et Data.gouv
* Import de données nettoyées
* Vérification de l’intégrité et des types

### ✔️ SQL avancé

* Agrégations
* Filtrages complexes
* Jointures multi-tables
* Calculs d’indicateurs immobiliers

### ✔️ Gouvernance & qualité des données

* Création d’un **dictionnaire de données complet**
* Respect des règles **RGPD**
* Mise en place d'une stratégie de sauvegarde

---

## 🏢 Contexte du projet

Vous êtes recruté par **Laplace Immo**, un réseau national d’agences immobilières.
La direction souhaite exploiter les données pour créer un modèle prédictif fiable des prix immobiliers.

La CTO, **Clara Daucourt**, vous confie :

> **La refonte et l’enrichissement de la base de données interne**
> afin d’intégrer :

* les données DVF (transactions immobilières)
* des données démographiques INSEE
* des référentiels géographiques Data.gouv

Vous devez également préparer une analyse SQL destinée aux agences régionales.

---

# 🗂️ Étapes du projet

## 🧩 Étape 1 — Compréhension & préparation des données

Travail réalisé :

* Analyse approfondie des fichiers (DVF, INSEE, référentiel géographique)
* Identification :

  * des données essentielles à conserver
  * des colonnes à supprimer (doublons, données sensibles → RGPD)
* Construction du **dictionnaire de données**, comprenant pour chaque variable :

  * code
  * signification
  * type
  * longueur
  * nature
  * règles de gestion et de calcul

**Livrable :** Dictionnaire de données complet et conforme RGPD.

---

## 🧩 Étape 2 — Modification du schéma relationnel

Objectifs :

* Intégrer les nouvelles données “région” et “population”
* Appliquer les règles de la **3NF**
* Définir toutes les clés :

  * clés primaires
  * clés étrangères
* Identifier les relations entre tables

Points clés :

* Suppression des redondances (ex : voie/code voie, département/code département)
* Construction de clés composites lorsque nécessaire
  Exemple :
  `id_codedep_codecommune = CodeDépartement + CodeCommune`

**Livrable :** Nouveau schéma relationnel normalisé.

---

## 🧩 Étape 3 — Création de la base de données

Travail effectué :

* Création d’une base via SQLite (ou SQL Server/MySQL/PostgreSQL)
* Construction des tables :

  * respect des noms
  * types corrects
  * contraintes
  * relations PK/FK
* Contrôle de cohérence

  * vérification du nombre de lignes
  * conformité des types

**Livrable :** Base de données fonctionnelle.

---

## 🧩 Étape 4 — Import des données & contrôles

* Import des fichiers CSV nettoyés
* Vérification de l’intégrité :

  * respect des types
  * absence de valeurs interdites
  * cohérence des clés étrangères

---

## 🧩 Étape 5 — Rédaction des requêtes SQL & analyse

Production de requêtes visant à analyser :

* les prix immobiliers selon les zones
* les tendances régionales
* les indicateurs clés :

  * prix médian
  * surface moyenne
  * types de biens
* comparaisons territoriales

**Livrable :**
Code SQL + résultats intégrés dans une présentation.

---

## 🧩 Étape 6 — Vérification & préparation de la soutenance

* Auto-évaluation du projet
* Vérification de la cohérence des requêtes et de la BDD
* Finalisation des supports : schéma, dictionnaire, analyse SQL

---

# 📦 Livrables finaux

* ✔️ **Dictionnaire de données complet**
* ✔️ **Schéma relationnel normalisé (3NF)**
* ✔️ **Base de données SQL opérationnelle**
* ✔️ **Requêtes SQL + résultats**
* ✔️ **Support de présentation contenant :**

  * Contexte du projet
  * Conformité RGPD
  * Données initiales
  * Extrait du dictionnaire
  * Schéma relationnel
  * Tables créées
  * Requêtes SQL + outputs
