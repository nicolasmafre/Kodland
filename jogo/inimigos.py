from pgzero.builtins import Actor
from jogo.constantes import *

class Enemy(Actor):
    def __init__(self, x, y, image_list, speed, is_flying=False):
        super().__init__(image_list[0], (x, y))
        self.images = image_list
        self.speed = speed
        self.is_flying = is_flying
        self.timer = 0
        self.frame_index = 0
        self.anim_timer = 0
        
        # Lógica de patrulha
        self.start_x = x
        self.start_y = y
        self.direction = 1
        self.move_timer = 0
        self.state = "moving" # moving, waiting

    def update(self):
        self.animate()
        
        if self.is_flying:
            # Voar para cima e para baixo
            self.y += self.speed * self.direction
            if abs(self.y - self.start_y) > 100:
                self.direction *= -1
        else:
            # Andar, parar, voltar
            if self.state == "moving":
                self.x += self.speed * self.direction
                self.move_timer += 1
                
                # Anda por cerca de 2 segundos (120 frames)
                if self.move_timer > 120:
                    self.state = "waiting"
                    self.move_timer = 0
            
            elif self.state == "waiting":
                self.move_timer += 1
                if self.move_timer > 120: # Espera 2 segundos
                    self.state = "moving"
                    self.move_timer = 0
                    self.direction *= -1 # Inverte direção

    def animate(self):
        self.anim_timer += 1
        if self.anim_timer > 10:
            self.frame_index = (self.frame_index + 1) % len(self.images)
            self.image = self.images[self.frame_index]
            self.anim_timer = 0

class SpikeEnemy(Enemy):
    def __init__(self, x, y):
        images = ['inimigos/espinho_andando01', 'inimigos/espinho_andando02']
        super().__init__(x, y, images, speed=2, is_flying=False)

class WingEnemy(Enemy):
    def __init__(self, x, y):
        images = ['inimigos/asas01', 'inimigos/asas02', 'inimigos/asas03', 'inimigos/asas04']
        super().__init__(x, y, images, speed=3, is_flying=True)
