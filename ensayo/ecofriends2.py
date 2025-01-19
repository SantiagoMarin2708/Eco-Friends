import os
from PIL import Image
import streamlit as st
import random

# Ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Cargar imagen principal
image_path = os.path.join(BASE_DIR, "Eco Friends.jpeg")
imagen = Image.open(image_path)
st.image(imagen)

# Configuración de la aplicación
st.title("🌍 Eco Friends 🗑️")
st.write("¡Ayuda a proteger el planeta clasificando los residuos correctamente!")

# Datos de basura y sus tipos
TRASH_ITEMS = [
    {"name": "Manzana", "type": "Orgánico", "image": os.path.join(BASE_DIR, "fotos", "manzana.jpg")},
    {"name": "Banano", "type": "Orgánico", "image": os.path.join(BASE_DIR, "fotos", "banano.jpg")},
    {"name": "Bolsa de plastico", "type": "No reciclable", "image": os.path.join(BASE_DIR, "fotos", "bolsa.jpg")},
    {"name": "Bombillo", "type": "No reciclable", "image": os.path.join(BASE_DIR, "fotos", "bombillo.jpg")},
    {"name": "Carton", "type": "Reciclable", "image": os.path.join(BASE_DIR, "fotos", "carton.jpg")},
    {"name": "Colores", "type": "No reciclable", "image": os.path.join(BASE_DIR, "fotos", "colores.jpg")},
    {"name": "Globos", "type": "No reciclable", "image": os.path.join(BASE_DIR, "fotos", "globos.webp")},
    {"name": "Pez", "type": "Orgánico", "image": os.path.join(BASE_DIR, "fotos", "pez.png")},
    {"name": "Pila", "type": "Reciclable", "image": os.path.join(BASE_DIR, "fotos", "pila.jpg")},
    {"name": "Tapa", "type": "Reciclable", "image": os.path.join(BASE_DIR, "fotos", "tapa.jpg")},
    {"name": "Tapabocas", "type": "No reciclable", "image": os.path.join(BASE_DIR, "fotos", "tapabocas.jpg")},
    {"name": "Vidrio", "type": "Reciclable", "image": os.path.join(BASE_DIR, "fotos", "vidrio.jpg")},
    {"name": "Botella de plástico", "type": "Reciclable", "image": os.path.join(BASE_DIR, "fotos", "botella.webp")},
    {"name": "Papel", "type": "Reciclable", "image": os.path.join(BASE_DIR, "fotos", "papel.jpg")},
    {"name": "Envoltura", "type": "No reciclable", "image": os.path.join(BASE_DIR, "fotos", "envoltura.jpg")},
    {"name": "Cáscara de huevo", "type": "Orgánico", "image": os.path.join(BASE_DIR, "fotos", "cascara.webp")}
]

# Contenedores
BIN_TYPES = ["Orgánico", "Reciclable", "No reciclable"]

# Estado inicial
if "score" not in st.session_state:
    st.session_state.score = 0
if "current_item" not in st.session_state:
    st.session_state.current_item = random.choice(TRASH_ITEMS)
if "message" not in st.session_state:
    st.session_state.message = None

# Define callback functions for buttons
def check_answer(selected_bin):
    if selected_bin == st.session_state.current_item["type"]:
        st.session_state.message = "✅ ¡Correcto! Buen trabajo."
        st.session_state.score += 1
    else:
        st.session_state.message = f"❌ Incorrecto. Este objeto es {st.session_state.current_item['type']}."
    # Elegir otro objeto
    st.session_state.current_item = random.choice(TRASH_ITEMS)

# Mostrar imagen del objeto actual
st.image(st.session_state.current_item["image"], caption=f"¿Dónde clasificarías este objeto?", width=200)

# Botones
boton1, boton2, boton3 = st.columns(3)
with boton1:
    if st.button("Orgánico", on_click=check_answer, args=("Orgánico",)):
        pass
with boton2:
    if st.button("Reciclable", on_click=check_answer, args=("Reciclable",)):
        pass
with boton3:
    if st.button("No reciclable", on_click=check_answer, args=("No reciclable",)):
        pass

# Mostrar mensaje si existe
if st.session_state.message:
    st.write(st.session_state.message)

# Mostrar puntuación
st.write(f"### Puntuación: {st.session_state.score}")
