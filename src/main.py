# src/main.py

import pygame
import sys
# Importa todas as configurações
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, TITLE, FPS, BACKGROUND_COLOR

# Exemplo de importação futura de uma Scene
# from scenes.menu import MenuScene 

class Game:
    """
    A classe Game é o ponto de entrada principal e o gerenciador de estado.
    Ela segue o padrão Singleton (implicitamente, pois só criamos uma instância)
    e o padrão Game Loop.
    """
    def __init__(self):
        """Inicializa o Pygame e configura os objetos essenciais."""
        pygame.init()
        
        # Define a tela de exibição (Surface)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        
        # Objeto Clock para controle de tempo/FPS
        self.clock = pygame.time.Clock()
        
        self.running = True
        
        # Estado atual do jogo (futuramente, usaremos isso para gerenciar Scenes/Cenas)
        # self.current_scene = MenuScene(self) 

    def handle_events(self):
        """Gerencia todos os eventos de entrada (input)."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            
            # Repassa eventos para a cena ativa, se houver
            # if self.current_scene:
            #     self.current_scene.handle_input(event)


    def update(self):
        """Atualiza a lógica do jogo."""
        # if self.current_scene:
        #     self.current_scene.update()
        pass

    def draw(self):
        """
        Desenha todos os elementos na tela.
        
        Ordem de desenho: Fundo -> Mapa -> Sprites -> UI/HUD.
        """
        
        # 1. Limpar a tela (Fundo)
        # Usa a constante de cor de fundo definida em settings.py
        self.screen.fill(BACKGROUND_COLOR) 
        
        # 2. Desenho de Elementos (Futuro: mapa, personagens, etc.)
        # Exemplo de desenho de texto ou um retângulo para demonstrar
        font = pygame.font.Font(None, 36)
        text = font.render(f"Pykémon - FPS: {int(self.clock.get_fps())}", True, WHITE)
        self.screen.blit(text, (10, 10))

        # 3. Atualizar a tela (Flip)
        # O comando flip() exibe o buffer de desenho na tela, tornando o frame visível.
        pygame.display.flip()
        
    def run(self):
        """O loop principal (Game Loop) que coordena o jogo."""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS) 

        self.quit()

    def quit(self):
        """Encerra o Pygame e o sistema de forma limpa."""
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    game = Game()
    game.run()