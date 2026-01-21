from pgzero.builtins import Rect
from jogo.constantes import *

class Menu:
    def __init__(self):
        # Centraliza os botões
        center_x = WIDTH // 2
        start_y = HEIGHT // 2 - 50
        
        self.btn_start = Rect(0, 0, 300, 60) # Botões maiores
        self.btn_start.center = (center_x, start_y)
        
        self.btn_sound = Rect(0, 0, 300, 60)
        self.btn_sound.center = (center_x, start_y + 100)
        
        self.btn_exit = Rect(0, 0, 300, 60)
        self.btn_exit.center = (center_x, start_y + 200)
        
        self.sound_enabled = True

    def draw(self, screen):
        screen.clear()
        screen.draw.text("AVENTURA DO COELHO", center=(WIDTH//2, 150), fontsize=100, color="white")
        
        # Botões
        screen.draw.filled_rect(self.btn_start, "blue")
        screen.draw.text("INICIAR", center=self.btn_start.center, fontsize=40, color="white")
        
        color_sound = "green" if self.sound_enabled else "gray"
        text_sound = "SOM: ON" if self.sound_enabled else "SOM: OFF"
        screen.draw.filled_rect(self.btn_sound, color_sound)
        screen.draw.text(text_sound, center=self.btn_sound.center, fontsize=40, color="white")
        
        screen.draw.filled_rect(self.btn_exit, "red")
        screen.draw.text("SAIR", center=self.btn_exit.center, fontsize=40, color="white")

    def handle_click(self, pos):
        if self.btn_start.collidepoint(pos):
            return "start"
        elif self.btn_sound.collidepoint(pos):
            self.sound_enabled = not self.sound_enabled
            return "toggle_sound"
        elif self.btn_exit.collidepoint(pos):
            return "exit"
        return None
