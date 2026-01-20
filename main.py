import pgzrun
import pygame
import os
from pgzero.builtins import keyboard

from jogo.constantes import *
from jogo.personagens import Player
from jogo.inimigos import EnemyManager
from jogo.fases import Level1
from jogo.menu import Menu

# Inicialização de Objetos
player = Player()
enemy_manager = EnemyManager()
level1 = Level1()
menu = Menu()

# Variáveis de Estado Global
state = MENU
survival_time = 0

# Variável para controlar se a música já foi iniciada
music_started = False

def manage_music():
    """Gerencia a música de fundo baseada na configuração de som"""
    global music_started
    
    # Caminho absoluto para garantir que o arquivo seja encontrado
    music_path = os.path.join("musica", "musica_fundo.mp3")
    
    try:
        if menu.sound_enabled:
            if not pygame.mixer.music.get_busy():
                print(f"Tentando carregar música de: {os.path.abspath(music_path)}")
                if os.path.exists(music_path):
                    pygame.mixer.music.load(music_path)
                    pygame.mixer.music.play(-1)
                    music_started = True
                    print("Música iniciada com sucesso.")
                else:
                    print(f"ERRO: Arquivo não encontrado: {os.path.abspath(music_path)}")
        else:
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()
                music_started = False
                print("Música parada.")
    except Exception as e:
        print(f"Erro ao manipular música: {e}")

def draw():
    screen.clear()
    
    if state == MENU:
        menu.draw(screen)
    elif state == LEVEL1:
        level1.draw(screen)
        player.draw(screen)
    elif state == LEVEL2:
        draw_level2_ui()
        player.draw(screen)
        enemy_manager.draw(screen)
    elif state == GAME_OVER:
        draw_message("GAME OVER", "red", "Pressione ESPAÇO para voltar")
    elif state == VICTORY:
        draw_message("VITÓRIA!", "green", "Pressione ESPAÇO para voltar")

def draw_level2_ui():
    time_left = max(0, TARGET_TIME - survival_time)
    screen.draw.text(f"Fase 2: Sobreviva! Tempo: {time_left:.1f}s", topleft=(10, 10), fontsize=30, color="white")

def draw_message(title, color, subtitle):
    screen.draw.text(title, center=(WIDTH//2, HEIGHT//2), fontsize=60, color=color)
    screen.draw.text(subtitle, center=(WIDTH//2, HEIGHT//2 + 60), fontsize=30, color="white")

def update(dt):
    global state, survival_time
    
    # Tenta iniciar a música no primeiro frame (quando o mixer já deve estar pronto)
    if state == MENU and menu.sound_enabled and not pygame.mixer.music.get_busy():
         manage_music()

    if state == LEVEL1:
        player.update()
        level_complete = level1.update(player.rect, menu.sound_enabled)
        
        if level_complete:
            state = LEVEL2
            player.reset_position()
            enemy_manager.init_enemies(player.rect)
            survival_time = 0
            
    elif state == LEVEL2:
        player.update()
        enemy_manager.update()
        survival_time += dt
        
        if enemy_manager.check_collision(player.rect):
            state = GAME_OVER
            if menu.sound_enabled:
                print("Som: Game Over!")
        
        if survival_time >= TARGET_TIME:
            state = VICTORY
            if menu.sound_enabled:
                print("Som: Vitória!")

    elif state in (GAME_OVER, VICTORY):
        if keyboard.space:
            state = MENU

def on_mouse_down(pos):
    global state
    
    if state == MENU:
        action = menu.handle_click(pos)
        if action == "start":
            state = LEVEL1
            player.reset_position()
            level1.start()
        elif action == "toggle_sound":
            manage_music()
        elif action == "exit":
            quit()

pgzrun.go()
