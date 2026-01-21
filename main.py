import pgzrun  # Importa a biblioteca principal do Pygame Zero para rodar o jogo
from pgzero.builtins import keyboard, music, keys  # Importa módulos para entrada de teclado e controle de música

# Importa constantes e classes dos módulos do jogo
from jogo.constantes import *  # Importa configurações globais como tamanho da tela e cores
from jogo.personagens import Player  # Importa a classe do jogador
from jogo.fases import Level  # Importa a classe que gerencia o nível
from jogo.menu import Menu  # Importa a classe do menu principal

# Inicialização dos objetos principais do jogo
player = Player()  # Cria uma instância do jogador (coelho)
level = Level()  # Cria uma instância do nível (plataformas, inimigos, moedas)
menu = Menu()  # Cria uma instância do menu

state = MENU  # Define o estado inicial do jogo como o Menu Principal

def manage_music():
    """Gerencia a música de fundo usando o sistema nativo do PgZero"""
    try:
        if menu.sound_enabled:  # Se o som estiver habilitado no menu
            if not music.is_playing('musica_fundo'):  # Se a música não estiver tocando
                music.play('musica_fundo')  # Inicia a música em loop
                music.set_volume(0.5)  # Define o volume para 50%
        else:
            music.stop()  # Para a música se o som for desabilitado
    except Exception as e:
        # Captura erros caso o arquivo de música não seja encontrado
        print(f"Aviso: Erro ao tocar música: {e}")

def update():
    """Função principal de atualização do jogo (chamada a cada frame)"""
    global state  # Permite modificar a variável global de estado
    
    if state == MENU:
        manage_music()  # Garante que a música toque no menu se habilitada

    if state == GAME:
        player.update(level.platforms)  # Atualiza a física e lógica do jogador
        level_complete = level.update(player)  # Atualiza o nível e verifica se completou
        
        if player.lives <= 0:  # Se as vidas acabarem
            state = GAME_OVER  # Muda para tela de derrota
        elif level_complete:  # Se coletar todas as moedas
            state = VICTORY  # Muda para tela de vitória

    elif state in (GAME_OVER, VICTORY):
        if keyboard.space:  # Se pressionar ESPAÇO nas telas finais
            state = MENU  # Volta para o menu
            player.lives = 3  # Reseta as vidas
            player.reset_position()  # Reseta a posição do jogador
            level.setup_level()  # Reinicia o nível (moedas e inimigos)

def draw():
    """Função principal de desenho (chamada a cada frame)"""
    screen.clear()  # Limpa a tela antes de desenhar
    
    if state == MENU:
        menu.draw(screen)  # Desenha o menu
    elif state == GAME:
        level.draw()  # Desenha o cenário (fundo, plataformas, inimigos)
        player.draw()  # Desenha o jogador
        
        # Desenha o HUD (Heads-Up Display)
        # Texto da contagem de moedas (lado direito)
        screen.draw.text(f"x {len(level.coins)}", pos=(WIDTH - 70, 20), fontsize=30, color="white")
        # Texto da contagem de vidas (lado esquerdo)
        screen.draw.text(f"x {player.lives}", pos=(80, 20), fontsize=30, color="white")

    elif state == GAME_OVER:
        # Desenha a tela de Game Over
        screen.draw.text("GAME OVER", center=(WIDTH//2, HEIGHT//2), fontsize=60, color="red")
        screen.draw.text("Pressione ESPAÇO", center=(WIDTH//2, HEIGHT//2 + 60), fontsize=30, color="white")
    elif state == VICTORY:
        # Desenha a tela de Vitória
        screen.draw.text("VITÓRIA!", center=(WIDTH//2, HEIGHT//2), fontsize=60, color="green")
        screen.draw.text("Pressione ESPAÇO", center=(WIDTH//2, HEIGHT//2 + 60), fontsize=30, color="white")

def on_mouse_down(pos):
    """Evento de clique do mouse"""
    global state
    if state == MENU:
        action = menu.handle_click(pos)  # Verifica onde clicou no menu
        if action == "start":
            state = GAME  # Inicia o jogo
        elif action == "toggle_sound":
            manage_music()  # Alterna o som
        elif action == "exit":
            quit()  # Fecha o jogo

def on_key_down(key):
    """Evento de tecla pressionada para ações pontuais"""
    if state == GAME:
        if key == keys.UP:
            player.jump()  # Chama a função de pulo do jogador

pgzrun.go()  # Inicia o loop principal do jogo
