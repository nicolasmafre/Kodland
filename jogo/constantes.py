# Configurações da Tela
WIDTH = 1200  # Largura da janela do jogo em pixels
HEIGHT = 800  # Altura da janela do jogo em pixels
TITLE = "Aventura do Coelho"  # Título da janela

# Cores (Tuplas RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Física e Gameplay
GRAVITY = 0.8  # Força da gravidade que puxa o jogador para baixo
JUMP_POWER = -16  # Força do pulo (negativo pois Y cresce para baixo)
SPEED = 5  # Velocidade de movimento horizontal do jogador
ENEMY_SPEED = 4  # Velocidade de movimento dos inimigos

# Estados do Jogo (Constantes para a máquina de estados)
MENU = 0
GAME = 1
GAME_OVER = 2
VICTORY = 3