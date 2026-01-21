# Aventura do Coelho (Platformer)

Um jogo de plataforma vibrante e divertido desenvolvido em Python utilizando **apenas** a biblioteca **PgZero**. O projeto foi estruturado para ser modular, limpo e seguir boas práticas de programação.

## 🎮 Sobre o Jogo

Neste jogo, você controla um coelho aventureiro que precisa coletar moedas de bronze espalhadas por um cenário cheio de plataformas flutuantes e perigos.

### Principais Funcionalidades:
*   **Mecânica de Pulo Duplo**: O coelho pode pular duas vezes consecutivas para alcançar lugares altos.
*   **Inimigos com IA Simples**:
    *   **Espinho**: Patrulha o chão, indo e voltando.
    *   **Asas**: Voa verticalmente, bloqueando caminhos aéreos.
*   **Sistema de Vidas**: O jogador possui 3 vidas. Ao ser atingido, reseta a posição.
*   **Resolução HD**: O jogo roda em uma tela ampla de **1200x800**.
*   **Menu Interativo**: Com opções de iniciar, controlar som e sair.

## 📂 Estrutura de Pastas (Importante)

Para o funcionamento correto do PgZero, a estrutura de diretórios segue o padrão em inglês:

```
Kodland/
│
├── main.py                 # Arquivo principal (Ponto de entrada)
├── images/                 # Contém todos os sprites (Ambiente, Personagens, UI)
├── music/                  # Contém a trilha sonora (musica_fundo.mp3)
│
└── jogo/                   # Código fonte modular
    ├── constantes.py       # Configurações (Tela, Cores, Física)
    ├── personagens.py      # Lógica do Player (Física, Pulo Duplo, Animação)
    ├── inimigos.py         # Classes dos Inimigos (Patrulha e Voo)
    ├── fases.py            # Construção do Nível (Plataformas, Moedas)
    └── menu.py             # Interface do Menu Principal
```

## 🕹️ Como Jogar

1.  Execute o arquivo `main.py`.
2.  No menu, clique em **INICIAR**.
3.  **Controles**:
    *   ⬅️ **Seta Esquerda**: Mover para trás.
    *   ➡️ **Seta Direita**: Mover para frente.
    *   ⬆️ **Seta Cima**: Pular (Pressione novamente no ar para **Pulo Duplo**).
4.  **Objetivo**: Colete todas as moedas de bronze para vencer!
5.  **Cuidado**: Evite tocar nos inimigos (Espinho e Asas).

## 🛠️ Requisitos Técnicos

O projeto foi desenvolvido respeitando restrições estritas:
*   **Bibliotecas Permitidas**: `pgzero`, `math`, `random`.
*   **Sem Pygame Direto**: O código não faz importações diretas da biblioteca `pygame` para lógica de jogo, utilizando apenas os wrappers do PgZero (`Actor`, `Rect`, `music`, `keyboard`).

## 📝 Detalhes dos Módulos

*   **`main.py`**: Gerencia o loop principal, estados do jogo (Menu, Jogo, Vitória, Game Over) e eventos de entrada.
*   **`personagens.py`**: Implementa a física de gravidade, colisão com plataformas e o sistema de pulo duplo.
*   **`inimigos.py`**: Define o comportamento dos inimigos. O *Espinho* anda e espera, o *Asas* voa em oscilação.
*   **`fases.py`**: Gera o layout do nível, posicionando o chão, plataformas flutuantes, moedas e inimigos.
