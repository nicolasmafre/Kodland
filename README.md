# Jogo de 2 Fases com Pygame Zero

Este é um projeto de um jogo simples desenvolvido em Python utilizando a biblioteca **Pygame Zero**. O jogo consiste em duas fases distintas: coleta de itens e sobrevivência.

## 📂 Estrutura de Pastas e Arquivos

A estrutura do projeto está organizada da seguinte forma:

```
Kodland/
│
├── main.py                 # Arquivo principal para iniciar o jogo
├── README.md               # Documentação do projeto
│
├── jogo/                   # Pacote contendo a lógica do jogo
│   ├── constantes.py       # Configurações e constantes globais
│   ├── personagens.py      # Classe do Jogador (Player)
│   ├── inimigos.py         # Gerenciamento dos Inimigos (EnemyManager)
│   ├── fases.py            # Lógica da Fase 1 (Level1)
│   └── menu.py             # Interface e lógica do Menu Principal
│
└── musica/                 # Pasta para arquivos de áudio
    └── musica_fundo.mp3    # Arquivo de música de fundo
```

## 📚 Bibliotecas Utilizadas

O projeto utiliza apenas bibliotecas padrão do Python e o framework Pygame Zero:

*   **pgzero**: Biblioteca principal para criação de jogos.
*   **math**: Utilizada para cálculos matemáticos.
*   **random**: Utilizada para gerar posições aleatórias.
*   **pygame**: Utilizada internamente para carregar música de uma pasta personalizada ("musica").

## 📝 Descrição dos Arquivos

### `main.py`
É o ponto de entrada do jogo. Gerencia o loop principal (`update` e `draw`), a máquina de estados e a entrada do usuário. Também gerencia a reprodução da música de fundo a partir da pasta `musica`.

### `jogo/constantes.py`
Contém variáveis globais que definem as configurações do jogo.

### `jogo/personagens.py`
Define a classe `Player`. Responsável por desenhar e mover o jogador.

### `jogo/inimigos.py`
Define a classe `EnemyManager`. Gerencia a criação e atualização dos inimigos da Fase 2.

### `jogo/fases.py`
Define a classe `Level1`. Gerencia a lógica da primeira fase (coleta de moedas).

### `jogo/menu.py`
Define a classe `Menu`. Responsável por desenhar a interface inicial.

## 🎮 Funcionalidade do Jogo

1.  **Menu Principal**: Iniciar, Som (On/Off), Sair.
2.  **Fase 1**: Colete 5 moedas amarelas.
3.  **Fase 2**: Sobreviva por 10 segundos fugindo dos inimigos vermelhos.
4.  **Fim de Jogo**: Telas de Vitória ou Game Over.

## 🎵 Som

O jogo busca o arquivo `musica_fundo.mp3` dentro da pasta `musica`.
