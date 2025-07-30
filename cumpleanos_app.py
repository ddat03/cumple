import streamlit as st
import base64
from PIL import Image, ImageDraw
import io
import time
import random

# Configuración de la página
st.set_page_config(
    page_title="💖 Feliz Cumpleaños Mi Amor 💖",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS personalizado para estilos bonitos
st.markdown("""
<style>
    .main-container {
        background: linear-gradient(45deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);
        padding: 2rem;
        border-radius: 20px;
        margin: 1rem 0;
    }
    
    .heart-container {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        margin: 2rem 0;
    }
    
    .heart {
        position: relative;
        width: 300px;
        height: 300px;
        background: linear-gradient(45deg, #ff6b8a, #c44569);
        margin: 50px auto;
        transform: rotate(-45deg);
        border-radius: 50px 50px 0 50px;
        box-shadow: 0 0 30px rgba(255, 107, 138, 0.6);
        animation: heartbeat 1.5s ease-in-out infinite;
    }
    
    .heart:before,
    .heart:after {
        content: '';
        width: 150px;
        height: 240px;
        position: absolute;
        left: 75px;
        top: -120px;
        background: linear-gradient(45deg, #ff6b8a, #c44569);
        border-radius: 150px 150px 0 0;
        transform: rotate(-45deg);
        transform-origin: 0 100%;
    }
    
    .heart:after {
        left: -75px;
        transform: rotate(45deg);
        transform-origin: 100% 100%;
    }
    
    @keyframes heartbeat {
        0% { transform: rotate(-45deg) scale(1); }
        50% { transform: rotate(-45deg) scale(1.1); }
        100% { transform: rotate(-45deg) scale(1); }
    }
    
    .love-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        margin: 2rem 0;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    
    .photo-gallery {
        background: rgba(255, 255, 255, 0.9);
        padding: 2rem;
        border-radius: 20px;
        margin: 2rem 0;
    }
    
    .scratch-card {
        background: #f0f0f0;
        border: 3px solid #ddd;
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        margin: 2rem 0;
    }
    
    .floating-hearts {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 1000;
    }
    
    .floating-heart {
        position: absolute;
        color: #ff6b8a;
        font-size: 20px;
        animation: float 6s ease-in-out infinite;
    }
    
    @keyframes float {
        0% { transform: translateY(100vh) rotate(0deg); opacity: 1; }
        100% { transform: translateY(-100px) rotate(360deg); opacity: 0; }
    }
</style>
""", unsafe_allow_html=True)

# Función para generar corazones flotantes
def generate_floating_hearts():
    hearts_html = "<div class='floating-hearts'>"
    for i in range(5):
        left_pos = random.randint(0, 100)
        delay = random.uniform(0, 6)
        hearts_html += f"""
        <div class='floating-heart' style='left: {left_pos}%; animation-delay: {delay}s;'>💖</div>
        """
    hearts_html += "</div>"
    return hearts_html

# Inicializar estado de sesión
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'photos' not in st.session_state:
    st.session_state.photos = []
if 'scratch_revealed' not in st.session_state:
    st.session_state.scratch_revealed = False

# Función de autenticación
def authenticate():
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    
    # Título principal con emojis
    st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
        <h1 style='color: #ff6b8a; font-size: 3rem; margin-bottom: 1rem;'>
            💖 ¡Feliz Cumpleaños Mi Amor! 💖
        </h1>
        <h3 style='color: #c44569;'>🎂 Día especial para una persona especial 🎂</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Corazones flotantes
    st.markdown(generate_floating_hearts(), unsafe_allow_html=True)
    
    # Contenedor del corazón
    st.markdown("<div class='heart-container'>", unsafe_allow_html=True)
    st.markdown("<div class='heart'></div>", unsafe_allow_html=True)
    
    # Campo de entrada del código
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style='text-align: center; margin: 2rem 0;'>
            <h3 style='color: #c44569; margin-bottom: 1rem;'>
                🔐 Ingresa el código secreto del amor 🔐
            </h3>
        </div>
        """, unsafe_allow_html=True)
        
        code = st.text_input("", placeholder="Código de amor...", type="password", key="love_code")
        
        if st.button("💝 Abrir mi regalo 💝", type="primary"):
            if code == "12345":
                st.session_state.authenticated = True
                st.balloons()
                st.success("¡Código correcto! 💖 ¡Bienvenida a tu sorpresa de cumpleaños!")
                time.sleep(2)
                st.rerun()
            else:
                st.error("Código incorrecto 💔 ¡Inténtalo de nuevo!")
    
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Página principal después de autenticación
def main_page():
    # Título de bienvenida
    st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
        <h1 style='color: #ff6b8a; font-size: 3rem; margin-bottom: 1rem;'>
            🌟 ¡Sorpresa de Cumpleaños! 🌟
        </h1>
        <h3 style='color: #c44569;'>✨ Un día mágico para ti ✨</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Crear pestañas para las diferentes secciones
    tab1, tab2, tab3, tab4 = st.tabs(["💝 Mensaje de Amor", "📸 Galería de Recuerdos", "🎁 Rasca y Gana", "🎵 Sorpresa Musical"])
    
    with tab1:
        message_section()
    
    with tab2:
        photo_gallery_section()
    
    with tab3:
        scratch_card_section()
    
    with tab4:
        music_section()

# Sección de mensaje de amor
def message_section():
    st.markdown("""
    <div class='love-message'>
        <h2>💖 Mensaje Especial Para Ti 💖</h2>
        <p style='font-size: 1.3rem; line-height: 1.6; margin: 2rem 0;'>
            En este día tan especial, quiero que sepas que eres la luz de mis días,
            la melodía de mis noches y la razón de mi sonrisa cada mañana.
            Tu cumpleaños no es solo la celebración de un año más de vida,
            sino la celebración del amor más puro y hermoso que existe.
        </p>
        <p style='font-size: 1.2rem; font-style: italic;'>
            ¡Que este nuevo año esté lleno de aventuras juntos, risas infinitas,
            sueños cumplidos y todo el amor que mereces! 🌹
        </p>
        <h3 style='margin-top: 2rem;'>¡Te amo más de lo que las palabras pueden expresar! 💕</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Botón para efectos especiales
    if st.button("🎆 ¡Celebrar! 🎆"):
        st.balloons()
        st.snow()

# Sección de galería de fotos
def photo_gallery_section():
    st.markdown("<div class='photo-gallery'>", unsafe_allow_html=True)
    st.markdown("### 📸 Nuestros Momentos Especiales 📸")
    
    # Subir fotos
    uploaded_files = st.file_uploader(
        "Agrega nuestras fotos favoritas 💕", 
        accept_multiple_files=True, 
        type=['png', 'jpg', 'jpeg']
    )
    
    if uploaded_files:
        st.session_state.photos = uploaded_files
    
    # Mostrar galería
    if st.session_state.photos:
        cols = st.columns(3)
        for idx, photo in enumerate(st.session_state.photos):
            with cols[idx % 3]:
                st.image(photo, caption=f"Recuerdo {idx + 1} 💕", use_container_width=True)
                if st.button(f"❤️", key=f"like_{idx}"):
                    st.write("¡Me encanta este momento! 💖")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Sección de rasca y gana
def scratch_card_section():
    st.markdown("<div class='scratch-card'>", unsafe_allow_html=True)
    st.markdown("### 🎁 Rasca y Descubre tu Sorpresa 🎁")
    
    if not st.session_state.scratch_revealed:
        st.markdown("""
        <div style='background: silver; padding: 3rem; border-radius: 10px; margin: 2rem 0;'>
            <h3 style='color: #666; text-align: center;'>
                🔍 Haz clic en "Rascar" para descubrir tu sorpresa musical 🔍
            </h3>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("✨ Rascar ✨", type="primary"):
            st.session_state.scratch_revealed = True
            st.balloons()
            st.rerun()
    else:
        # Mostrar código QR (aquí puedes poner el código QR real de la canción de Spotify)
        st.markdown("""
        <div style='text-align: center; padding: 2rem;'>
            <h2>🎵 ¡Tu Canción Especial! 🎵</h2>
            <p>Escanea este código QR para escuchar nuestra canción ❤️</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Aquí deberías reemplazar con el QR real de tu canción de Spotify
        st.markdown("""
        <div style='display: flex; justify-content: center; margin: 2rem 0;'>
            <div style='border: 3px solid #ff6b8a; padding: 1rem; border-radius: 10px; background: white;'>
                <p style='font-size: 4rem; margin: 0;'>📱</p>
                <p style='margin: 0.5rem 0 0 0; color: #666;'>Código QR</p>
                <p style='margin: 0; color: #999; font-size: 0.8rem;'>
                    (Reemplaza con tu QR real)
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🔄 Rascar de nuevo"):
            st.session_state.scratch_revealed = False
            st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)

# Sección musical adicional
def music_section():
    st.markdown("### 🎵 Playlist de Cumpleaños 🎵")
    
    # Lista de canciones románticas
    songs = [
        "💕 Perfect - Ed Sheeran",
        "🌹 All of Me - John Legend", 
        "💖 Thinking Out Loud - Ed Sheeran",
        "✨ A Thousand Years - Christina Perri",
        "🎶 Make You Feel My Love - Adele"
    ]
    
    selected_song = st.selectbox("🎧 Elige una canción para dedicar:", songs)
    
    if st.button("🎼 Dedicar esta canción 🎼"):
        st.success(f"¡Has dedicado: {selected_song}! 💝")
        st.balloons()
    
    # Crear playlist personalizada
    st.markdown("#### 🎵 Crea tu mensaje musical:")
    user_message = st.text_area(
        "Escribe un mensaje con la canción:",
        placeholder="Esta canción me recuerda a ti porque..."
    )
    
    if user_message:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #ff9a9e, #fecfef); 
                    padding: 1rem; border-radius: 10px; margin: 1rem 0;'>
            <p style='font-style: italic; color: #333;'>"{user_message}"</p>
            <p style='text-align: right; color: #666;'>- Con amor 💕</p>
        </div>
        """, unsafe_allow_html=True)

# Ejecutar la aplicación
if __name__ == "__main__":
    if not st.session_state.authenticated:
        authenticate()
    else:
        main_page()
        
        # Botón para cerrar sesión
        if st.sidebar.button("🚪 Salir"):
            st.session_state.authenticated = False
            st.rerun()