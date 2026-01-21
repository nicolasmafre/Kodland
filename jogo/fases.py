from pgzero.builtins import Actor
from jogo.constantes import *
from jogo.inimigos import SpikeEnemy, WingEnemy
import random

class Level:
    def __init__(self):
        self.platforms = []
        self.decorations = []
        self.coins = []
        self.enemies = []
        
        self.bg = Actor('fundo/fundo')
        self.bg.pos = (WIDTH//2, HEIGHT//2)
        
        self.hud_coin = Actor('objetos/moedas_bronze', (WIDTH - 100, 30))
        self.hud_life = Actor('objetos/vidas', (WIDTH - 150, 30))
        
        self.setup_level()

    def setup_level(self):
        self.platforms = []
        self.decorations = []
        self.coins = []
        self.enemies = []

        # Chão principal
        for i in range(0, WIDTH + 70, 70):
            plat = Actor('ambiente/fase01-piso_normal', (i + 35, HEIGHT - 35))
            self.platforms.append(plat)

        # Plataformas flutuantes (Ajustadas para 1200x800)
        self.create_platform(200, HEIGHT - 180, 3)
        self.create_platform(800, HEIGHT - 280, 4)
        self.create_platform(100, HEIGHT - 400, 3)
        self.create_platform(600, HEIGHT - 500, 3)
        self.create_platform(300, HEIGHT - 620, 2)
        self.create_platform(900, HEIGHT - 650, 3)

        # Decoração aleatória
        for _ in range(10):
            x = random.randint(50, WIDTH-50)
            y = HEIGHT - 100
            img = f'ambiente/fase01-{random.randint(1,4)}_paisagem'
            deco = Actor(img, (x, y))
            self.decorations.append(deco)

        # Moedas (Bronze)
        coin_positions = [
            (200, HEIGHT - 230), 
            (800, HEIGHT - 330), 
            (100, HEIGHT - 450), 
            (600, HEIGHT - 550),
            (300, HEIGHT - 670),
            (950, HEIGHT - 700)
        ]
        for pos in coin_positions:
            coin = Actor('objetos/bronze_1', pos)
            self.coins.append(coin)

        # Inimigos
        # Espinho um pouco mais alto (y=HEIGHT-95) para ficar "em cima" do chão visualmente
        self.enemies.append(SpikeEnemy(600, HEIGHT - 95)) 
        
        # Voador um pouco mais baixo (y=400)
        self.enemies.append(WingEnemy(500, 400))

    def create_platform(self, x, y, size):
        for i in range(size):
            plat = Actor('ambiente/fase01-piso_pequeno', (x + i*70, y))
            self.platforms.append(plat)

    def update(self, player):
        # Atualizar inimigos
        for enemy in self.enemies:
            enemy.update()
            if player.colliderect(enemy):
                player.take_damage()

        # Coletar moedas
        for coin in self.coins[:]:
            coin.angle += 2
            if player.colliderect(coin):
                self.coins.remove(coin)
        
        return len(self.coins) == 0

    def draw(self):
        self.bg.draw()
        for deco in self.decorations:
            deco.draw()
        for plat in self.platforms:
            plat.draw()
        for coin in self.coins:
            coin.draw()
        for enemy in self.enemies:
            enemy.draw()
        
        self.hud_coin.draw()
        self.hud_life.draw()
