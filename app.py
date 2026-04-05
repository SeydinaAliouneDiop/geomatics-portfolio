import streamlit as st

st.set_page_config(
    page_title="CV - Seydina Alioune Diop",
    page_icon="🌍",
    layout="wide"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Inter:wght@400;500&display=swap');

    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

    section[data-testid="stSidebar"] { background-color: #0f1f14; }
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] li,
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] div { color: #ccddd0 !important; }
    section[data-testid="stSidebar"] h3 { color: #ffffff !important; letter-spacing: 1px; }
    section[data-testid="stSidebar"] a { color: #4ade80 !important; }

    .sidebar-name {
        padding: 24px 14px;
        background: linear-gradient(135deg, #166534, #15803d, #16a34a);
        border-radius: 10px;
        text-align: center;
        margin-bottom: 18px;
        box-shadow: 0 4px 20px rgba(22,101,52,0.4);
    }
    .sidebar-name h1 {
        color: #fff !important;
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.15rem;
        font-weight: 700;
        margin: 0 0 4px 0;
        line-height: 1.4;
        letter-spacing: 0.5px;
    }
    .sidebar-name p { color: #bbf7d0 !important; font-size: 0.78rem; margin: 0; font-style: italic; }

    .cv-link-badge {
        display: block;
        background: linear-gradient(135deg, #14532d, #166534);
        border: 1px solid #22c55e;
        border-radius: 8px;
        padding: 10px 14px;
        text-align: center;
        margin: 8px 0;
        text-decoration: none !important;
        color: #bbf7d0 !important;
        font-size: 0.8rem;
        font-weight: 600;
        letter-spacing: 0.5px;
        transition: all 0.2s;
    }
    .cv-link-badge:hover { background: #16a34a; border-color: #4ade80; }

    .section-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 0.7rem;
        font-weight: 700;
        color: #166534;
        text-transform: uppercase;
        letter-spacing: 3px;
        border-bottom: 2px solid #16a34a;
        padding-bottom: 5px;
        margin: 28px 0 14px 0;
    }

    .project-block {
        border-left: 3px solid #16a34a;
        padding: 14px 18px;
        background: linear-gradient(to right, #f0fdf4, #ffffff);
        border-radius: 0 8px 8px 0;
        margin-bottom: 14px;
        box-shadow: 0 1px 6px rgba(0,0,0,0.05);
    }
    .project-block h4 {
        margin: 0 0 6px 0;
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1rem;
        color: #14532d;
    }
    .project-highlight {
        border-left: 3px solid #f59e0b;
        background: linear-gradient(to right, #fffbeb, #ffffff);
    }
    .project-highlight h4 { color: #92400e; }

    .tool-tag {
        display: inline-block;
        background-color: #f0fdf4;
        color: #166534 !important;
        padding: 4px 12px;
        border-radius: 4px;
        font-size: 0.8rem;
        font-weight: 600;
        border: 1px solid #86efac;
        margin: 3px 3px 3px 0;
    }
    .tool-tag-ai {
        display: inline-block;
        background-color: #eff6ff;
        color: #1e40af !important;
        padding: 4px 12px;
        border-radius: 4px;
        font-size: 0.8rem;
        font-weight: 600;
        border: 1px solid #93c5fd;
        margin: 3px 3px 3px 0;
    }

    .vision-box {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a2f 100%);
        border-radius: 10px;
        padding: 20px 24px;
        color: #e2e8f0;
        border: 1px solid #166534;
        margin: 10px 0 20px 0;
    }
    .vision-box h4 {
        color: #4ade80;
        font-family: 'Space Grotesk', sans-serif;
        margin: 0 0 10px 0;
        font-size: 0.9rem;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    .vision-box p { color: #cbd5e1; font-size: 0.9rem; line-height: 1.7; margin: 0; }

    .cv-footer {
        text-align: center;
        font-size: 0.8rem;
        color: #94a3b8;
        padding: 20px 0 8px 0;
        border-top: 1px solid #e2e8f0;
        margin-top: 32px;
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

    st.markdown("### 📬 Contact")
    st.markdown("📞 +221 76 774 54 56")
    st.markdown("📧 seydinadioppro99@gmail.com")
    st.markdown("📍 Dakar, Sénégal")

    st.markdown("---")

    st.markdown("### 🔗 Liens")
    st.markdown("""
    <a class="cv-link-badge" href="https://seydinaaliounediop.streamlit.app/" target="_blank">
        🌐 CV Interactif (Streamlit)
    </a>
    <a class="cv-link-badge" href="https://linkedin.com/in/seydina-diop" target="_blank">
        💼 LinkedIn
    </a>
    <a class="cv-link-badge" href="https://github.com/SeydinaAliouneDiop" target="_blank">
        💻 GitHub — Voir mes projets
    </a>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 🎓 Formation")
    st.markdown("""
**BTS Géomatique** *(en cours)*  
2025 – 2027  
*Systèmes d'information géographique, cartographie, télédétection*
""")
    st.markdown("""
**Baccalauréat Scientifique (S)**  
2024  
*Solide base en mathématiques, physique et sciences*
""")


# ═══════════════════════════════════════════════════════
# CONTENU PRINCIPAL
# ═══════════════════════════════════════════════════════

st.markdown("# Seydina Alioune DIOP")
st.markdown("**Technicien Supérieur en Géomatique — Data Géospatiale · Cartographie Web · IA appliquée au SIG**")

st.divider()

# ── PROFIL ──────────────────────────────────────────────
st.markdown('<p class="section-title">Profil</p>', unsafe_allow_html=True)
st.write(
    "Technicien Supérieur en Géomatique, je conçois des applications cartographiques interactives "
    "à l'intersection des systèmes d'information géographique, de la data science et du développement web. "
    "Convaincu que la donnée géospatiale et l'intelligence artificielle sont les prochains leviers de transformation "
    "du territoire africain, j'oriente activement ma pratique vers l'analyse de données spatiales, "
    "la visualisation intelligente et l'automatisation au service de la prise de décision. "
    "Rigoureux, autonome et curieux, je m'adapte rapidement aux environnements techniques exigeants."
)

# ── AUTODIDAXIE ─────────────────────────────────────────
st.markdown('<p class="section-title">Apprentissage Autodidacte</p>', unsafe_allow_html=True)
st.markdown("""
<div style="background:#f8fafc; border-radius:8px; padding:16px 20px; border:1px solid #e2e8f0; margin-bottom:8px;">
    <strong>🧠 Formation par la pratique</strong><br><br>
    Au-delà du cursus académique en géomatique, j'ai appris de façon entièrement autonome 
    la majorité des langages et frameworks que j'utilise aujourd'hui : 
    <strong>HTML, CSS, JavaScript, TypeScript, Python, React, Flask, SQL</strong> — 
    à travers des ressources en ligne, de la documentation et surtout la pratique directe.
    <br><br>
    Les projets présentés ci-dessous sont nés de cet apprentissage par l'action : 
    chaque outil maîtrisé a été mis en œuvre sur un projet concret, 
    du prototype local jusqu'au déploiement en production sur le web.
    Cette capacité à apprendre vite, seul, et à produire des résultats réels 
    est l'une de mes forces les plus solides.
</div>
""", unsafe_allow_html=True)

# ── VISION DATA & IA ────────────────────────────────────
st.markdown("""
<div class="vision-box">
    <h4>🔭 Vision — Data Géospatiale & Intelligence Artificielle</h4>
    <p>
    La géomatique entre dans une nouvelle ère : les données satellitaires massives, les modèles d'apprentissage 
    automatique et les bases de données spatiales transforment notre capacité à comprendre et gérer les territoires. 
    Je m'investis dans cette convergence — entre SIG traditionnel et IA — pour développer des outils 
    qui répondent aux défis concrets de l'Afrique : urbanisation, gestion des infrastructures, 
    événements sportifs à grande échelle comme les Jeux Olympiques de la Jeunesse de Dakar 2026.
    </p>
</div>
""", unsafe_allow_html=True)

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
- Gestion et interrogation de bases de données spatiales (PostGIS)
    """)
    st.markdown("**Data & Intelligence Artificielle**")
    st.markdown("""
- Traitement et visualisation de données géospatiales volumineuses
- Initiation au Machine Learning appliqué aux données territoriales
- Automatisation des pipelines de données géographiques
- Exploration des LLM et outils IA pour l'analyse de territoire
    """)

with col2:
    st.markdown("**Cartographie Web & Développement**")
    st.markdown("""
- Conception d'interfaces cartographiques interactives (Leaflet.js)
- Intégration de couches vectorielles et raster dans un navigateur
- Développement de dashboards de visualisation géospatiale
- API REST pour la collecte et diffusion de données spatiales
- Conception d'interfaces responsive (mobile-first)
    """)

# ── OUTILS & TECHNOLOGIES ───────────────────────────────
st.markdown('<p class="section-title">Outils & Technologies</p>', unsafe_allow_html=True)

st.markdown("**SIG & Cartographie**")
st.markdown("""
<span class="tool-tag">QGIS</span>
<span class="tool-tag">ArcGIS</span>
<span class="tool-tag">AutoCAD</span>
<span class="tool-tag">Leaflet.js</span>
<span class="tool-tag">PostGIS</span>
""", unsafe_allow_html=True)

st.markdown("**Développement**")
st.markdown("""
<span class="tool-tag">Python</span>
<span class="tool-tag">JavaScript</span>
<span class="tool-tag">React</span>
<span class="tool-tag">Flask</span>
<span class="tool-tag">HTML / CSS</span>
<span class="tool-tag">SQL</span>
<span class="tool-tag">Git / GitHub</span>
""", unsafe_allow_html=True)

st.markdown("**Data & IA (en apprentissage actif)**")
st.markdown("""
<span class="tool-tag-ai">Pandas / GeoPandas</span>
<span class="tool-tag-ai">Streamlit</span>
<span class="tool-tag-ai">Machine Learning</span>
<span class="tool-tag-ai">API REST</span>
<span class="tool-tag-ai">PostgreSQL</span>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── PROJETS ─────────────────────────────────────────────
st.markdown('<p class="section-title">Projets Réalisés</p>', unsafe_allow_html=True)

st.markdown("""
<div class="project-block project-highlight">
    <h4>🗺️ Plateforme de Signalement Géolocalisé — ZAC de Mbao, Dakar</h4>
    <p>
        Application web full-stack permettant aux citoyens de signaler des incidents géolocalisés 
        sur le territoire de la Zone d'Aménagement Concerté de Mbao (Dakar). 
        Les signalements sont stockés dans une base de données spatiale (PostgreSQL + PostGIS), 
        visualisés en temps réel sur une carte interactive, et consultables via une interface web déployée.
        <br><br>
        Ce projet illustre directement l'application de la géomatique et de la data au service 
        d'une collectivité sénégalaise — exactement le type d'outil pertinent dans le contexte 
        d'un grand événement urbain comme les JOJ 2026.
    </p>
    <br>
    <em style="color:#92400e; font-size:0.83rem;">Technologies : Flask · Leaflet.js · PostgreSQL · PostGIS · Python · HTML/CSS</em>
    <br>
    <small style="color:#9ca3af; font-size:0.75rem;">
        ⚠️ La démo est hébergée sur le plan gratuit de Render — la base de données coupe les connexions après inactivité, 
        ce qui peut empêcher l'envoi de signalements. La carte de visualisation reste fonctionnelle. 
        Le code source complet est disponible sur GitHub.
    </small>
    <br><br>
    <a href="https://carte-signalements-mbao-1.onrender.com" target="_blank" style="font-size:0.83rem; color:#b45309;">🔗 Démo live</a>
    &nbsp;&nbsp;
    <a href="https://github.com/SeydinaAliouneDiop/CARTE-SIGNALEMENTS-MBAO" target="_blank" style="font-size:0.83rem; color:#b45309;">💻 Code source GitHub</a>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="project-block">
    <h4>🏠 Dashboard Immobilier Interactif</h4>
    <p>
        Application web de visualisation de biens immobiliers avec carte interactive.
        Mise en place d'un système de filtres multicritères (type de bien, fourchette de prix, localisation),
        d'une carte avec marqueurs dynamiques et d'un tableau de bord statistiques en temps réel.
        Interface responsive adaptée aux usages mobiles.
    </p>
    <br>
    <em style="color:#566573; font-size:0.83rem;">Technologies : React · JavaScript · Leaflet.js · CSS</em>
    <br><br>
    <a href="https://real-estate-dashboard-eihw.onrender.com" target="_blank" style="font-size:0.83rem; color:#2980b9;">🔗 Démo live</a>
    &nbsp;&nbsp;
    <a href="https://github.com/SeydinaAliouneDiop/real-estate-dashboard" target="_blank" style="font-size:0.83rem; color:#2980b9;">💻 Code source</a>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="project-block">
    <h4>📊 CV Interactif — Portfolio Géomatique</h4>
    <p>
        Ce CV lui-même est une application web déployée, conçue avec Python et Streamlit.
        Il reflète mon approche : transformer des données et des contenus en interfaces 
        numériques accessibles, claires et déployées en ligne.
    </p>
    <br>
    <em style="color:#566573; font-size:0.83rem;">Technologies : Python · Streamlit · CSS</em>
    <br><br>
    <a href="https://seydinaaliounediop.streamlit.app/" target="_blank" style="font-size:0.83rem; color:#2980b9;">🌐 Voir en ligne</a>
    &nbsp;&nbsp;
    <a href="https://github.com/SeydinaAliouneDiop/geomatics-portfolio" target="_blank" style="font-size:0.83rem; color:#2980b9;">💻 Code source</a>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

col_gh1, col_gh2 = st.columns([2, 1])
with col_gh1:
    st.markdown("""
    **💡 Vous souhaitez explorer davantage ?**  
    Tous mes projets sont accessibles librement sur GitHub, avec leur code source documenté.  
    Je construis activement de nouveaux outils à l'intersection de la géomatique, de la data et de l'IA.
    """)
with col_gh2:
    st.link_button(
        "🔗 Visiter mon GitHub",
        "https://github.com/SeydinaAliouneDiop",
        use_container_width=True
    )

st.markdown('<p class="cv-footer">Seydina Alioune DIOP · Dakar, Sénégal · seydinadioppro99@gmail.com</p>', unsafe_allow_html=True)
