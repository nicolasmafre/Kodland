import pgzrun
from pgzero.builtins import keyboard, music, keys

from jogo.constantes import *
from jogo.personagens import Player
from jogo.fases import Level
from jogo.menu import Menu

# Inicialização
player = Player()
level = Level()
menu = Menu()

state = MENU

def manage_music():
    """Gerencia a música usando o sistema nativo do PgZero"""
    try:
        if menu.sound_enabled:
            if not music.is_playing('musica_fundo'):
                music.play('musica_fundo')
                music.set_volume(0.5)
        else:
            music.stop()
    except Exception as e:
        print(f"Aviso: Erro ao tocar música: {e}")

def update():
    global state
    
    if state == MENU:
        manage_music()

    if state == GAME:
        player.update(level.platforms)
        level_complete = level.update(player)
        
        if player.lives <= 0:
            state = GAME_OVER
        elif level_complete:
            state = VICTORY

    elif state in (GAME_OVER, VICTORY):
        if keyboard.space:
            state = MENU
            player.lives = 3
            player.reset_position()
            level.setup_level()

def draw():
    screen.clear()
    
    if state == MENU:
        menu.draw(screen)
    elif state == GAME:
        level.draw()
        player.draw()
        screen.draw.text(f"x {len(level.coins)}", pos=(WIDTH - 70, 20), fontsize=30, color="white")
        screen.draw.text(f"x {player.lives}", pos=(WIDTH - 120, 20), fontsize=30, color="white")
    elif state == GAME_OVER:
        screen.draw.text("GAME OVER", center=(WIDTH//2, HEIGHT//2), fontsize=60, color="red")
        screen.draw.text("Pressione ESPAÇO", center=(WIDTH//2, HEIGHT//2 + 60), fontsize=30, color="white")
    elif state == VICTORY:
        screen.draw.text("VITÓRIA!", center=(WIDTH//2, HEIGHT//2), fontsize=60, color="green")
        screen.draw.text("Pressione ESPAÇO", center=(WIDTH//2, HEIGHT//2 + 60), fontsize=30, color="white")

def on_mouse_down(pos):
    global state
    if state == MENU:
        action = menu.handle_click(pos)
        if action == "start":
            state = GAME
        elif action == "toggle_sound":
            manage_music()
        elif action == "exit":
            quit()

def on_key_down(key):
    """Evento de tecla pressionada para pulo preciso"""
    if state == GAME:
        if key == keys.UP:
            player.jump()

pgzrun.go()
