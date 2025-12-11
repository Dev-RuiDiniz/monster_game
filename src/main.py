# src/main.py

import pygame
import sys
from config import SCREEN_WIDTH, SCREEN_HEIGHT, TITLE, FPS, WHITE, BLACK

class Game:
    """
    Classe principal para gerenciar o estado e o loop do jogo Pykémon.
    Seguindo o princípio de POO, o jogo é encapsulado em um objeto.
    """
    def __init__(self):
        """Inicializa o Pygame, a janela e o relógio."""
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

    def handle_events(self):
        """Gerencia todos os eventos do usuário (teclado, mouse, fechar janela)."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            # Adicione outras manipulações de eventos aqui (e.g., tecla pressionada)
            
    def update(self):
        """Atualiza a lógica do jogo (movimentação, colisões, etc.)."""
        # A lógica de atualização do estado do jogo virá aqui
        pass

    def draw(self):
        """Desenha todos os elementos na tela."""
        self.screen.fill(WHITE) # Preenche o fundo com branco
        # Outros elementos do jogo serão desenhados aqui
        
        # Atualiza a tela para exibir o que foi desenhado
        pygame.display.flip()
        
    def run(self):
        """O loop principal do jogo."""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS) # Garante que o jogo rode no FPS definido

        # Finaliza o Pygame
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    game = Game()
    game.run()