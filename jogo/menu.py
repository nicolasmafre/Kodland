from pgzero.builtins import Rect  # Importa Rect para criar botões

class Menu:
    def __init__(self):
        """Inicializa os botões do menu e o estado do som"""
        # Define a posição e tamanho dos botões (x, y, largura, altura)
        self.btn_start = Rect(300, 200, 200, 50)
        self.btn_sound = Rect(300, 300, 200, 50)
        self.btn_exit = Rect(300, 400, 200, 50)
        self.sound_enabled = True  # Estado inicial do som (Ligado)

    def draw(self, screen):
        """Desenha o menu na tela"""
        # Título do Menu
        screen.draw.text("MENU PRINCIPAL", center=(400, 100), fontsize=50, color="white")
        
        # Botão Iniciar (Azul)
        screen.draw.filled_rect(self.btn_start, "blue")
        screen.draw.text("INICIAR", center=self.btn_start.center, fontsize=30, color="white")
        
        # Botão Som (Verde se ligado, Cinza se desligado)
        color_sound = "green" if self.sound_enabled else "gray"
        text_sound = "SOM: LIGADO" if self.sound_enabled else "SOM: DESLIGADO"
        screen.draw.filled_rect(self.btn_sound, color_sound)
        screen.draw.text(text_sound, center=self.btn_sound.center, fontsize=30, color="white")
        
        # Botão Sair (Vermelho)
        screen.draw.filled_rect(self.btn_exit, "red")
        screen.draw.text("SAIR", center=self.btn_exit.center, fontsize=30, color="white")

    def handle_click(self, pos):
        """Verifica se algum botão foi clicado e retorna a ação correspondente"""
        if self.btn_start.collidepoint(pos):  # Se clicou no botão Iniciar
            return "start"
        elif self.btn_sound.collidepoint(pos):  # Se clicou no botão Som
            self.sound_enabled = not self.sound_enabled  # Alterna o estado do som
            return "toggle_sound"
        elif self.btn_exit.collidepoint(pos):  # Se clicou no botão Sair
            return "exit"
        return None  # Se clicou fora dos botões
