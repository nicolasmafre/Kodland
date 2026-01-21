from pgzero.builtins import Actor
from jogo.constantes import *
import random

class Enemy(Actor):
    def __init__(self, x, y, image_list, speed, is_flying=False):
        super().__init__(image_list[0], (x, y))
        self.images = image_list
        self.speed = speed
        self.is_flying = is_flying
        self.timer = 0
        self.frame_index = 0
        self.anim_timer = 0
        
        # Física para inimigos terrestres
        self.vy = 0
        
        # Lógica de patrulha
        self.start_x = x
        self.start_y = y
        self.direction = 1
        self.move_timer = 0
        self.state = "moving" # moving, waiting

    def update(self):
        self.animate()
        
        if self.is_flying:
            # Voar para cima e para baixo com maior amplitude
            self.y += self.speed * self.direction
            if abs(self.y - self.start_y) > 250:
                self.direction *= -1
        else:
            # Lógica Terrestre (Espinho)
            
            # Gravidade
            self.vy += GRAVITY
            self.y += self.vy
            
            # Colisão simples com o chão original
            if self.y >= self.start_y:
                self.y = self.start_y
                self.vy = 0
            
            # Pulo Aleatório (apenas se estiver no chão e se movendo)
            if self.state == "moving" and self.y == self.start_y:
                if random.randint(0, 100) < 1:
                    self.vy = -18

            # Andar, parar, voltar
            if self.state == "moving":
                self.x += self.speed * self.direction
                
                # Verifica limites da tela para inverter direção
                # Se bater na borda direita E estiver indo para a direita
                if self.x > WIDTH - 50 and self.direction > 0:
                    self.direction = -1 # Força ir para a esquerda
                    self.state = "waiting"
                
                # Se bater na borda esquerda E estiver indo para a esquerda
                elif self.x < 50 and self.direction < 0:
                    self.direction = 1 # Força ir para a direita
                    self.state = "waiting"
                
                # Removemos o timer de segurança que estava forçando a parada antes da hora
                # self.move_timer += 1 ...
            
            elif self.state == "waiting":
                self.move_timer += 1
                if self.move_timer > 60: # Espera 1 segundo
                    self.state = "moving"
                    self.move_timer = 0
                    # A direção já foi invertida no bloco anterior, não inverte aqui novamente

    def animate(self):
        self.anim_timer += 1
        if self.anim_timer > 10:
            self.frame_index = (self.frame_index + 1) % len(self.images)
            self.image = self.images[self.frame_index]
            self.anim_timer = 0

class SpikeEnemy(Enemy):
    def __init__(self, x, y):
        images = ['inimigos/espinho_andando01', 'inimigos/espinho_andando02']
        super().__init__(x, y, images, speed=ENEMY_SPEED, is_flying=False)

class WingEnemy(Enemy):
    def __init__(self, x, y):
        images = ['inimigos/asas01', 'inimigos/asas02', 'inimigos/asas03', 'inimigos/asas04']
        super().__init__(x, y, images, speed=ENEMY_SPEED + 1, is_flying=True)
