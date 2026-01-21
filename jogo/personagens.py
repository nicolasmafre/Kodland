from pgzero.builtins import Actor, keyboard  # Importa Actor para sprites e keyboard para entrada
from jogo.constantes import *  # Importa constantes globais

class Player(Actor):
    def __init__(self):
        # Inicializa o Actor com a imagem padrão e posição inicial
        super().__init__('personagem/coelho_parado01', (100, 400))
        self.vx = 0  # Velocidade horizontal
        self.vy = 0  # Velocidade vertical
        self.on_ground = False  # Flag para verificar se está no chão
        self.jump_count = 0  # Contador para controle de pulo duplo
        self.lives = 3  # Quantidade de vidas
        self.is_hurt = False  # Estado de dano (invencibilidade temporária)
        self.hurt_timer = 0  # Timer para duração do estado de dano
        
        # Variáveis de Animação
        self.anim_timer = 0
        self.frame_index = 0
        self.facing_right = True  # Direção que o personagem está olhando
        
        # Listas de imagens para animação
        self.img_idle = ['personagem/coelho_parado01', 'personagem/coelho_parado02']
        self.img_walk = ['personagem/coelho_andando01', 'personagem/coelho_andando02']
        self.img_jump = 'personagem/coelho_pulando'
        self.img_hurt = 'personagem/coelho_machucado'

    def jump(self):
        """Executa o pulo se tiver pulos restantes (Pulo Duplo)"""
        if self.jump_count < 2:  # Permite pular se pulou menos de 2 vezes
            self.vy = JUMP_POWER  # Aplica força vertical
            self.on_ground = False  # Sai do chão
            self.jump_count += 1  # Incrementa contador

    def update(self, platforms):
        """Atualiza a lógica do jogador a cada frame"""
        # Lógica de Dano
        if self.is_hurt:
            self.image = self.img_hurt  # Muda sprite para machucado
            self.hurt_timer -= 1
            if self.hurt_timer <= 0:  # Se acabou o tempo de dano
                self.is_hurt = False
                self.reset_position()  # Volta para o início
            return  # Não processa movimento enquanto machucado

        # Movimento Horizontal (Teclado)
        self.vx = 0
        if keyboard.left:
            self.vx = -SPEED
            self.facing_right = False
        elif keyboard.right:
            self.vx = SPEED
            self.facing_right = True

        # Física Vertical (Gravidade)
        self.vy += GRAVITY
        
        # Aplica movimento às coordenadas
        self.x += self.vx
        self.y += self.vy

        # Colisão com plataformas
        self.on_ground = False
        for plat in platforms:
            # Verifica colisão apenas se estiver caindo (vy >= 0)
            if self.colliderect(plat) and self.vy >= 0:
                # Ajuste fino: verifica se os pés estavam acima da plataforma antes
                if self.bottom - self.vy <= plat.top + 10: 
                    self.bottom = plat.top  # Corrige posição para cima da plataforma
                    self.vy = 0  # Zera velocidade vertical
                    self.on_ground = True
                    self.jump_count = 0  # Reseta o pulo duplo ao tocar o chão

        # Limites da tela
        if self.left < 0: self.left = 0
        if self.right > WIDTH: self.right = WIDTH
        if self.top > HEIGHT: # Se cair no buraco
            self.take_damage()

        self.animate()  # Atualiza o sprite

    def animate(self):
        """Gerencia a troca de sprites baseada no estado"""
        if not self.on_ground:
            self.image = self.img_jump  # Sprite de pulo
        elif self.vx != 0:
            # Animação de caminhada
            self.anim_timer += 1
            if self.anim_timer > 10:  # Troca a cada 10 frames
                self.frame_index = (self.frame_index + 1) % 2
                self.anim_timer = 0
            self.image = self.img_walk[self.frame_index]
        else:
            # Animação parado
            self.anim_timer += 1
            if self.anim_timer > 20:  # Troca a cada 20 frames (mais lento)
                self.frame_index = (self.frame_index + 1) % 2
                self.anim_timer = 0
            self.image = self.img_idle[self.frame_index]

    def take_damage(self):
        """Aplica dano ao jogador"""
        if not self.is_hurt:
            self.lives -= 1
            self.is_hurt = True
            self.hurt_timer = 60 # Fica invulnerável/parado por 1 segundo (60 frames)
            self.vy = -10 # Pequeno pulo de feedback de dano

    def reset_position(self):
        """Reseta o jogador para a posição inicial"""
        self.pos = (100, 400)
        self.vx = 0
        self.vy = 0
        self.jump_count = 0
