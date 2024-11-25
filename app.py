import streamlit as st
import subprocess
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
import os

# Configuracion modo amplio
st.set_page_config(layout="wide")


@st.cache_data
def ejecutar_comando(comando):
    try:
        resultado = subprocess.check_output(comando, stderr=subprocess.STDOUT).decode("utf-8")
        return resultado
    except subprocess.CalledProcessError as e:
        return f"Error al ejecutar {' '.join(comando)}: {e.output.decode('utf-8')}"
    except FileNotFoundError:
        return f"El comando {' '.join(comando)} no se encuentra en el PATH."


# Comando para obtener la versión de Maven
comando_maven = ['mvn', '-version']
version_maven = ejecutar_comando(comando_maven)
# print("Versión de Maven:", version_maven)

# Comando para obtener la versión de Java
comando_java = ['java', '-version']
version_java = ejecutar_comando(comando_java)
# print("Versión de Java:", version_java)


# CSS para ocultar el header
hide_streamlit_style = """
            <style>
            /* Ocultar el header */
            #header {visibility: hidden;}
            /* Ocultar el menú de hamburguesa */
            .css-18e3th9 {visibility: hidden;}
            /* Opcional: Ocultar el footer de Streamlit */
            #.css-1s44ra {visibility: hidden;}
            .ezrtsby1 {visibility: hidden;}
            .en6cib62 {visibility: hidden;}
            .ea3mdgi2 {visibility: hidden;}
            .ea3mdgi6 {visibility: hidden;}
            .st-emotion-cache-1p2n2i4 {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# --------------------------------------------------------------------------------------------------------------MENU
with st.sidebar:
    selected = option_menu(
        menu_title="Menú",
        options=["Inicio", "Métricas", "Aso bot", "Historial"],
        icons=["house", "activity", "chat", "clock"],
        default_index=0,
        styles={
            "nav-link-selected":
                {
                    "background-color": "#0f5bd6",
                    "font-size": "16px",
                    "font-weight": "normal"
                },

            "nav-link": {"font-size": "16px"},
        }
    )

# --------------------------------------------------------------------------------------------------------------SIDEBAR MODELS


# Añadir una selectbox al sidebar
cliente = st.sidebar.selectbox(
    'Cliente',
    ('OpenAI', 'VertexAI'))

# Añadir una selectbox al sidebar
modelo = st.sidebar.selectbox(
    'Modelo',
    ('gpt-3.5-turbo-instruct', 'gpt-3.5-turbo', 'gpt-4'))

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

    # Usar HTML para cambiar el tamaño de la letra
    st.markdown(f"<p style='font-size:12px'>{str(version_maven)}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:12px'>{str(version_java)}</p>", unsafe_allow_html=True)

# --------------------------------------------------------------------------------------------------------------Inicio
particles_js = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Particles.js</title>
  <style>
  #particles-js {
    position: fixed;
    width: 100vw;
    height: 100vh;
    top: 0;
    left: 0;
    z-index: -1; /* Send the animation to the back */
  }
  .content {
    position: relative;
    z-index: 1;
    color: white;
  }

</style>
</head>
<body>
  <div id="particles-js"></div>
  <div class="content">
    <!-- Placeholder for Streamlit content -->
  </div>
  <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
  <script>
    particlesJS("particles-js", {
      "particles": {
        "number": {
          "value": 600,
          "density": {
            "enable": true,
            "value_area": 500
          }
        },
        "color": {
          "value": "#ffffff"
        },
        "shape": {
          "type": "square",
          "stroke": {
            "width": 0,
            "color": "#000000"
          },
          "polygon": {
            "nb_sides": 5
          },
          "image": {
            "src": "img/github.svg",
            "width": 100,
            "height": 100
          }
        },
        "opacity": {
          "value": 0.5,
          "random": false,
          "anim": {
            "enable": false,
            "speed": 1,
            "opacity_min": 0.2,
            "sync": false
          }
        },
        "size": {
          "value": 2,
          "random": true,
          "anim": {
            "enable": false,
            "speed": 40,
            "size_min": 0.1,
            "sync": false
          }
        },
        "line_linked": {
          "enable": true,
          "distance": 100,
          "color": "#ffffff",
          "opacity": 0.22,
          "width": 1
        },
        "move": {
          "enable": true,
          "speed": 0.9,
          "direction": "none",
          "random": false,
          "straight": false,
          "out_mode": "out",
          "bounce": true,
          "attract": {
            "enable": false,
            "rotateX": 600,
            "rotateY": 1200
          }
        }
      },
      "interactivity": {
        "detect_on": "canvas",
        "events": {
          "onhover": {
            "enable": true,
            "mode": "grab"
          },
          "onclick": {
            "enable": true,
            "mode": "repulse"
          },
          "resize": true
        },
        "modes": {
          "grab": {
            "distance": 100,
            "line_linked": {
              "opacity": 1
            }
          },
          "bubble": {
            "distance": 400,
            "size": 2,
            "duration": 2,
            "opacity": 0.5,
            "speed": 1
          },
          "repulse": {
            "distance": 200,
            "duration": 0.4
          },
          "push": {
            "particles_nb": 2
          },
          "remove": {
            "particles_nb": 3
          }
        }
      },
      "retina_detect": true
    });
  </script>
</body>
</html>
"""

if selected == "Inicio":

    # Cargar el contenido del archivo SVG
    svg_path = "/app/assets/logobbva.svg"

    with open(svg_path, "r") as file:
        svg_example = file.read()

    # HTML para el banner con SVG incluido
    banner_html = f"<div style='background-color: transparent; padding: 0px; border-radius: 10px; text-align: center'>{svg_example}</div>"

    st.markdown(banner_html, unsafe_allow_html=True)

    # Crea un cargador de archivos
    st.file_uploader("Carga el RAML", type=['zip'])

    if "show_animation" not in st.session_state:
        st.session_state.show_animation = True

    if st.session_state.show_animation:
        components.html(particles_js, height=370, scrolling=True)




    # Obtener la ubicación actual
    ubicacion_actual = os.getcwd()

    # Imprimir la ubicación actual
    print("Directorio actual:" + str(ubicacion_actual))

    st.text("Directorio actual:" + str(ubicacion_actual))




    # Cambiar de carpeta a 'app/riskadmissionscalculateincomesv0'
    os.chdir('/app/riskadmissionscalculateincomesv0')

    # Verificar la ubicación actual
    print("Directorio actual:" + str(ubicacion_actual))

    ubicacion_actual = os.getcwd()

    st.text("Directorio actual:" + str(ubicacion_actual))




    def ejecutar_comando_maven(comando):
        try:
            resultado = subprocess.check_output(comando, stderr=subprocess.STDOUT).decode("utf-8")
            return resultado
        except subprocess.CalledProcessError as e:
            return f"Error al ejecutar {' '.join(comando)}: {e.output.decode('utf-8')}"
        except FileNotFoundError:
            return f"El comando {' '.join(comando)} no se encuentra en el PATH."


    # Crear un botón en Streamlit para ejecutar el comando
    if st.button('Ejecutar mvn clean install'):
        comando_maven = ['mvn', 'clean', 'install']
        salida1 = ejecutar_comando_maven(comando_maven)

        # Mostrar la salida línea por línea en Streamlit
        for linea in salida1.splitlines():
            st.text(linea)










