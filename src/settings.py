# src/settings.py
#
# Arquivo centralizado para todas as constantes e configurações globais do jogo.

# --- ⚙️ CONFIGURAÇÕES GERAIS DO JOGO ---
TITLE = "Pykémon - Aventura POO"
FPS = 60 # Quadros por segundo (Frame Rate)

# --- 🖼️ CONFIGURAÇÕES DA TELA ---
# Dimensões da tela em pixels
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# --- 📏 CONFIGURAÇÕES DO MAPA E TILES ---
# TILE_SIZE é crucial para o motor de mapa, define o tamanho de cada bloco/quadrado.
# O valor padrão mais comum para jogos retro é 16 ou 32.
TILE_SIZE = 32

# Calcula as dimensões do mapa em número de tiles, não em pixels.
# Isso será útil para loops de desenho de mapa.
MAP_WIDTH = SCREEN_WIDTH // TILE_SIZE
MAP_HEIGHT = SCREEN_HEIGHT // TILE_SIZE

# --- 🎨 PALETA DE CORES (RGB) ---
# Centralizar cores evita que o desenvolvedor tenha que lembrar dos códigos RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BACKGROUND_COLOR = (135, 206, 250) # Azul céu claro