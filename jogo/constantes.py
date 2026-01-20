# Configurações da Janela
WIDTH = 800  # Largura da janela do jogo em pixels
HEIGHT = 600  # Altura da janela do jogo em pixels
TITLE = "Jogo de 2 Fases"  # Título que aparece na barra da janela

# Estados do Jogo (Constantes para controlar o fluxo do jogo)
MENU = "menu"
LEVEL1 = "level1"
LEVEL2 = "level2"
GAME_OVER = "game_over"
VICTORY = "victory"

# Gameplay (Constantes de balanceamento do jogo)
PLAYER_SPEED = 5  # Velocidade de movimento do jogador (pixels por frame)
COIN_COUNT = 5  # Quantidade de moedas para coletar na Fase 1
ENEMY_COUNT = 6  # Quantidade de inimigos na Fase 2
TARGET_TIME = 10.0  # Tempo em segundos para sobreviver na Fase 2