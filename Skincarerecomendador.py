import streamlit as st

# =============================
# CONFIGURACIÓN DE LA PÁGINA
# =============================
st.set_page_config(
    page_title="Recomendador de Skincare",
    page_icon="🌸",
    layout="centered"
)

# =============================
# ESTILOS VISUALES
# =============================
st.markdown("""
<style>
    .main-title {
        text-align: center;
        color: #D81E5B;
        font-size: 42px;
        font-weight: bold;
    }
    .subtitle {
        text-align: center;
        color: #555;
        font-size: 18px;
        margin-bottom: 25px;
    }
    .result-box {
        background-color: #FFF3EE;
        border-left: 6px solid #D81E5B;
        padding: 18px;
        border-radius: 12px;
        margin-top: 18px;
    }
    .warning-box {
        background-color: #FFF8E1;
        border-left: 6px solid #F9A825;
        padding: 14px;
        border-radius: 10px;
        color: #5D4037;
        margin-top: 18px;
    }
</style>
""", unsafe_allow_html=True)

# =============================
# BASE DE PRODUCTOS EJEMPLO
# =============================
productos = {
    "limpiador_suave": "SKIN1004 Madagascar Centella Ampoule Foam",
    "hidratante_ligera": "SKIN1004 Hyalu-Cica Moisture Cream",
    "protector_glow": "SKIN1004 Hyalu-Cica Water-Fit Sun Serum SPF50+ PA++++",
    "protector_control_grasa": "CELIMAX Oil Control Light Sunscreen",
    "protector_barra": "Tocobo Cotton Soft Sun Stick SPF50+ PA++++",
    "esencia_reparadora": "COSRX Advanced Snail 96 Mucin Power Essence",
    "protector_hidratante": "Tocobo Bio Watery Sun Cream SPF50+ PA++++"
}

# =============================
# FUNCIÓN RECOMENDADORA
# =============================
def recomendar_rutina(tipo_piel, preocupacion, sensibilidad):
    rutina = []
    explicacion = []

    # Paso 1: limpieza
    rutina.append(("1. Limpieza", productos["limpiador_suave"]))
    explicacion.append("Una limpieza suave ayuda a retirar grasa, sudor, protector solar e impurezas sin dejar la piel tirante.")

    # Paso 2: tratamiento o hidratación según preocupación
    if preocupacion == "Deshidratación o piel apagada":
        rutina.append(("2. Esencia hidratante", productos["esencia_reparadora"]))
        explicacion.append("Para piel apagada o deshidratada, conviene priorizar hidratación y reparación de barrera.")
    elif preocupacion == "Sensibilidad o rojez":
        rutina.append(("2. Hidratante calmante", productos["hidratante_ligera"]))
        explicacion.append("Si hay sensibilidad, es mejor mantener una rutina corta y enfocada en calmar la piel.")
    elif preocupacion == "Grasa o brillo excesivo":
        rutina.append(("2. Hidratante ligera", productos["hidratante_ligera"]))
        explicacion.append("La piel grasa también necesita hidratación; saltarla puede hacer que la piel se sienta más desequilibrada.")
    else:
        rutina.append(("2. Hidratante", productos["hidratante_ligera"]))
        explicacion.append("Una hidratante ligera ayuda a mantener la barrera cutánea estable.")

    # Paso 3: protector solar según tipo de piel
    if tipo_piel == "Grasa" or preocupacion == "Grasa o brillo excesivo":
        rutina.append(("3. Protector solar", productos["protector_control_grasa"]))
        explicacion.append("Para piel grasa, conviene buscar texturas ligeras y con acabado menos brillante.")
    elif tipo_piel == "Seca" or preocupacion == "Deshidratación o piel apagada":
        rutina.append(("3. Protector solar", productos["protector_hidratante"]))
        explicacion.append("Para piel seca o deshidratada, puede funcionar mejor un protector con sensación hidratante.")
    elif tipo_piel == "Mixta":
        rutina.append(("3. Protector solar", productos["protector_glow"]))
        explicacion.append("Para piel mixta, una textura ligera puede equilibrar comodidad e hidratación.")
    else:
        rutina.append(("3. Protector solar", productos["protector_glow"]))
        explicacion.append("El protector solar diario es clave dentro de una rutina básica de cuidado facial.")

    # Recomendación extra
    extra = None
    if preocupacion == "Reaplicación durante el día":
        extra = productos["protector_barra"]

    # Ajuste por sensibilidad
    if sensibilidad == "Sí, mi piel se irrita fácilmente":
        nota_sensibilidad = "Como tu piel es sensible, introduce los productos uno por uno y evita combinar demasiados activos al inicio."
    else:
        nota_sensibilidad = "Puedes iniciar con esta rutina básica y ajustar según cómo responda tu piel."

    return rutina, explicacion, extra, nota_sensibilidad

# =============================
# INTERFAZ PRINCIPAL
# =============================
st.markdown('<div class="main-title">🌸 Recomendador de Skincare</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Responde unas preguntas y recibe una rutina básica personalizada.</div>', unsafe_allow_html=True)

st.markdown("### 1. Cuéntanos sobre tu piel")

tipo_piel = st.selectbox(
    "¿Cuál es tu tipo de piel?",
    ["Grasa", "Mixta", "Seca", "Normal", "No estoy segura"]
)

preocupacion = st.selectbox(
    "¿Cuál es tu principal preocupación?",
    [
        "Grasa o brillo excesivo",
        "Deshidratación o piel apagada",
        "Sensibilidad o rojez",
        "Reaplicación durante el día",
        "Solo quiero una rutina básica"
    ]
)

sensibilidad = st.radio(
    "¿Tu piel se irrita fácilmente?",
    ["Sí, mi piel se irrita fácilmente", "No, normalmente tolero bien los productos"]
)

edad = st.slider("¿Qué edad tienes?", 13, 60, 23)

st.markdown("---")

if st.button("Generar mi rutina"):
    rutina, explicacion, extra, nota_sensibilidad = recomendar_rutina(tipo_piel, preocupacion, sensibilidad)

    st.markdown("## ✨ Tu rutina recomendada")

    st.markdown('<div class="result-box">', unsafe_allow_html=True)
    st.write(f"**Tipo de piel:** {tipo_piel}")
    st.write(f"**Preocupación principal:** {preocupacion}")
    st.write(f"**Edad:** {edad} años")
    st.markdown('</div>', unsafe_allow_html=True)

    for paso, producto in rutina:
        st.markdown(f"### {paso}")
        st.write(f"**Producto sugerido:** {producto}")

    if extra:
        st.markdown("### Extra recomendado")
        st.write(f"**Para reaplicar protector durante el día:** {extra}")

    st.markdown("## ¿Por qué esta rutina?")
    for texto in explicacion:
        st.write(f"- {texto}")

    st.info(nota_sensibilidad)

    st.markdown("""
    <div class="warning-box">
    ⚠️ Esta recomendación es orientativa y no reemplaza la evaluación de un dermatólogo. Si tienes acné severo, ardor persistente, alergias, rosácea diagnosticada, embarazo o tratamiento médico, consulta con un profesional.
    </div>
    """, unsafe_allow_html=True)

    st.success("Rutina generada correctamente 🌸")

# =============================
# PIE DE PÁGINA
# =============================
st.markdown("---")
st.caption("Proyecto creado con Streamlit para recomendación básica de skincare.")
