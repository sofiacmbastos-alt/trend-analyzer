import streamlit as st


# ==========================================
# ABOUT THE MODE-RN
# ==========================================

st.markdown("""
<div style="
text-align:center;
margin-top:60px;
margin-bottom:40px;
">

<h2 style="
font-family: Georgia, serif;
font-weight: 400;
font-size: 2.6rem;
letter-spacing: 2px;
margin-bottom: 20px;
">
ABOUT
</h2>

<p style="
max-width:750px;
margin:auto;
line-height:1.9;
color:#444;
font-size:1.05rem;
">

A Mode-RN nasce como um espaço de leitura do presente.<br><br>

Mais do que acompanhar a moda, o projeto observa os sistemas que a atravessam — 
o comportamento digital, as dinâmicas de consumo e as formas contemporâneas de circulação de imagem e desejo.<br><br>

A moda é entendida aqui não apenas como estética, mas como linguagem cultural em constante transformação,
um campo onde identidade, mídia e mercado se reorganizam continuamente.<br><br>

Entre análise e curadoria, o projeto busca organizar fragmentos do agora para compreender os sentidos que estão sendo construídos.

</p>

</div>
""", unsafe_allow_html=True)

# ==========================================
# FGV BANNER
# ==========================================
st.markdown("""
<div style="
text-align:center;
margin-bottom:20px;
">

<p style="
text-transform:uppercase;
letter-spacing:3px;
font-size:0.85rem;
color:#7A7268;
">
Projeto Acadêmico
</p>

</div>
""", unsafe_allow_html=True)

st.image(
        "fotogv.jpeg",
        use_container_width=True
    )

st.markdown("""
<div style="
max-width:850px;
margin:auto;
text-align:center;
padding-top:20px;
padding-bottom:60px;
">

<p style="
font-size:16px;
line-height:1.8;
color:#555555;
">
Desenvolvido por estudantes de Comunicação da FGV Rio, o The Mode-RN surgiu no contexto da disciplina de Programação, ministrada pelo professor Josir Gomes.
</p>

</div>
""", unsafe_allow_html=True)

# ==========================================
# TEAM TITLE
# ==========================================

st.markdown("""
<h2 style="
text-align:center;
font-family:Georgia, serif;
font-size:2.2rem;
font-weight:300;
letter-spacing:3px;
margin-bottom:40px;
">
DEVELOPERS
</h2>
""", unsafe_allow_html=True)


# ==========================================
# TEAM MEMBERS
# ==========================================

col1, spacer, col2 = st.columns([0.9,0.25,0.9])

with col1:

    st.image(
        "fotositesofia.jpeg",
        width=250
    )

    st.markdown("""
    <div style="
    text-align:center;
    padding-top:15px;
    padding-bottom:30px;
    ">

    <h3 style="
    font-family:Georgia, serif;
    font-weight:400;
    ">
    <a href="https://br.linkedin.com/in/sofiacmbastos"
    target="_blank"
    style="
    text-decoration:none;
    color:black;
    ">
    Sofia Bastos 
    </a>
    </h3>

    <p style="
    max-width:350px;
    margin:auto;
    line-height:1.8;
    color:#555555;
    ">
    Estudante de Comunicação na FGV com atenção à moda contemporânea como expressão cultural, em diálogo com comportamento digital e práticas de consumo.
    </p>
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.image(
        "fotoluizapb.jpg",
        width=250
    )

    st.markdown("""
    <div style="
    text-align:center;
    padding-top:15px;
    padding-bottom:30px;
    ">

    <h3 style="
    font-family:Georgia, serif;
    font-weight:400;
    ">
    <a href="https://www.linkedin.com/in/luiza-seda-011472389/"
    target="_blank"
    style="
    text-decoration:none;
    color:black;
    ">
    Luiza Seda 
    </a>
    </h3>

    <p style="
    max-width:350px;
    margin:auto;
    line-height:1.8;
    color:#555555;
    ">
    Estudante de Comunicação na FGV com interesse em comunicação, comportamento digital e consumo.
    </p>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# QUOTE
# ==========================================

st.markdown("""
<div style="
text-align:center;
padding-top:80px;
font-size:1rem;
">

<p style="
font-family:Georgia, serif;
font-size:1.25rem;
font-style:italic;
color:#444444;
letter-spacing:0.5px;
">
Understanding today's signals to anticipate tomorrow's culture.
</p>

</div>
""", unsafe_allow_html=True)
