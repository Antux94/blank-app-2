import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

import subprocess

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
print("Versión de Maven:", version_maven)

# Comando para obtener la versión de Java
comando_java = ['java', '-version']
version_java = ejecutar_comando(comando_java)
print("Versión de Java:", version_java)
