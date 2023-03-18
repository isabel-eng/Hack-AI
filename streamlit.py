import streamlit as st


# dashboard containing a input box for text, and 3 questions
st.title("Government Alternative Selections")

lugar = st.text_input("Lugar")
# list of topics
topics = ["Economía", "Salud", "Educación", "Seguridad", "Medio Ambiente"]
# input of select a topic
topic = st.selectbox("Tema", topics)
presupuesto = st.text_input("Presupuesto máximo", "$")
# list of complexity
complexity = ["Baja", "Media", "Alta"]
# input of select a complexity
complejidad = st.selectbox("Complejidad", complexity)
# input number
temporalidad = st.number_input("Temporalidad en meses", min_value=0, max_value=100, value=6)
impacto = st.text_input("Mínimo de personas a impactar")

# validade that all fields have an input
if lugar and topic and presupuesto and complejidad and temporalidad and impacto:
    if st.button("Validar"):
        st.write("Sí es viable 🤩")