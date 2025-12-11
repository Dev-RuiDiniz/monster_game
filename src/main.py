# src/main.py

import pygame
import sys
# Importa todas as configurações
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, TITLE, FPS, BACKGROUND_COLOR, WHITE

# Importa a primeira entidade para teste
from entities.pokemon import Pokemon 

class Game:
    """
    A classe Game encapsula a inicialização do Pygame, a janela, 
    o relógio e o loop principal do jogo (Game Loop).
    """
    def __init__(self):
        """Inicializa o Pygame e configura os objetos essenciais."""
        pygame.init()
        
        # Cria a janela de exibição
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
        # Define o título da janela
        pygame.display.set_caption(TITLE)
        
        # Cria o objeto Clock para controlar o FPS
        self.clock = pygame.time.Clock()
        
        self.running = True

        # --- Exemplo de inicialização de Entidades para teste ---
        # Definindo ataques
        tackle = {'name': 'Tackle', 'power': 15}
        
        # Criando Pokémons de teste
        base_stats_char = {'hp': 40, 'attack': 12, 'defense': 8}
        self.player_pokemon = Pokemon("Charizard", 5, base_stats_char, [tackle])
        print(f"Game iniciado com: {self.player_pokemon}")

    def handle_events(self):
        """
        Gerencia todos os eventos de entrada (input) do usuário.
        Inclui o tratamento do evento de fechar a janela e pressionar ESC.
        """
        for event in pygame.event.get():
            # 1. Tratamento do Fechamento de Janela (Botão 'X')
            if event.type == pygame.QUIT:
                self.running = False
            
            # 2. Tratamento de Teclado
            if event.type == pygame.KEYDOWN:
                # Tratamento do ESC (Escape Key)
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self):
        """Atualiza a lógica do jogo: movimento, colisões, IA, estados de cena."""
        # Esta é a etapa onde a lógica principal do jogo acontece
        pass

    def draw(self):
        """Desenha todos os elementos na tela na ordem correta (fundo, mapa, sprites, UI)."""
        
        # 1. Desenha o fundo (limpa o frame anterior)
        self.screen.fill(BACKGROUND_COLOR)
        
        # 2. Desenha os elementos do jogo (aqui virão o mapa e os sprites)
        
        # 3. Desenha a UI/HUD (barra de vida, texto)
        
        # Atualiza o display para que as mudanças sejam visíveis
        pygame.display.flip()
        
    def run(self):
        """O loop principal do jogo."""
        print("Iniciando Game Loop...")
        while self.running:
            # ...
            pass # Lógica do Game Loop
        
        # Chamada final que encerra o Pygame e o sistema
        self.quit()

        # Finalização limpa do Pygame
        self.quit()

    def quit(self):
        """Encerra o Pygame e o sistema de forma limpa."""
        print("Encerrando Pygame...")
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    # Este bloco garante que o código só será executado se o arquivo for o principal.
    game = Game()
    game.run()