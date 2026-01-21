# Aventura do Coelho (Platformer)

Um jogo de plataforma desenvolvido em Python utilizando **apenas** a biblioteca **PgZero**, sem dependências diretas do Pygame.

## ⚠️ IMPORTANTE: Estrutura de Pastas

Para que o PgZero funcione corretamente, as pastas de recursos **DEVEM** ter os seguintes nomes em inglês (padrão da biblioteca):

1.  Renomeie a pasta `imagens` para **`images`**.
2.  Renomeie a pasta `musica` para **`music`**.

A estrutura final deve ser:

```
Kodland/
│
├── main.py                 # Arquivo principal
├── images/                 # (Antiga 'imagens') Contém todos os gráficos
│   ├── ambiente/
│   ├── fundo/
│   ├── inimigos/
│   ├── objetos/
│   └── personagem/
│
├── music/                  # (Antiga 'musica') Contém o áudio
│   └── musica_fundo.mp3
│
└── jogo/                   # Código fonte modular
    ├── constantes.py
    ├── personagens.py
    ├── inimigos.py
    ├── fases.py
    └── menu.py
```

## 🎮 Como Jogar

1.  **Objetivo**: Colete todas as 4 moedas de bronze para vencer.
2.  **Controles**:
    *   **Setas Esquerda/Direita**: Mover o coelho.
    *   **Seta Cima**: Pular.
3.  **Inimigos**:
    *   **Espinho**: Patrulha o chão. Evite-o!
    *   **Asas**: Voa para cima e para baixo.
4.  **Vidas**: Você tem 3 vidas. Se tocar em um inimigo, perde uma vida e volta ao início.

## 🛠️ Requisitos Técnicos

*   **Bibliotecas**: Apenas `pgzero`, `math`, `random`.
*   **Sem Pygame**: O código não importa `pygame` diretamente.
*   **Animação**: Sprites animados para o jogador (parado, andando, pulando) e inimigos.
