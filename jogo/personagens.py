from pgzero.builtins import Rect, keyboard  # Importa Rect para geometria e keyboard para entrada
from jogo.constantes import WIDTH, HEIGHT, PLAYER_SPEED  # Importa constantes necessárias

class Player:
    def __init__(self):
        """Inicializa o jogador"""
        self.rect = Rect(400, 300, 30, 30)  # Cria um retângulo na posição (400, 300) com tamanho 30x30
        self.color = "yellow"  # Cor do jogador

    def reset_position(self):
        """Reseta a posição do jogador para o centro da tela"""
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

    def update(self):
        """Atualiza a posição do jogador baseado nas teclas pressionadas"""
        if keyboard.left:
            self.rect.x -= PLAYER_SPEED  # Move para a esquerda
        if keyboard.right:
            self.rect.x += PLAYER_SPEED  # Move para a direita
        if keyboard.up:
            self.rect.y -= PLAYER_SPEED  # Move para cima
        if keyboard.down:
            self.rect.y += PLAYER_SPEED  # Move para baixo
            
        # Manter jogador dentro dos limites da tela
        if self.rect.left < 0: self.rect.left = 0
        if self.rect.right > WIDTH: self.rect.right = WIDTH
        if self.rect.top < 0: self.rect.top = 0
        if self.rect.bottom > HEIGHT: self.rect.bottom = HEIGHT

    def draw(self, screen):
        """Desenha o jogador na tela"""
        screen.draw.filled_rect(self.rect, self.color)
