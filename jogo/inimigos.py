from pgzero.builtins import Actor  # Importa a classe base para objetos do jogo
from jogo.constantes import *  # Importa constantes globais
import random  # Importa para comportamento aleatório

class Enemy(Actor):
    def __init__(self, x, y, image_list, speed, is_flying=False):
        # Inicializa o inimigo com a primeira imagem da lista
        super().__init__(image_list[0], (x, y))
        self.images = image_list  # Guarda lista de sprites para animação
        self.speed = speed  # Velocidade de movimento
        self.is_flying = is_flying  # Define se é voador ou terrestre
        
        # Variáveis de animação
        self.timer = 0
        self.frame_index = 0
        self.anim_timer = 0
        
        # Física para inimigos terrestres
        self.vy = 0
        
        # Lógica de patrulha
        self.start_x = x
        self.start_y = y
        self.direction = 1  # 1 para direita, -1 para esquerda
        self.move_timer = 0
        self.state = "moving" # Estados: "moving" (andando) ou "waiting" (esperando)

    def update(self):
        """Atualiza a lógica do inimigo"""
        self.animate()  # Atualiza sprite
        
        if self.is_flying:
            # Lógica de Voo (Asas)
            self.y += self.speed * self.direction  # Move verticalmente
            # Se afastar muito do ponto inicial, inverte direção
            if abs(self.y - self.start_y) > 250:
                self.direction *= -1
        else:
            # Lógica Terrestre (Espinho)
            
            # Aplica Gravidade
            self.vy += GRAVITY
            self.y += self.vy
            
            # Colisão simples com o chão (mantém na altura inicial Y)
            if self.y >= self.start_y:
                self.y = self.start_y
                self.vy = 0
            
            # Pulo Aleatório
            if self.state == "moving" and self.y == self.start_y:
                # 1% de chance de pular a cada frame enquanto anda
                if random.randint(0, 100) < 1:
                    self.vy = -18  # Aplica força de pulo

            # Máquina de Estados de Movimento
            if self.state == "moving":
                self.x += self.speed * self.direction  # Move horizontalmente
                
                # Verifica limites da tela para inverter direção
                # Se bater na borda direita E estiver indo para a direita
                if self.x > WIDTH - 50 and self.direction > 0:
                    self.direction = -1 # Força ir para a esquerda
                    self.state = "waiting" # Entra em estado de espera
                
                # Se bater na borda esquerda E estiver indo para a esquerda
                elif self.x < 50 and self.direction < 0:
                    self.direction = 1 # Força ir para a direita
                    self.state = "waiting" # Entra em estado de espera
            
            elif self.state == "waiting":
                self.move_timer += 1
                if self.move_timer > 60: # Espera 1 segundo (60 frames)
                    self.state = "moving"  # Volta a andar
                    self.move_timer = 0

    def animate(self):
        """Cicla entre as imagens da lista para animar"""
        self.anim_timer += 1
        if self.anim_timer > 10:  # Troca a cada 10 frames
            self.frame_index = (self.frame_index + 1) % len(self.images)
            self.image = self.images[self.frame_index]
            self.anim_timer = 0

class SpikeEnemy(Enemy):
    def __init__(self, x, y):
        # Define as imagens específicas do Espinho
        images = ['inimigos/espinho_andando01', 'inimigos/espinho_andando02']
        # Inicializa como inimigo terrestre
        super().__init__(x, y, images, speed=ENEMY_SPEED, is_flying=False)

class WingEnemy(Enemy):
    def __init__(self, x, y):
        # Define as imagens específicas do Asas
        images = ['inimigos/asas01', 'inimigos/asas02', 'inimigos/asas03', 'inimigos/asas04']
        # Inicializa como inimigo voador (mais rápido)
        super().__init__(x, y, images, speed=ENEMY_SPEED + 1, is_flying=True)
