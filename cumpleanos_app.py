import streamlit as st    
import base64
from PIL import Image, ImageDraw
import io
import time
import random
import streamlit.components.v1 as components
import mimetypes
import os


    
def get_base64_image(image_path):
    """Convierte imagen local a base64 para usar en HTML"""
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            # Detectar tipo MIME automáticamente
            mime_type, _ = mimetypes.guess_type(image_path)
            if mime_type is None:
                mime_type = "image/jpeg"  # Default
            
            encoded = base64.b64encode(img_file.read()).decode()
            return f"data:{mime_type};base64,{encoded}"
    else:
        st.error(f"No se encontró la imagen: {image_path}")
        return ""

# Configuración de la página
st.set_page_config(
    page_title="💖 Feliz Cumpleaños Mi Amor 💖",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS personalizado con imagen de fondo y estilos elegantes
# Agregar debug temporal
fondo_imagen = get_base64_image("images/11.jpeg")

# CSS solo para el fondo
st.markdown(f"""
<style>
    .stApp {{
        background: url('{fondo_imagen}') center/80%   no-repeat fixed;
        background-blend-mode: overlay;
        background-color: rgba(255, 182, 193, 0.3);
    }}
</style>
""", unsafe_allow_html=True)



st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;600;700&family=Poppins:wght@300;400;600&display=swap');
    .main-overlay {
        background: rgba(0, 0, 0, 0.4);
        backdrop-filter: blur(10px);
        min-height: 100vh;
        padding: 2rem 0;
    }
    
    .login-container {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border-radius: 30px;
        padding: 4rem 3rem;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.2);
        max-width: 500px;
        margin: 0 auto;
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .login-container::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%
        ;
        background: linear-gradient(45deg, transparent, rgba(255, 182, 193, 0.1), transparent);
        animation: shimmer 3s infinite;
    }
    
    @keyframes shimmer {
        0%% { transform: translateX(-100%%) translateY(-100%%) rotate(45deg); }
        100%% { transform: translateX(100%%) translateY(100%%) rotate(45deg); }
    }
    
    .heart-3d {
        position: relative;
        width: 200px;
        height: 200px;
        margin: 2rem auto;
        border-radius: 50%;
        overflow: hidden;
        box-shadow: 0 15px 40px rgba(255, 107, 138, 0.4);
        animation: heartbeat3d 2s ease-in-out infinite;
        background: linear-gradient(45deg, #ff6b8a, #c44569);
        padding: 5px;
    }
    
    .heart-3d::before,
    .heart-3d::after {
        display: none;
    }
    
    @keyframes heartbeat3d {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.1); }
    }
    
    @keyframes heartbeat3d {
        0%, 100% { transform: rotate(-45deg) scale(1); }
        25% { transform: rotate(-45deg) scale(1.1); }
        50% { transform: rotate(-45deg) scale(1.05); }
        75% { transform: rotate(-45deg) scale(1.15); }
    }
    
    .title-elegant {
        font-family: 'Dancing Script', cursive;
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(45deg, #ff6b8a, #c44569, #8e44ad);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .subtitle-elegant {
        font-family: 'Poppins', sans-serif;
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 2rem;
    }
    
    .input-elegant {
        background: rgba(255, 255, 255, 0.9);
        border: 2px solid rgba(255, 107, 138, 0.3);
        border-radius: 25px;
        padding: 15px 25px;
        font-size: 1.1rem;
        text-align: center;
        width: 100%;
        box-shadow: inset 0 4px 15px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    
    .input-elegant:focus {
        border-color: #ff6b8a;
        box-shadow: 0 0 20px rgba(255, 107, 138, 0.3);
        outline: none;
    }
    
    .btn-elegant {
        background: rgba(255, 182, 193, 0.3);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 15px 40px;
        font-size: 1.2rem;
        font-weight: 600;
        cursor: pointer;
        box-shadow: 0 8px 25px rgba(255, 107, 138, 0.3);
        transition: all 0.3s ease;
        margin-top: 1.5rem;
    }
    
    .btn-elegant:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(255, 107, 138, 0.4);
    }
    
    .content-section {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border-radius: 25px;
        padding: 3rem;
        margin: 3rem auto;
        max-width: 1000px;
        box-shadow: 0 15px 50px rgba(0, 0, 0, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    
    .section-title {
        font-family: 'Dancing Script', cursive;
        font-size: 2.8rem;
        font-weight: 600;
        background: linear-gradient(45deg, #ff6b8a, #c44569);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .love-message-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2.5rem;
        border-radius: 20px;
        margin: 2rem 0;
        text-align: center;
        box-shadow: 0 15px 40px rgba(0,0,0,0.2);
        position: relative;
        overflow: hidden;
    }
    
    .love-message-box::before {
        content: '💖';
        position: absolute;
        top: -10px;
        right: -10px;
        font-size: 4rem;
        opacity: 0.1;
    }
    
    .photo-grid {
        display: flex;
        overflow: hidden;
        margin: 2rem 0;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        width: 100%
    }

    .photo-scroll {
        display: flex;
        animation: scroll-photos 30s linear infinite;
        gap: 2rem;
    }

    @keyframes scroll-photos {
        0% { transform: translateX(0); }
        100% { transform: translateX(-100%); }
    }

    .photo-scroll:hover {
        animation-play-state: paused;
    }    
    
    .photo-card {
        background: white;
        border-radius: 15px;
        padding: 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
        overflow: hidden;
        min-width: 400px;
        height: 500px;
        flex: 1;
    }
    
    .photo-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    }
    
    .photo-card img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        border-radius: 15px;
    }
    
    .scratch-area {
        background: linear-gradient(45deg, #silver, #c0c0c0);
        border-radius: 15px;
        padding: 4rem 2rem;
        text-align: center;
        margin: 2rem 0;
        cursor: pointer;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .scratch-area:hover {
        background: linear-gradient(45deg, #b0b0b0, #a0a0a0);
    }
    
    .qr-revealed {
        background: white;
        border: 3px solid #ff6b8a;
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 15px 40px rgba(255, 107, 138, 0.2);
    }
    
    .floating-elements {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 1000;
        overflow: hidden;
    }
    
    .floating-heart {
        position: absolute;
        font-size: 25px;
        animation: float-up 8s linear infinite;
        opacity: 0.7;
    }
    
    @keyframes float-up {
        0% {
            transform: translateY(100vh) rotate(0deg);
            opacity: 0;
        }
        10% {
            opacity: 0.7;
        }
        90% {
            opacity: 0.7;
        }
        100% {
            transform: translateY(-100px) rotate(360deg);
            opacity: 0;
        }
    }
    
    .music-player {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        text-align: center;
    }
    
    .song-item {
        background: rgba(255, 255, 255, 0.1);
        margin: 1rem 0;
        padding: 1rem;
        border-radius: 10px;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .song-item:hover {
        background: rgba(255, 255, 255, 0.2);
        transform: scale(1.02);
    }
    .stButton > button[kind="primary"] {
        background: linear-gradient(45deg, #ff6b8a, #c44569) !important;
        border: none !important;
        color: white !important;
        border-radius: 25px !important;
        padding: 0.5rem 2rem !important;
        font-weight: 600 !important;
        box-shadow: 0 4px 15px rgba(255, 107, 138, 0.3) !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button[kind="primary"]:hover {
        background: linear-gradient(45deg, #ff4569, #a03454) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(255, 107, 138, 0.4) !important;
    }
    
    .stButton > button[kind="primary"]:active {
        transform: translateY(0px) !important;
    }
</style>
""", unsafe_allow_html=True)

# Función para generar elementos flotantes
def generate_floating_elements():
    elements_html = "<div class='floating-elements'>"
    emojis = ['💖', '💕', '🌹', '✨', '💝', '🎂', '🎉']
    for i in range(8):
        emoji = random.choice(emojis)
        left_pos = random.randint(0, 100)
        delay = random.uniform(0, 8)
        elements_html += f"""
        <div class='floating-heart' style='left: {left_pos}%; animation-delay: {delay}s;'>{emoji}</div>
        """
    elements_html += "</div>"
    return elements_html

# Inicializar estado de sesión
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'scratch_revealed' not in st.session_state:
    st.session_state.scratch_revealed = False

# Función de autenticación elegante
def elegant_login():

    
    # Contenedor principal centrado
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        mi_foto_b64 = get_base64_image("images/4.jpeg")
        
        # Agregar estado para el modal
        if 'show_modal' not in st.session_state:
            st.session_state.show_modal = False
        
        st.markdown(f"""
        <div class='login-container'>
            <div class='heart-3d' style='cursor: pointer;'>
                <img src='{mi_foto_b64}' style='width: 100%; height: 100%; object-fit: cover; border-radius: 50%;'>
            </div>
            <h1 class='title-elegant'>Feliz Cumpleaños</h1>
            <p class='subtitle-elegant'>Mi Amor Eterno ✨</p>
            <p style='color: #888; margin-bottom: 2rem; font-style: italic;'>
                "Cada día contigo es una celebración,<br>
                pero hoy es especialmente mágico"
            </p>
            <p style='color: #c44569; font-weight: 600; margin-top: 1rem;'>
                💕 Haz clic en el botón para continuar 💕
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Botón para abrir modal (encima de la imagen)
        if st.button("🔐 Ingresar la Fecha de tu cumple mi Pua", type="primary", use_container_width=True):
            st.session_state.show_modal = True
            st.rerun()
        
        # Modal flotante
        if st.session_state.show_modal:
            st.markdown("""
            <div style='
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                background: white;
                padding: 3rem;
                border-radius: 25px;
                box-shadow: 0 25px 80px rgba(0, 0, 0, 0.4);
                border: 3px solid #ff6b8a;
                z-index: 9999;
                text-align: center;
                max-width: 300px;
            '>
                <h2 style='color: #c44569; margin-bottom: 1rem; font-size: 24px;''>🔐 Te quiero mucho mi amor</h2>
                
            </div>
            """, unsafe_allow_html=True)
            
            # Input del código
            code = st.text_input("", placeholder="12345", type="password", key="modal_code")
            
            # Botones
            col_btn1, col_btn2 = st.columns(2)
            with col_btn1:
                if st.button("✨ Entrar ✨", type="primary"):
                    if code == "12345":
                        st.session_state.authenticated = True
                        st.session_state.show_modal = False
                        st.balloons()
                        st.success("¡Código correcto! 💖")
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.error("💔 Intenta de nuevo")
            
            with col_btn2:
                if st.button("❌ Cerrar"):
                    st.session_state.show_modal = False
                    st.rerun()

# Página principal con todas las secciones
def main_birthday_page():


    imagen_11 = get_base64_image("images/12.jpeg")
    # Título principal
    st.markdown(f"""
        <h1 style='
            font-family: Dancing Script, cursive;
            font-size: 2.8rem;
            font-weight: 600;
            -webkit-background-clip: text;
            text-align: center;
            margin-bottom: 2rem;
            color: #ffffff;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
        '>🎂 Tu Día Especial Ha Llegado 🎂</h1>
        <p style='text-align: center; font-size: 1.3rem; color: #666; margin-bottom: 3rem;'>
            Son 22 hermosos años✨
        </p>
         <img src='{imagen_11}' style='
        width: 60%; 
        height: 400px; 
        object-fit: cover; 
        border-radius: 15px;
        display: block;
        margin: 2rem auto;
    '>
    """, unsafe_allow_html=True)
    
    # Sección 1: Mensaje de Amor
    with open("gif.gif", "rb") as f:
        gif_base64 = base64.b64encode(f.read()).decode()

    st.markdown(f"""
        <h2 style='text-align: center; color: #c44569; font-family: Georgia, serif; margin-bottom: 20px;'>
            Con todo mi corazon 💖
        </h2>
        <div style="text-align: center; margin: 20px 0;">
            <img src="data:image/gif;base64,{gif_base64}" 
                 width="300" 
                 style="border-radius: 12px; box-shadow: 0 4px 12px rgba(255, 107, 157, 0.3);">
        </div>
        """, unsafe_allow_html=True)

    
    # Sección 2: Galería de Recuerdos (con imágenes predeterminadas)
    st.markdown("""
        <h2 class='section-title'> Porque siempre seras la mas hermosa</h2>
    """, unsafe_allow_html=True)
    
    # Lista de fotos (cambia por tus nombres reales)
    mis_fotos = ["images/1.jpeg", "images/2.jpeg", "images/5.jpeg", "images/6.jpeg", "images/7.jpeg", "images/8.jpeg", "images/9.jpeg", "images/10.jpeg", ]
    
    # Crear carrusel dinámicamente
    html_fotos = "<div class='photo-grid'><div class='photo-scroll'>"
    
    for foto in mis_fotos:
        if os.path.exists(foto):
            imagen_b64 = get_base64_image(foto)
            html_fotos += f"<div class='photo-card'><img src='{imagen_b64}' style='height: 400px; border-radius: 15px; padding: 0;'></div>"
    
    # Duplicar para loop infinito
    for foto in mis_fotos:
        if os.path.exists(foto):
            imagen_b64 = get_base64_image(foto)
            html_fotos += f"<div class='photo-card'><img src='{imagen_b64}' style='height: 400px; border-radius: 15px; padding: 0;'></div>"
    
    html_fotos += "</div></div>"
    
    # Mostrar el HTML
    st.markdown(html_fotos, unsafe_allow_html=True)
    # Sección 3: Rasca y Gana
    st.markdown("""
        <h2 class='section-title'>🎁 Esta cancion siempre me recuerda a nosotros 🎁</h2>
    """, unsafe_allow_html=True)
    
    if not st.session_state.scratch_revealed:
        st.markdown("""
        <div style='text-align: center; margin: 2rem 0;'>
            <div class='scratch-area' style='
                background: linear-gradient(45deg, #ffb3d1, #ff6b9d);
                border-radius: 15px;
                padding: 4rem 2rem;
                cursor: pointer;
                transition: all 0.3s ease;
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            '>
                <h3 style='color: #666; margin-bottom: 1rem;'>Te quiero mucho mi amor</h3>
                <div style='font-size: 4rem; margin: 1rem 0;'>🎁</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🎵 Presiona 🎵", type="primary", use_container_width=True):
                st.session_state.scratch_revealed = True
                st.balloons()
                st.rerun()
    
    if st.session_state.scratch_revealed:
        st.markdown("""
        <div style='text-align: center; margin: 2rem 0;'>
            <div style='
                background: white;
                border: 3px solid #ff6b8a;
                border-radius: 15px;
                padding: 2rem;
                box-shadow: 0 15px 40px rgba(255, 107, 138, 0.2);
            '>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # VIDEO DE YOUTUBE EMBEBIDO
        st.video("https://www.youtube.com/watch?v=KECUActT8mY&list=RDKECUActT8mY&start_radio=1")
        
        st.markdown("""
        <div style='text-align: center; margin: 2rem 0;'>
            <p style='color: #888; font-style: italic; font-size: 1.2rem;'>
                "Esta canción siempre me recuerda a nosotros..." 💖
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🔄 Ocultar video", use_container_width=True):
                st.session_state.scratch_revealed = False
                st.rerun()
        
        # Animación CSS
        st.markdown("""
        <style>
        @keyframes fadeIn {
            from { opacity: 0; transform: scale(0.8); }
            to { opacity: 1; transform: scale(1); }
        }
        </style>
        """, unsafe_allow_html=True)
        
    
    # Botón final de celebració
    
    
    if st.button("🎆 ¡FELIZ CUMPLEAÑOS! 🎆", type="primary"):
        st.balloons()
        st.snow()
        st.success("¡Que todos tus sueños se hagan realidad! 💖✨🎂")
    
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
# Ejecutar la aplicación
if __name__ == "__main__":
    if not st.session_state.authenticated:
        elegant_login()
    else:
        main_birthday_page()
        





































































