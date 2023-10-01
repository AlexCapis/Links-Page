import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

st.write("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://gitHub.com/dataprofessor/links)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))



import streamlit as st

# Centro el título y reduzco el espacio superior e interlineado
st.markdown("<h1 style='text-align: center; margin-bottom: 0; line-height: 0.5;'>Alex Marzá Manuel</h1>", unsafe_allow_html=True)

# Centro el subtítulo y reduzco el espacio inferior e interlineado
st.markdown("<h2 style='text-align: center; margin-top: 0; line-height: 0.5;'>Junior Data Scientist</h2>", unsafe_allow_html=True)


# Texto justificado
st.markdown("<p style='text-align: justify;'>Soy un apasionado de los datos con experiencia en el análisis y la visualización de datos. Mi enfoque creativo y mi capacidad para contar historias con datos me permiten convertir la información en insights valiosos para la toma de decisiones.</p>", unsafe_allow_html=True)


icon_size = 20


# Enlaces y mensajes
github_url = "https://github.com/AlexCapis"
linkedin_url = "https://www.linkedin.com/in/alex-marza-data-science/"
whatsapp_url = "http://wa.me/34695802887?text=%C2%A1Hola!%20He%20revisado%20su%20perfil%20y%20parece%20encajar%20con%20lo%20que%20estamos%20buscando.%20Por%20ello,%20desde%20nuestro%20departamento%20de%20RRHH%20nos%20gustar%C3%ADa%20concertar%20una%20entrevista%20con%20usted%20para%20profundizar%20en%20el%20puesto%20laboral%20y%20conocernos%20mejor.%20%C2%A1Espero%20su%20respuesta!"

# Tamaño del icono
icon_size = 64

# Crear los botones
st.write("Puedes contactarme a través de estos enlaces:")
st_button('github', github_url, ' Mis proyectos en GitHub', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/alex-marza-data-science/', ' Sigueme en LinkedIn', icon_size)
# st_button('linkedin', linkedin_url, 'LinkedIn', icon_size)
st_button('whatsapp', whatsapp_url, 'WhatsApp', icon_size)





