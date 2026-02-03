import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="CV - Seydina Alioune Diop",
    page_icon="🌍",
    layout="wide"
)

st.markdown("""
<style>
    .sidebar-content {
        background-color: #2c3e50;
        padding: 20px;
        border-radius: 10px;
        color: white;
    }
    .main-header {
        color: #2c3e50;
        border-bottom: 3px solid #27ae60;
        padding-bottom: 10px;
    }
    .section-header {
        color: #27ae60;
        margin-top: 20px;
        border-left: 4px solid #27ae60;
        padding-left: 10px;
    }
    .skill-item {
        margin: 10px 0;
    }
    .contact-info {
        background-color: #ecf0f1;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    

    st.image("https://via.placeholder.com/200", width=200)
    
    st.markdown("---")
    
    st.markdown("### 📋 INFORMATIONS")
    st.markdown("**Nom:** Seydina Alioune Diop")
    st.markdown(" Technicien Superieur en Geomatique")
    st.markdown("**Âge:** 20ans")
    st.markdown("**Localisation:** Dakar, Sénégal")
    
    st.markdown("---")
    
  
    st.markdown("### 📞 CONTACT")
    st.markdown("📧 seydinadioppro99@gmail.com")
    st.markdown("💼 [LinkedIn](https://linkedin.com/in/seydina-diop)")
    st.markdown("💻 [GitHub](https://github.com/SeydinaAliouneDiop)")
    
    st.markdown("---")
    
   
    st.markdown("### 🌐 LANGUES")
    st.markdown("**Français:** Courant")
    
    st.markdown("---")
    
    st.markdown("### 🎯 COMPÉTENCES CLÉS")
    st.markdown("""
    - Cartographie Web
    - Analyse Spatiale
    - Développement Frontend
    - Automatisation Python
    - Visualisation de Données
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)




st.divider()

st.markdown('<h2 class="section-header">👤 PROFIL PROFESSIONNEL</h2>', unsafe_allow_html=True)
st.write("""
Étudiant en BTS Géomatique passionné par l'intersection entre les systèmes d'information géographique 
et le développement web moderne. Spécialisé dans la création de solutions cartographiques interactives 
et l'automatisation du traitement de données géospatiales.

**Expertise principale :** Développement d'applications web de cartographie interactive combinant 
compétences SIG et programmation moderne (React, Python, Leaflet).
""")

st.divider()

st.markdown('<h2 class="section-header">🎓 FORMATION</h2>', unsafe_allow_html=True)

col1, col2 = st.columns([3, 7])
with col1:
    st.markdown("**2024 - 2026**")
with col2:
    st.markdown("**BTS Géomatique** ")
    st.write("Formation technique spécialisée en systèmes d'information géographique, cartographie et technologies géospatiales")
    st.write("*Compétences :* QGIS, ArcGIS, Python GIS, Télédétection, AutoCAD")

st.markdown("")

col1, col2 = st.columns([3, 7])
with col1:
    st.markdown("**2023-2024**")
with col2:
    st.markdown("**Baccalauréat Scientifique**")
    st.write("Diplôme obtenu avec mention")

st.divider()

st.markdown('<h2 class="section-header">🚀 PROJETS RÉALISÉS</h2>', unsafe_allow_html=True)

st.markdown("### 🏠 Dashboard Immobilier Interactif")
col1, col2 = st.columns([7, 3])
with col1:
    st.write("""
    Application web full-stack pour la visualisation de propriétés immobilières avec carte interactive.
    
    **Fonctionnalités :**
    - Carte Leaflet avec marqueurs personnalisés
    - Système de filtres avancés (type, prix, localisation)
    - Dashboard statistiques en temps réel
    - Design responsive mobile-first
    
    **Technologies :** React, JavaScript, Leaflet, CSS
    
    **Réalisation :** 1 semaine
    """)
with col2:
    st.info("🔗 [Démo Live](https://real-estate-dashboard-eihw.onrender.com)")
    st.info("💻 [Code Source](https://github.com/SeydinaAliouneDiop/real-estate-dashboard)")

st.markdown("---")

# Projet 2
st.markdown("### 🌍 Portfolio Géomatique Interactif")
col1, col2 = st.columns([7, 3])
with col1:
    st.write("""
    Site web de portfolio professionnel avec visualisation géospatiale interactive.
    
    **Fonctionnalités :**
    - Carte interactive de Dakar avec points d'intérêt
    - Présentation skills et projets
    - Interface responsive
    
    **Technologies :** Python, Streamlit, Folium
    """)
with col2:
    st.info("🔗 [Démo Live](https://geomatics-portfolio.onrender.com)")
    st.info("💻 [Code Source](https://github.com/SeydinaAliouneDiop/geomatics-portfolio)")

st.markdown("---")

st.divider()

st.markdown('<h2 class="section-header">💡 COMPÉTENCES TECHNIQUES</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### 🗺️ SIG & Géomatique")
    st.markdown("**QGIS** ")
    
    st.markdown("**ArcGIS** ")
    
    st.markdown("**AutoCAD** ")
    

with col2:
    st.markdown("#### 💻 Développement Web")
    st.markdown("**JavaScript/React** ")
    
    st.markdown("**HTML/CSS** ")
   
    st.markdown("**Leaflet** ")
    

with col3:
    st.markdown("#### 🐍 Programmation")
    st.markdown("**Python** ")
    
    st.markdown("**Git/GitHub** ")
    
    st.markdown("**Streamlit** ")
    
st.divider()

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #7f8c8d; padding: 20px;'>
    <p>💼 <b>Disponible pour missions freelance et stages</b></p>
    <p>Spécialisé en : Cartographie Web • Automatisation SIG • Visualisation de Données Géospatiales</p>
    <p>📧 seydinadioppro99@gmail.com | 💻 GitHub: SeydinaAliouneDiop</p>
</div>
""", unsafe_allow_html=True)