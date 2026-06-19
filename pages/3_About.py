import streamlit as st


# ==========================================
# ABOUT THE MODE-RN
# ==========================================

st.markdown("""
<div style="
background:white;
padding:50px;
border-radius:24px;
border:1px solid #E5DDD0;
margin-top:30px;
margin-bottom:40px;
">

<h1 style="
text-align:center;
font-family:Georgia, serif;
font-size:3rem;
font-weight:300;
letter-spacing:4px;
margin-bottom:30px;
">
ABOUT THE MODE-RN
</h1>

<p style="
max-width:900px;
margin:auto;
font-size:18px;
line-height:1.9;
text-align:center;
color:#333333;
">
<strong>The Mode-RN</strong> nasce de um jogo de palavras entre
<i>The Mode Right Now</i> — “o modo de agora” — e a pronúncia da palavra
<i>Modern</i>. O nome traduz a proposta da plataforma: observar o presente
para compreender os sinais que apontam para o futuro.

<br><br>

Em um cenário de informação cada vez mais acelerado, acompanhar tendências
exige mais do que consumir notícias isoladas. O The Mode-RN reúne conteúdos
de veículos especializados em moda, comportamento e consumo, transformando
diferentes perspectivas em uma experiência de pesquisa organizada, visual e acessível.

<br><br>

Ao centralizar e explorar essas narrativas, a plataforma permite identificar
temas emergentes, movimentos culturais e mudanças de comportamento que ajudam
a compreender o cenário contemporâneo.
</p>

</div>
""", unsafe_allow_html=True)

# ==========================================
# FGV BANNER
# ==========================================

left, center, right = st.columns([0.05, 1.9, 0.05])

with center:
    st.image(
        "fgv-rj (1) (1).jpeg",
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
Developed by students of FGV Communication Rio as part of the
Programming course taught by Professor Josir Gomes.
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

col1, spacer, col2 = st.columns([1,0.3,1])

with col1:

    st.image(
    "fotositesofia.jpeg",
    use_container_width=True
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
    Estudante de Comunicação na FGV com interesse em moda,
    comportamento digital, consumo e pesquisa de tendências.
    </p>

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.image(
    "fotoluizapb.jpg",
    use_container_width=True
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
    Estudante de Comunicação na FGV com interesse em moda,
    comportamento digital, consumo e pesquisa de tendências.
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
Tracking the conversations shaping the future of fashion and culture.
</p>

</div>
""", unsafe_allow_html=True)
