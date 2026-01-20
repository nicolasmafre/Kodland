import random  # Importa random para posicionar moedas
from pgzero.builtins import Rect  # Importa Rect para as moedas
from jogo.constantes import WIDTH, HEIGHT, COIN_COUNT  # Importa constantes

class Level1:
    def __init__(self):
        """Inicializa a Fase 1"""
        self.coins = []  # Lista de moedas
        self.score = 0  # Pontuação atual
    
    def start(self):
        """Configura o início da fase, espalhando as moedas"""
        self.coins = []
        self.score = 0
        for _ in range(COIN_COUNT):
            # Gera posições aleatórias com uma margem de 50px das bordas
            x = random.randint(50, WIDTH - 50)
            y = random.randint(50, HEIGHT - 50)
            self.coins.append(Rect(x, y, 15, 15))  # Adiciona moeda (quadrado 15x15)

    def update(self, player_rect, sound_enabled):
        """Verifica colisões entre jogador e moedas"""
        # Itera sobre uma cópia da lista ([:]) para poder remover itens durante o loop
        for coin in self.coins[:]:
            if player_rect.colliderect(coin):  # Se houver colisão
                self.coins.remove(coin)  # Remove a moeda da lista
                self.score += 1  # Aumenta a pontuação
                if sound_enabled:
                    print("Som: Moeda coletada!")  # Placeholder de som
        
        # Retorna True se todas as moedas foram coletadas (Fim da fase)
        return self.score >= COIN_COUNT

    def draw(self, screen):
        """Desenha o HUD da fase e as moedas"""
        # Desenha o texto com a contagem de moedas
        screen.draw.text(f"Fase 1: Colete {COIN_COUNT} moedas! ({self.score}/{COIN_COUNT})", topleft=(10, 10), fontsize=30, color="white")
        # Desenha todas as moedas restantes
        for coin in self.coins:
            screen.draw.filled_circle(coin.center, 7, "gold")
