from pgzero.builtins import Rect  # Importa Rect para criar áreas clicáveis
from jogo.constantes import *  # Importa constantes globais

class Menu:
    def __init__(self):
        # Calcula o centro da tela para posicionar os botões
        center_x = WIDTH // 2
        start_y = HEIGHT // 2 - 50
        
        # Cria os retângulos dos botões (x, y, largura, altura)
        self.btn_start = Rect(0, 0, 300, 60)
        self.btn_start.center = (center_x, start_y)
        
        self.btn_sound = Rect(0, 0, 300, 60)
        self.btn_sound.center = (center_x, start_y + 100)
        
        self.btn_exit = Rect(0, 0, 300, 60)
        self.btn_exit.center = (center_x, start_y + 200)
        
        self.sound_enabled = True  # Estado inicial do som

    def draw(self, screen):
        """Desenha a interface do menu"""
        screen.clear()  # Limpa a tela
        
        # Título do Jogo
        screen.draw.text("AVENTURA DO COELHO", center=(WIDTH//2, 150), fontsize=100, color="white")
        
        # Botão Iniciar (Azul)
        screen.draw.filled_rect(self.btn_start, "blue")
        screen.draw.text("INICIAR", center=self.btn_start.center, fontsize=40, color="white")
        
        # Botão Som (Verde/Cinza)
        color_sound = "green" if self.sound_enabled else "gray"
        text_sound = "SOM: ON" if self.sound_enabled else "SOM: OFF"
        screen.draw.filled_rect(self.btn_sound, color_sound)
        screen.draw.text(text_sound, center=self.btn_sound.center, fontsize=40, color="white")
        
        # Botão Sair (Vermelho)
        screen.draw.filled_rect(self.btn_exit, "red")
        screen.draw.text("SAIR", center=self.btn_exit.center, fontsize=40, color="white")

    def handle_click(self, pos):
        """Verifica cliques nos botões e retorna a ação"""
        if self.btn_start.collidepoint(pos):
            return "start"
        elif self.btn_sound.collidepoint(pos):
            self.sound_enabled = not self.sound_enabled  # Alterna estado do som
            return "toggle_sound"
        elif self.btn_exit.collidepoint(pos):
            return "exit"
        return None  # Nenhum botão clicado
