import streamlit as st
import folium
from streamlit_folium import st_folium
st.set_page_config(
    page_title="Portfolio-Seydina Alioune Diop",
    page_icon="🌍",
    layout="wide"
)
st.title("🌍 Portfolio - Géomatique & Développement")
st.subheader("Étudiant en BTS Géomatique | Passionné par les données géospatiales et le développement")
st.divider()
st.header("👤 À propos de moi")
st.write("""
Je suis étudiant en BTS Géomatique avec un fort intérêt pour :
- **Les satellites** et l'observation de la Terre
- Le **traitement des données avec une légère préférence géospatiales**
- La **sécurité des données géospatiales**
- Le **développement d'applications** (web et data)

Je combine des compétences en **SIG** (ArcGIS, QGIS) avec des compétences en **programmation** 
(Python, JavaScript, React) pour créer des solutions innovantes.
""")
col1, col2 = st.columns([7, 3])

with col1:
    st.markdown("### 🎓 Formation et Diplomes")
    st.markdown("Baccalauréat Scientifique")
    st.write("**BTS Géomatique** - En cours")


with col2:
    st.markdown("### 📍 Localisation")
    st.write("Dakar, Sénégal")
st.divider()
st.header("💡 Compétences Techniques")
col_gauche, col_droite = st.columns(2)

with col_gauche:
    st.subheader("🗺️ SIG & Géomatique")
    
    st.write("**ArcGIS**")
    st.progress(0.4)
    
    st.write("**QGIS**")
    st.progress(0.5)
    
    st.write("**AutoCAD**")
    st.progress(0.3)
      
    st.write("**SketchUp**")
    st.progress(0.2)

with col_droite:
    st.subheader("💻 Programmation & Dev")
    
    st.write("**Python**")
    st.progress(0.4)
    
    st.write("**JavaScript / React**")
    st.progress(0.4)
    
    st.write("**HTML / CSS**")
    st.progress(0.5)
st.divider()
st.header("🚀 Mes Projets")

st.info("📂 Section en construction - Projets à ajouter prochainement")

st.write("""
**Projets à venir :**
- Dashboard immobilier (React + Vite + JavaScript)
- Projets de cartographie (ArcGIS, QGIS)
- Analyses de données géospatiales
- Traitement d'images satellites
""")
st.divider()
st.header("🗺️ Démonstration Interactive")
st.write("**Carte interactive de Dakar** - Exemple de visualisation géospatiale avec Python")
carte = folium.Map(
    location=[14.7167, -17.4677],
    zoom_start=12,
    tiles="OpenStreetMap"
)
points_interet = [
    {"nom": "Dakar Plateau", "coords": [14.6928, -17.4467], "desc": "Centre administratif"},
    {"nom": "Corniche", "coords": [14.7128, -17.4719], "desc": "Front de mer"},
    {"nom": "Île de Gorée", "coords": [14.6679, -17.3981], "desc": "Site UNESCO"},
    {"nom": "Monument Renaissance", "coords": [14.7169, -17.5089], "desc": "Monument iconique"},
]
for point in points_interet:
    folium.Marker(
        location=point["coords"],
        popup=f"<b>{point['nom']}</b><br>{point['desc']}",
        tooltip=point["nom"],
        icon=folium.Icon(color='green', icon='info-sign')
    ).add_to(carte)

st_folium(carte, width=700, height=500)

st.divider()
st.header("📧 Contact")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("**GitHub**")
    st.write("github.com/SeydinaAliouneDiop")

with col2:
    st.write("**LinkedIn**")
    st.write("linkedin.com/in/Seydina Diop")

with col3:
    st.write("**Email**")
    st.write("seydinadioppro99@gmail.com")