import random  # Importa biblioteca para números aleatórios
import math  # Importa biblioteca matemática para cálculos de distância
from pgzero.builtins import Rect  # Importa Rect para os inimigos
from jogo.constantes import WIDTH, HEIGHT, ENEMY_COUNT  # Importa constantes

class EnemyManager:
    def __init__(self):
        """Inicializa o gerenciador de inimigos"""
        self.enemies = []  # Lista para armazenar os dicionários de inimigos

    def init_enemies(self, player_rect):
        """Cria os inimigos em posições aleatórias, longe do jogador"""
        self.enemies = []
        for _ in range(ENEMY_COUNT):
            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)
            
            # Loop para garantir que o inimigo não nasça muito perto do jogador (distância mínima de 150px)
            while math.hypot(x - player_rect.centerx, y - player_rect.centery) < 150:
                x = random.randint(0, WIDTH)
                y = random.randint(0, HEIGHT)
            
            enemy_rect = Rect(x, y, 25, 25)  # Cria o retângulo do inimigo
            
            # Define velocidades aleatórias para X e Y, evitando 0 para que sempre se movam
            vx = random.choice([-4, -3, 3, 4])
            vy = random.choice([-4, -3, 3, 4])
            
            # Adiciona o inimigo à lista como um dicionário contendo o Rect e as velocidades
            self.enemies.append({'rect': enemy_rect, 'vx': vx, 'vy': vy})

    def update(self):
        """Atualiza a posição de todos os inimigos"""
        for enemy in self.enemies:
            r = enemy['rect']
            r.x += enemy['vx']  # Move no eixo X
            r.y += enemy['vy']  # Move no eixo Y
            
            # Lógica de rebatimento nas paredes (inverte a velocidade se tocar na borda)
            if r.left < 0 or r.right > WIDTH:
                enemy['vx'] *= -1
            if r.top < 0 or r.bottom > HEIGHT:
                enemy['vy'] *= -1

    def check_collision(self, player_rect):
        """Verifica se algum inimigo colidiu com o jogador"""
        for enemy in self.enemies:
            if player_rect.colliderect(enemy['rect']):
                return True  # Retorna True se houver colisão
        return False  # Retorna False se não houver colisão

    def draw(self, screen):
        """Desenha todos os inimigos na tela"""
        for enemy in self.enemies:
            screen.draw.filled_rect(enemy['rect'], "red")
