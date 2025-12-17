import streamlit as st
import pandas as pd
import pickle
import numpy as np
import io
from sklearn.preprocessing import StandardScaler # Gardez-le au cas où vous auriez besoin de normaliser manuellement

# =========================================================================
# 1. FONCTION DE CLASSIFICATION
# =========================================================================

def classifier_billets(fichier_telecharge, chemin_modele_pkl="modele_logreg.pkl"):
    """
    Charge un modèle de classification logistique, lit le fichier CSV de billets,
    effectue les prédictions (classe et probabilité), et retourne le DataFrame mis à jour.
    """
    
    # --- 1. Chargement du Modèle ---
    try:
        with open(chemin_modele_pkl, "rb") as f:
            clf_loaded = pickle.load(f)
    except Exception as e:
        st.error(f"❌ Erreur lors du chargement du modèle : {e}")
        return None

    # --- 2. Lecture du Fichier CSV ---
    try:
        # st.upload_file retourne un objet que pandas peut lire
        df_billets_production = pd.read_csv(fichier_telecharge, sep=',', encoding='latin1')
        
    except Exception as e:
        st.error(f"❌ Erreur lors de la lecture du fichier CSV. Format incorrect ou encodage : {e}")
        return None

    # Préparation des données pour la prédiction
    df_billets_prediction = df_billets_production.copy()
    
    # Retirer la colonne 'id' si elle existe, car elle n'est pas une feature
    if 'id' in df_billets_prediction.columns:
        df_billets_prediction = df_billets_prediction.drop(columns=['id'])

    # --- 3. Prédiction ---
    try:
        # Le modèle doit gérer la normalisation des données tout seul (via un pipeline)
        y_pred = clf_loaded.predict(df_billets_prediction)
        y_proba = clf_loaded.predict_proba(df_billets_prediction)
    except Exception as e:
        st.error(f"❌ Erreur lors de la prédiction. Le modèle attend peut-être un format différent de colonnes : {e}")
        return None
    
    # --- 4. Ajout des résultats ---
    
    df_billets_production['is_genuine_pred'] = y_pred
    df_billets_production['is_genuine_proba'] = y_proba[:, 1]
    
    df_billets_production['interpretation'] = np.where(
        df_billets_production['is_genuine_pred'] == 1, 
        "Authentique", 
        "Contrefaçon"
    )

    return df_billets_production


# =========================================================================
# 2. CODE STREAMLIT (INTERFACE UTILISATEUR)
# =========================================================================

st.title("💸 Détection de Faux Billets")
st.markdown("Uploadez un fichier CSV pour classifier l'authenticité des billets.")

uploaded_file = st.file_uploader(
    "Téléchargez votre fichier CSV (colonnes de caractéristiques)", 
    type="csv"
)

if uploaded_file is not None:
    st.info("Fichier chargé. Exécution du modèle en cours...")
    
    df_resultat = classifier_billets(uploaded_file)
    
    if df_resultat is not None:
        
        st.header("Résultats")
        st.dataframe(df_resultat)
        
        st.markdown("---")
        
        @st.cache_data
        def convert_df_to_csv(df):
            # Utilisation du point-virgule comme séparateur pour éviter les confusions
            return df.to_csv(index=False, sep=';').encode('utf-8') 

        csv_download = convert_df_to_csv(df_resultat)

        st.download_button(
            label="⬇️ Télécharger le fichier de résultats (CSV)",
            data=csv_download,
            file_name='billets_classifies.csv',
            mime='text/csv',
        )