from pgzero.builtins import Actor, keyboard
from jogo.constantes import *

class Player(Actor):
    def __init__(self):
        super().__init__('personagem/coelho_parado01', (100, 400))
        self.vx = 0
        self.vy = 0
        self.on_ground = False
        self.jump_count = 0  # Contador de pulos
        self.lives = 3
        self.is_hurt = False
        self.hurt_timer = 0
        
        # Animação
        self.anim_timer = 0
        self.frame_index = 0
        self.facing_right = True
        
        # Imagens
        self.img_idle = ['personagem/coelho_parado01', 'personagem/coelho_parado02']
        self.img_walk = ['personagem/coelho_andando01', 'personagem/coelho_andando02']
        self.img_jump = 'personagem/coelho_pulando'
        self.img_hurt = 'personagem/coelho_machucado'

    def jump(self):
        """Executa o pulo se tiver pulos restantes (Pulo Duplo)"""
        if self.jump_count < 2:
            self.vy = JUMP_POWER
            self.on_ground = False
            self.jump_count += 1

    def update(self, platforms):
        if self.is_hurt:
            self.image = self.img_hurt
            self.hurt_timer -= 1
            if self.hurt_timer <= 0:
                self.is_hurt = False
                self.reset_position()
            return

        # Movimento Horizontal
        self.vx = 0
        if keyboard.left:
            self.vx = -SPEED
            self.facing_right = False
        elif keyboard.right:
            self.vx = SPEED
            self.facing_right = True

        # Física Vertical
        self.vy += GRAVITY
        
        # Aplicar movimento
        self.x += self.vx
        self.y += self.vy

        # Colisão com plataformas
        self.on_ground = False
        for plat in platforms:
            if self.colliderect(plat) and self.vy >= 0:
                # Ajuste fino para colisão: verifica se os pés estavam acima ou no nível da plataforma antes
                if self.bottom - self.vy <= plat.top + 10: 
                    self.bottom = plat.top
                    self.vy = 0
                    self.on_ground = True
                    self.jump_count = 0  # Reseta o pulo duplo ao tocar o chão

        # Limites da tela
        if self.left < 0: self.left = 0
        if self.right > WIDTH: self.right = WIDTH
        if self.top > HEIGHT: # Caiu no buraco
            self.take_damage()

        self.animate()

    def animate(self):
        if not self.on_ground:
            self.image = self.img_jump
        elif self.vx != 0:
            self.anim_timer += 1
            if self.anim_timer > 10:
                self.frame_index = (self.frame_index + 1) % 2
                self.anim_timer = 0
            self.image = self.img_walk[self.frame_index]
        else:
            self.anim_timer += 1
            if self.anim_timer > 20:
                self.frame_index = (self.frame_index + 1) % 2
                self.anim_timer = 0
            self.image = self.img_idle[self.frame_index]

    def take_damage(self):
        if not self.is_hurt:
            self.lives -= 1
            self.is_hurt = True
            self.hurt_timer = 60 # 1 segundo a 60fps
            self.vy = -10 # Pulo de dano

    def reset_position(self):
        self.pos = (100, 400)
        self.vx = 0
        self.vy = 0
        self.jump_count = 0
