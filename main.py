import pgzrun  # Importa a biblioteca principal do Pygame Zero
from pgzero.builtins import keyboard  # Importa o módulo de teclado para detectar teclas pressionadas

# Importa constantes e classes dos outros módulos do jogo
from jogo.constantes import *
from jogo.personagens import Player
from jogo.inimigos import EnemyManager
from jogo.fases import Level1
from jogo.menu import Menu

# Inicialização de Objetos
player = Player()  # Cria a instância do jogador
enemy_manager = EnemyManager()  # Cria o gerenciador de inimigos
level1 = Level1()  # Cria a instância da Fase 1
menu = Menu()  # Cria a instância do Menu

# Variáveis de Estado Global
state = MENU  # Define o estado inicial do jogo como o Menu
survival_time = 0  # Inicializa o tempo de sobrevivência da Fase 2

def manage_music():
    """Gerencia a música de fundo baseada na configuração de som"""
    try:
        if menu.sound_enabled:  # Se o som estiver habilitado no menu
            # Apenas inicia se não estiver tocando a música correta
            if not musica.is_playing("musica_fundo"):
                musica.play("musica_fundo")  # Toca a música em loop
        else:
            musica.stop()  # Para a música se o som estiver desabilitado
    except Exception:
        # Evita erro se o arquivo não existir ou a pasta 'musica' não for encontrada
        print("Aviso: Para música, crie a pasta 'musica' e adicione 'musica_fundo.mp3'")

# Tenta iniciar a música ao carregar o jogo
manage_music()

def draw():
    """Função principal de desenho do Pygame Zero, chamada a cada quadro"""
    screen.clear()  # Limpa a tela antes de desenhar o novo quadro
    
    if state == MENU:
        menu.draw(screen)  # Desenha o menu se o estado for MENU
    elif state == LEVEL1:
        level1.draw(screen)  # Desenha os elementos da Fase 1
        player.draw(screen)  # Desenha o jogador
    elif state == LEVEL2:
        draw_level2_ui()  # Desenha a interface da Fase 2 (tempo)
        player.draw(screen)  # Desenha o jogador
        enemy_manager.draw(screen)  # Desenha os inimigos
    elif state == GAME_OVER:
        draw_message("GAME OVER", "red", "Pressione ESPAÇO para voltar")  # Tela de derrota
    elif state == VICTORY:
        draw_message("VITÓRIA!", "green", "Pressione ESPAÇO para voltar")  # Tela de vitória

def draw_level2_ui():
    """Desenha o tempo restante na Fase 2"""
    time_left = max(0, TARGET_TIME - survival_time)  # Calcula o tempo restante, não deixando ser negativo
    screen.draw.text(f"Fase 2: Sobreviva! Tempo: {time_left:.1f}s", topleft=(10, 10), fontsize=30, color="white")

def draw_message(title, color, subtitle):
    """Função auxiliar para desenhar mensagens de fim de jogo (Vitória/Derrota)"""
    screen.draw.text(title, center=(WIDTH//2, HEIGHT//2), fontsize=60, color=color)
    screen.draw.text(subtitle, center=(WIDTH//2, HEIGHT//2 + 60), fontsize=30, color="white")

def update(dt):
    """Função principal de atualização do Pygame Zero, chamada a cada quadro"""
    global state, survival_time  # Permite modificar as variáveis globais
    
    if state == LEVEL1:
        player.update()  # Atualiza a posição do jogador
        level_complete = level1.update(player.rect, menu.sound_enabled)  # Atualiza a lógica da fase 1
        
        if level_complete:  # Se coletou todas as moedas
            state = LEVEL2  # Muda para a Fase 2
            player.reset_position()  # Reseta a posição do jogador para o centro
            enemy_manager.init_enemies(player.rect)  # Inicializa os inimigos longe do jogador
            survival_time = 0  # Reseta o tempo de sobrevivência
            
    elif state == LEVEL2:
        player.update()  # Atualiza a posição do jogador
        enemy_manager.update()  # Atualiza a posição dos inimigos
        survival_time += dt  # Incrementa o tempo de sobrevivência com o tempo delta (dt)
        
        if enemy_manager.check_collision(player.rect):  # Verifica colisão com inimigos
            state = GAME_OVER  # Muda o estado para Game Over
            if menu.sound_enabled:
                print("Som: Game Over!")  # Placeholder para som de derrota
        
        if survival_time >= TARGET_TIME:  # Se sobreviveu pelo tempo alvo
            state = VICTORY  # Muda o estado para Vitória
            if menu.sound_enabled:
                print("Som: Vitória!")  # Placeholder para som de vitória

    elif state in (GAME_OVER, VICTORY):
        if keyboard.space:  # Se pressionar ESPAÇO nas telas finais
            state = MENU  # Volta para o menu

def on_mouse_down(pos):
    """Evento de clique do mouse"""
    global state
    
    if state == MENU:
        action = menu.handle_click(pos)  # Verifica onde clicou no menu
        if action == "start":
            state = LEVEL1  # Inicia o jogo
            player.reset_position()
            level1.start()  # Reinicia as moedas da Fase 1
        elif action == "toggle_sound":
            manage_music() # Atualiza a música imediatamente ao clicar no botão de som
        elif action == "exit":
            quit()  # Fecha o jogo

pgzrun.go()  # Inicia o loop principal do jogo
