# Bienvenido a la página de enlaces de Streamlit

![Streamlit Links Page](streamlit-links-page.png)

> Una aplicación de Streamlit que puedes crear de forma gratuita para almacenar todos tus enlaces personales, similar en funcionalidad a [Linktr.ee](https://linktr.ee/).

![App de demostración](23F54497-245E-413F-99C7-F3E295E4EA13.png)

# Demo de la aplicación

[![App de Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://chanin.streamlitapp.com/)

# Configuración

Configurar tu propia página de enlaces de Streamlit es realmente fácil, solo sigue los siguientes 3 pasos:

**Paso 1**. [Haz clic aquí](https://github.com/streamlit/links/generate) para generar una copia de este repositorio. A continuación, nombra tu nuevo repositorio como desees, excepto `tu nombre de usuario`.github.io.

**Paso 2**. Personaliza el contenido de la recién generada "página de enlaces" editando el archivo `streamlit_app.py`:

```python
import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('Chanin Nantasenamat, Ph.D.')

st.info('Developer Advocate, Content Creator y ex Profesor con interés en Data Science y Bioinformática')

icon_size = 20

st_button('youtube', 'https://youtube.com/dataprofessor', 'Canal de YouTube de Data Professor', icon_size)
st_button('youtube', 'https://youtube.com/codingprofessor', 'Canal de YouTube de Coding Professor', icon_size)
st_button('medium', 'https://data-professor.medium.com/', 'Lee mis blogs', icon_size)
st_button('twitter', 'https://twitter.com/thedataprof/', 'Sígueme en Twitter', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/chanin-nantasenamat/', 'Sígueme en LinkedIn', icon_size)
st_button('newsletter', 'https://sendfox.com/dataprofessor/', 'Regístrate en mi boletín', icon_size)
st_button('cup', 'https://www.buymeacoffee.com/dataprofessor/', 'Invítame un café', icon_size)
