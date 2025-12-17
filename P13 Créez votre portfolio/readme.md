# 💵 Projet 12 — Détection de faux billets pour l’ONCFM

## 🎯 Objectif du projet

Le projet avait pour objectif de **développer un modèle de machine learning** permettant de **prédire si un billet en euros est vrai ou faux** à partir de caractéristiques physiques (longueur, largeur, hauteur, etc.).
Le projet inclut la **modélisation, le choix de l’algorithme et la création d’une application fonctionnelle** pour la détection des billets.

---

## 🧠 Compétences développées

### ✔️ Préparation et exploration des données

* Nettoyage et vérification de la qualité des données (1500 billets, 1000 vrais et 500 faux)
* Analyse des distributions et traitement des valeurs manquantes
* Préparation des variables pour la modélisation

### ✔️ Machine learning supervisé et non supervisé

* Test de plusieurs algorithmes :

  * **K-means** pour le clustering non supervisé
  * **Régression logistique**
  * **K-Nearest Neighbors (KNN)**
  * **Random Forest**
* Évaluation de chaque modèle avec les métriques adaptées (précision, rappel, F1-score, etc.)
* Sélection du **modèle final** en fonction des performances et de la robustesse

### ✔️ Développement d’une application

* Création d’un **notebook Python interactif** permettant à l’utilisateur de tester la nature d’un billet en entrant ses caractéristiques
* Démonstration de la prédiction pour de nouveaux billets

### ✔️ Communication et data storytelling

* Préparation d’un **support de présentation de 20 slides** synthétique :

  * Méthodologie de traitement des données
  * Comparaison des modèles et résultats
  * Justification du choix du modèle final
  * Présentation de l’application fonctionnelle

---

## 🏢 Contexte du projet

L’**ONCFM (Organisation nationale de lutte contre le faux-monnayage)** souhaitait automatiser la détection des faux billets pour aider ses équipes à **identifier rapidement les billets contrefaits**.
Le projet devait produire :

* Un **modèle prédictif fiable**
* Une **application fonctionnelle utilisable par les équipes**
* Une **présentation claire des résultats et recommandations**

---

## 🗂️ Étapes du projet

### 📝 Étape 1 — Préparation des données

* Analyse du jeu de données de 1500 billets
* Nettoyage, traitement des valeurs manquantes
* Vérification de la cohérence et exploration statistique

---

### 🔍 Étape 2 — Modélisation

* Test de plusieurs algorithmes supervisés et non supervisés :

  * K-means
  * Régression logistique
  * KNN
  * Random Forest
* Comparaison des performances et choix du **meilleur modèle**
* Évaluation avec métriques pertinentes (accuracy, recall, F1-score, matrice de confusion)

---

### 📊 Étape 3 — Développement de l’application

* Création d’un **notebook Python interactif** permettant la prédiction de nouveaux billets
* Mise en place d’une interface simple pour saisir les caractéristiques et obtenir un résultat

---

### 🎤 Étape 4 — Présentation finale

* Support PowerPoint de **20 slides maximum**
* Contenu :

  * Méthodologie de collecte et préparation des données
  * Comparaison et résultats des algorithmes testés
  * Choix du modèle final et justification
  * Démonstration de l’application fonctionnelle

---

## 📦 Livrables finaux

* ✔️ Notebook Python contenant les **prétraitements et tests des différents algorithmes**
* ✔️ Notebook Python contenant l’**application finale pour tester les billets**
* ✔️ **Présentation PowerPoint** (20 slides) incluant méthodologie, résultats et application
