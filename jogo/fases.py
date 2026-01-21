from pgzero.builtins import Actor  # Importa Actor para criar objetos do jogo
from jogo.constantes import *  # Importa constantes globais
from jogo.inimigos import SpikeEnemy, WingEnemy  # Importa classes de inimigos
import random  # Importa random para geração procedural de decoração

class Level:
    def __init__(self):
        # Listas para armazenar os objetos do nível
        self.platforms = []
        self.decorations = []
        self.coins = []
        self.enemies = []
        
        # Configura o fundo
        self.bg = Actor('fundo/fundo')
        self.bg.pos = (WIDTH//2, HEIGHT//2)  # Centraliza o fundo
        
        # Configura o HUD (Interface)
        self.hud_life = Actor('objetos/vidas', (50, 30)) # Ícone de vida na esquerda
        self.hud_coin = Actor('objetos/moedas_bronze', (WIDTH - 100, 30)) # Ícone de moeda na direita
        
        self.setup_level()  # Chama a função que constrói o nível

    def setup_level(self):
        """Cria e posiciona todos os elementos do nível"""
        # Limpa as listas para reiniciar o nível limpo
        self.platforms = []
        self.decorations = []
        self.coins = []
        self.enemies = []

        # Cria o chão principal
        # Loop preenche a largura da tela com blocos de chão
        for i in range(0, WIDTH + 70, 70):
            plat = Actor('ambiente/fase01-piso_normal', (i + 35, HEIGHT - 35))
            self.platforms.append(plat)

        # Cria plataformas flutuantes em posições estratégicas
        self.create_platform(200, HEIGHT - 180, 3)
        self.create_platform(800, HEIGHT - 280, 4)
        self.create_platform(100, HEIGHT - 400, 3)
        self.create_platform(600, HEIGHT - 500, 3)
        self.create_platform(300, HEIGHT - 620, 2)
        self.create_platform(900, HEIGHT - 650, 3)

        # Adiciona decoração aleatória no fundo (arbustos/pedras)
        for _ in range(10):
            x = random.randint(50, WIDTH-50)
            y = HEIGHT - 100
            # Escolhe aleatoriamente entre 4 imagens de paisagem
            img = f'ambiente/fase01-{random.randint(1,4)}_paisagem'
            deco = Actor(img, (x, y))
            self.decorations.append(deco)

        # Posiciona as moedas de bronze
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

        # Cria os Inimigos
        # Espinho começa no meio para patrulhar para os lados
        self.enemies.append(SpikeEnemy(WIDTH//2, HEIGHT - 95))
        # Asas começa voando no meio da tela
        self.enemies.append(WingEnemy(500, 400))          

    def create_platform(self, x, y, size):
        """Função auxiliar para criar uma plataforma de tamanho variável"""
        for i in range(size):
            plat = Actor('ambiente/fase01-piso_pequeno', (x + i*70, y))
            self.platforms.append(plat)

    def update(self, player):
        """Atualiza a lógica do nível (inimigos e moedas)"""
        # Atualiza inimigos e verifica colisão com jogador
        for enemy in self.enemies:
            enemy.update()
            if player.colliderect(enemy):
                player.take_damage()

        # Atualiza moedas (animação e coleta)
        for coin in self.coins[:]:  # Itera sobre cópia para permitir remoção
            coin.angle += 2  # Gira a moeda
            if player.colliderect(coin):
                self.coins.remove(coin)  # Remove moeda coletada
        
        # Retorna True se todas as moedas foram coletadas (Vitória)
        return len(self.coins) == 0

    def draw(self):
        """Desenha todos os elementos do nível na ordem correta"""
        self.bg.draw()  # Fundo primeiro
        for deco in self.decorations:
            deco.draw()
        for plat in self.platforms:
            plat.draw()
        for coin in self.coins:
            coin.draw()
        for enemy in self.enemies:
            enemy.draw()  # Inimigos por cima
        
        # Desenha o HUD por último (interface)
        self.hud_coin.draw()
        self.hud_life.draw()
