import streamlit as st
import base64
from PIL import Image, ImageDraw
import io
import time
import random
import streamlit.components.v1 as components

# Configuración de la página
st.set_page_config(
    page_title="💖 Feliz Cumpleaños Mi Amor 💖",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS personalizado con imagen de fondo y estilos elegantes
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;600;700&family=Poppins:wght@300;400;600&display=swap');
    
    .stApp {
        background: url('https://images.unsplash.com/photo-1518709268805-4e9042af2176?ixlib=rb-4.0.3&auto=format&fit=crop&w=2070&q=80') center/cover no-repeat fixed;
        background-blend-mode: overlay;
        background-color: rgba(255, 182, 193, 0.3);
    }
    
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
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(255, 182, 193, 0.1), transparent);
        animation: shimmer 3s infinite;
    }
    
    @keyframes shimmer {
        0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
        100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
    }
    
    .heart-3d {
        position: relative;
        width: 120px;
        height: 120px;
        margin: 2rem auto;
        transform: rotate(-45deg);
        animation: heartbeat3d 2s ease-in-out infinite;
    }
    
    .heart-3d::before,
    .heart-3d::after {
        content: '';
        width: 60px;
        height: 96px;
        position: absolute;
        left: 60px;
        top: -48px;
        background: linear-gradient(135deg, #ff6b8a, #ff8fa3, #c44569);
        border-radius: 60px 60px 0 0;
        transform: rotate(-45deg);
        transform-origin: 0 100%;
        box-shadow: 0 8px 25px rgba(255, 107, 138, 0.4);
    }
    
    .heart-3d::after {
        left: -60px;
        transform: rotate(45deg);
        transform-origin: 100% 100%;
    }
    
    .heart-3d {
        background: linear-gradient(135deg, #ff6b8a, #ff8fa3, #c44569);
        border-radius: 30px 30px 0 30px;
        box-shadow: 0 8px 25px rgba(255, 107, 138, 0.4);
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
        background: linear-gradient(45deg, #ff6b8a, #c44569);
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
    }

    .photo-scroll {
        display: flex;
        animation: scroll-photos 20s linear infinite;
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
        padding: 1rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
        overflow: hidden;
    }
    
    .photo-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    }
    
    .photo-card img {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 10px;
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
    # Overlay principal
    #st.components.v1.html(generate_floating_elements(), height=0)
    
    # Elementos flotantes
    #st.markdown(generate_floating_elements(), unsafe_allow_html=True)
    
    # Contenedor principal centrado
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class='login-container'>
            <div class='heart-3d'></div>
            <h1 class='title-elegant'>Feliz Cumpleaños</h1>
            <p class='subtitle-elegant'>Mi Amor Eterno ✨</p>
            <p style='color: #888; margin-bottom: 2rem; font-style: italic;'>
                "Cada día contigo es una celebración,<br>
                pero hoy es especialmente mágico"
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Input personalizado con HTML
        st.markdown("""
        <div style='margin-top: -80px; position: relative; z-index: 10;'>
            <p style='text-align: center; color: #c44569; font-weight: 600; margin-bottom: 1rem;'>
                🔐 Código del Corazón 🔐
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        code = st.text_input("", placeholder="Ingresa nuestro número especial...", type="password", key="love_code")
        
        # Botón personalizado
        if st.button("💝 Abrir mi Corazón 💝", type="primary"):
            if code == "12345":
                st.session_state.authenticated = True
                st.balloons()
                st.success("¡Código correcto! 💖 ¡Bienvenida a tu día especial!")
                time.sleep(2)
                st.rerun()
            else:
                st.error("💔 Intenta de nuevo, mi amor...")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Página principal con todas las secciones
def main_birthday_page():
    # Overlay principal
    st.markdown("<div class='main-overlay'>", unsafe_allow_html=True)
    
    # Elementos flotantes
    #st.components.v1.html(generate_floating_elements(), height=0)

    
    # Título principal
    st.markdown("""
    <div class='content-section'>
        <h1 class='section-title'>🌟 Tu Día Especial Ha Llegado 🌟</h1>
        <p style='text-align: center; font-size: 1.3rem; color: #666; margin-bottom: 3rem;'>
            Un día lleno de amor, sorpresas y momentos mágicos solo para ti ✨
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sección 1: Mensaje de Amor
    st.markdown("""
    <div class='content-section'>
        <h2 class='section-title'>💖 Carta de Amor 💖</h2>
        <div class='love-message-box'>
            <h3 style='margin-bottom: 2rem; font-size: 2rem;'>Para la Mujer Más Especial</h3>
            <p style='font-size: 1.4rem; line-height: 1.8; margin: 2rem 0;'>
                En este día tan especial, quiero que sepas que eres la razón por la cual 
                cada amanecer es una promesa de felicidad. Tu sonrisa ilumina mis días más oscuros,
                tu risa es la melodía más hermosa que he escuchado, y tu amor es el regalo 
                más preciado que la vida me ha dado.
            </p>
            <p style='font-size: 1.3rem; line-height: 1.6; font-style: italic;'>
                Que este nuevo año de vida esté lleno de sueños cumplidos, aventuras increíbles,
                momentos de pura felicidad y todo el amor que tu corazón puede contener.
            </p>
            <h3 style='margin-top: 2.5rem; font-size: 1.8rem;'>
                ¡Te amo más allá de las palabras! 💕✨
            </h3>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Sección 2: Galería de Recuerdos (con imágenes predeterminadas)
    st.markdown("""
   <div class='content-section'>
       <h2 class='section-title'>📸 Nuestros Momentos Mágicos 📸</h2>
       <div class='photo-grid'>
           <div class='photo-scroll'>
               <div class='photo-card'>
                   <img src='https://images.unsplash.com/photo-1516589178581-6cd7833ae3b2?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80' alt='Momento especial'>
                   <h4 style='text-align: center; margin: 1rem 0 0.5rem 0; color: #c44569;'>💕 Primera Cita</h4>
                   <p style='text-align: center; color: #888; font-size: 0.9rem;'>El día que cambió todo</p>
               </div>
               <div class='photo-card'>
                   <img src='https://images.unsplash.com/photo-1522673607200-164d1b6ce486?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80' alt='Celebrando juntos'>
                   <h4 style='text-align: center; margin: 1rem 0 0.5rem 0; color: #c44569;'>🎉 Celebrando Juntos</h4>
                   <p style='text-align: center; color: #888; font-size: 0.9rem;'>Momentos de felicidad pura</p>
               </div>
               <div class='photo-card'>
                   <img src='https://images.unsplash.com/photo-1518709268805-4e9042af2176?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80' alt='Aventuras'>
                   <h4 style='text-align: center; margin: 1rem 0 0.5rem 0; color: #c44569;'>🌟 Nuestras Aventuras</h4>
                   <p style='text-align: center; color: #888; font-size: 0.9rem;'>Explorando el mundo juntos</p>
               </div>
               <div class='photo-card'>
                   <img src='https://images.unsplash.com/photo-1469371670807-013ccf25f16a?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80' alt='Momentos íntimos'>
                   <h4 style='text-align: center; margin: 1rem 0 0.5rem 0; color: #c44569;'>💖 Momentos Íntimos</h4>
                   <p style='text-align: center; color: #888; font-size: 0.9rem;'>Solo tú y yo</p>
               </div>
               <div class='photo-card'>
                   <img src='https://images.unsplash.com/photo-1511988617509-a57c8a288659?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80' alt='Cumpleaños anteriores'>
                   <h4 style='text-align: center; margin: 1rem 0 0.5rem 0; color: #c44569;'>🎂 Cumpleaños Anteriores</h4>
                   <p style='text-align: center; color: #888; font-size: 0.9rem;'>Cada año más especial</p>
               </div>
               <div class='photo-card'>
                   <img src='https://images.unsplash.com/photo-1524863479829-916d8e77f114?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80' alt='Planes futuros'>
                   <h4 style='text-align: center; margin: 1rem 0 0.5rem 0; color: #c44569;'>🌈 Nuestro Futuro</h4>
                   <p style='text-align: center; color: #888; font-size: 0.9rem;'>Infinitas posibilidades</p>
               </div>
               <div class='photo-card'>
                   <img src='https://images.unsplash.com/photo-1516589178581-6cd7833ae3b2?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80' alt='Momento especial'>
                   <h4 style='text-align: center; margin: 1rem 0 0.5rem 0; color: #c44569;'>💕 Primera Cita</h4>
                   <p style='text-align: center; color: #888; font-size: 0.9rem;'>El día que cambió todo</p>
               </div>
               <div class='photo-card'>
                   <img src='https://images.unsplash.com/photo-1522673607200-164d1b6ce486?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80' alt='Celebrando juntos'>
                   <h4 style='text-align: center; margin: 1rem 0 0.5rem 0; color: #c44569;'>🎉 Celebrando Juntos</h4>
                   <p style='text-align: center; color: #888; font-size: 0.9rem;'>Momentos de felicidad pura</p>
               </div>
           </div>
       </div>
   </div>
   """, unsafe_allow_html=True)
    
    # Sección 3: Rasca y Gana
    st.markdown("""
    <div class='content-section'>
        <h2 class='section-title'>🎁 Sorpresa Musical Especial 🎁</h2>
    """, unsafe_allow_html=True)
    
    if not st.session_state.scratch_revealed:
        st.markdown("""
        <div class='scratch-area' onclick='this.style.display="none"; document.getElementById("qr-section").style.display="block";'>
            <h3 style='color: #666; margin-bottom: 1rem;'>🔍 Rasca aquí para descubrir</h3>
            <p style='color: #888; font-size: 1.1rem;'>Tu canción especial te está esperando...</p>
            <div style='font-size: 3rem; margin: 1rem 0;'>🎵</div>
            <p style='color: #999; font-size: 0.9rem;'>Haz clic para rascar</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("✨ Rascar Sorpresa ✨", type="primary"):
            st.session_state.scratch_revealed = True
            st.balloons()
            st.rerun()
    
    if st.session_state.scratch_revealed:
        st.markdown("""
        <div class='qr-revealed'>
            <h3 style='color: #c44569; margin-bottom: 1rem;'>🎵 ¡Tu Canción del Corazón! 🎵</h3>
            <p style='color: #666; margin-bottom: 2rem;'>Escanea este código QR para escuchar nuestra melodía especial 💕</p>
            <div style='display: flex; justify-content: center; margin: 2rem 0;'>
                <div style='border: 3px solid #ff6b8a; padding: 2rem; border-radius: 15px; background: white;'>
                    <div style='font-size: 6rem; margin: 0;'>📱</div>
                    <p style='margin: 1rem 0 0 0; color: #666; font-weight: 600;'>Código QR Spotify</p>
                    <p style='margin: 0.5rem 0 0 0; color: #999; font-size: 0.8rem;'>
                        (Aquí va tu QR real)
                    </p>
                </div>
            </div>
            <p style='color: #888; font-style: italic;'>
                "Esta canción siempre me recuerda a nosotros..." 💖
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🔄 Ocultar y rascar de nuevo"):
            st.session_state.scratch_revealed = False
            st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Sección 4: Playlist Musical
    st.markdown("""
    <div class='content-section'>
        <h2 class='section-title'>🎵 Playlist de Nuestro Amor 🎵</h2>
        <div class='music-player'>
            <h3 style='margin-bottom: 2rem;'>💕 Canciones que cuentan nuestra historia</h3>
            <div class='song-item'>
                <h4>🌹 "Perfect" - Ed Sheeran</h4>
                <p style='font-style: italic; margin: 0.5rem 0 0 0;'>"Porque eres perfecta para mí"</p>
            </div>
            <div class='song-item'>
                <h4>💖 "All of Me" - John Legend</h4>
                <p style='font-style: italic; margin: 0.5rem 0 0 0;'>"Todo de mí ama todo de ti"</p>
            </div>
            <div class='song-item'>
                <h4>✨ "A Thousand Years" - Christina Perri</h4>
                <p style='font-style: italic; margin: 0.5rem 0 0 0;'>"Te amaré por mil años más"</p>
            </div>
            <div class='song-item'>
                <h4>🎶 "Thinking Out Loud" - Ed Sheeran</h4>
                <p style='font-style: italic; margin: 0.5rem 0 0 0;'>"Cuando tus piernas ya no funcionen como antes"</p>
            </div>
        </div>
        
        <div style='margin-top: 2rem; text-align: center;'>
            <h4 style='color: #c44569; margin-bottom: 1rem;'>💌 Dedica una canción especial:</h4>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Dedicatoria musical
    user_message = st.text_area(
        "Escribe tu dedicatoria musical:",
        placeholder="Esta canción me recuerda a ti porque...",
        height=100
    )
    
    if user_message:
        st.markdown(f"""
        <div class='content-section'>
            <div style='background: linear-gradient(135deg, #ff9a9e, #fecfef); 
                        padding: 2rem; border-radius: 15px; margin: 2rem 0;'>
                <p style='font-size: 1.2rem; font-style: italic; color: #333; line-height: 1.6;'>
                    "{user_message}"
                </p>
                <p style='text-align: right; color: #666; margin-top: 1rem; font-weight: 600;'>
                    - Con todo mi amor 💕
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Botón final de celebración
    st.markdown("""
    <div class='content-section' style='text-align: center;'>
        <h2 style='color: #c44569; margin-bottom: 2rem;'>🎉 ¡Celebremos Juntos! 🎉</h2>
    """, unsafe_allow_html=True)
    
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
        
        # Botón para cerrar sesión en la barra lateral
        with st.sidebar:
            st.markdown("### 🚪 Opciones")
            if st.button("Cerrar Sesión"):
                st.session_state.authenticated = False
                st.rerun()
