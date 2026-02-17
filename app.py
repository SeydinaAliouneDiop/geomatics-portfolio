import streamlit as st

st.set_page_config(
    page_title="CV - Seydina Alioune Diop",
    page_icon="🌍",
    layout="wide"
)

st.markdown("""
<style>
    section[data-testid="stSidebar"] { background-color: #1b2838; }
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] li,
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] div { color: #dde3ea !important; }
    section[data-testid="stSidebar"] h3 { color: #ffffff !important; }
    section[data-testid="stSidebar"] a { color: #5dade2 !important; }

    .sidebar-name {
        padding: 20px 12px;
        background: linear-gradient(135deg, #1e8449, #27ae60);
        border-radius: 8px;
        text-align: center;
        margin-bottom: 16px;
    }
    .sidebar-name h1 { color: #fff !important; font-size: 1.1rem; font-weight: 800; margin: 0 0 4px 0; line-height: 1.4; }
    .sidebar-name p  { color: #d5f5e3 !important; font-size: 0.8rem; margin: 0; font-style: italic; }

    .section-title {
        font-size: 0.72rem;
        font-weight: 800;
        color: #1b2838;
        text-transform: uppercase;
        letter-spacing: 2px;
        border-bottom: 2px solid #27ae60;
        padding-bottom: 4px;
        margin: 24px 0 12px 0;
    }
    .project-block {
        border-left: 3px solid #27ae60;
        padding: 10px 16px;
        background-color: #f9fafb;
        border-radius: 0 6px 6px 0;
    }
    .tool-tag {
        display: inline-block;
        background-color: #eaf4fb;
        color: #1a5276 !important;
        padding: 3px 12px;
        border-radius: 4px;
        font-size: 0.82rem;
        font-weight: 600;
        border: 1px solid #aed6f1;
        margin: 3px 3px 3px 0;
    }
    .cv-footer {
        text-align: center;
        font-size: 0.82rem;
        color: #95a5a6;
        padding: 20px 0 8px 0;
        border-top: 1px solid #ecf0f1;
        margin-top: 28px;
    }
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════
# SIDEBAR
# ═══════════════════════════════════════════════════════
with st.sidebar:

    st.markdown("""
    <div class="sidebar-name">
        <h1>Seydina Alioune<br>DIOP</h1>
        <p>Technicien Supérieur en Géomatique</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Contact")
    st.markdown("📞 +221 76 774 54 56")
    st.markdown("📧 seydinadioppro99@gmail.com")
    st.markdown("📍 Dakar, Sénégal")
    st.markdown("💼 [linkedin.com/in/seydina-diop](https://linkedin.com/in/seydina-diop)")
    st.markdown("💻 [github.com/SeydinaAliouneDiop](https://github.com/SeydinaAliouneDiop)")

    st.markdown("---")

    st.markdown("### Formation")
    st.markdown("**BTS Géomatique** *(en cours)*  \n2024 – 2026")
    st.markdown("**Baccalauréat Scientifique**  \n2023 ")


# ═══════════════════════════════════════════════════════
# CONTENU PRINCIPAL
# ═══════════════════════════════════════════════════════

st.markdown("# Seydina Alioune DIOP")
st.markdown("**Technicien Supérieur en Géomatique — Cartographie Web & Développement SIG**")

st.divider()

# ── PROFIL ──────────────────────────────────────────────
st.markdown('<p class="section-title">Profil</p>', unsafe_allow_html=True)
st.write(
    "Technicien Supérieur en Géomatique, je conçois des applications cartographiques interactives "
    "à l'intersection des systèmes d'information géographique et du développement web. "
    "Rigoureux et autonome, je m'adapte rapidement à de nouveaux environnements techniques."
)

# ── COMPÉTENCES ─────────────────────────────────────────
st.markdown('<p class="section-title">Compétences</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Systèmes d'Information Géographique**")
    st.markdown("""
- Acquisition, structuration et contrôle qualité de données géospatiales
- Analyse spatiale : jointures, intersections, zones tampon, superpositions
- Cartographie thématique et mise en page de cartes
- Télédétection et interprétation d'images satellitaires
- Gestion et interrogation de bases de données spatiales
    """)

with col2:
    st.markdown("**Cartographie Web & Développement**")
    st.markdown("""
- Conception d'interfaces cartographiques interactives
- Intégration de couches vectorielles et raster dans un navigateur
- Développement de dashboards de visualisation de données géospatiales
- Automatisation du traitement de données géographiques
- Conception d'interfaces responsive (mobile-first)
    """)

# ── OUTILS & TECHNOLOGIES ───────────────────────────────
st.markdown('<p class="section-title">Outils & Technologies</p>', unsafe_allow_html=True)
st.markdown("""
<span class="tool-tag">QGIS</span>
<span class="tool-tag">ArcGIS</span>
<span class="tool-tag">AutoCAD</span>
<span class="tool-tag">Python</span>
<span class="tool-tag">JavaScript</span>
<span class="tool-tag">HTML / CSS</span>
<span class="tool-tag">SQL</span>
<span class="tool-tag">Git / GitHub</span>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── PROJETS ─────────────────────────────────────────────
st.markdown('<p class="section-title">Projet Réalisé</p>', unsafe_allow_html=True)

st.markdown("""
<div class="project-block">
    <strong>Dashboard Immobilier Interactif</strong><br><br>
    Application web de visualisation de biens immobiliers avec carte interactive.
    Mise en place d'un système de filtres multicritères (type de bien, fourchette de prix, localisation),
    d'une carte avec marqueurs dynamiques et d'un tableau de bord statistiques en temps réel.
    Interface responsive adaptée aux usages mobiles.
    <br><br>
    <em style="color:#566573; font-size:0.83rem;">Technologies : React · JavaScript · Leaflet.js · CSS</em>
    <br>
    <a href="https://real-estate-dashboard-eihw.onrender.com" target="_blank" style="font-size:0.83rem; color:#2980b9;">🔗 Démo live</a>
    &nbsp;&nbsp;
    <a href="https://github.com/SeydinaAliouneDiop/real-estate-dashboard" target="_blank" style="font-size:0.83rem; color:#2980b9;">💻 Code source</a>
</div>
""", unsafe_allow_html=True)

