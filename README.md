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
└── music/                  # (Opcional) Pasta para arquivos de áudio
    └── musica_fundo.mp3    # Arquivo de música de fundo (deve ser adicionado manualmente)
```

## 📚 Bibliotecas Utilizadas

O projeto utiliza apenas bibliotecas padrão do Python e o framework Pygame Zero:

*   **pgzero**: Biblioteca principal para criação de jogos, facilitando o uso do Pygame com uma API mais simples.
*   **math**: Utilizada para cálculos matemáticos, especificamente para calcular a distância entre o jogador e os inimigos (função `hypot`) para evitar que nasçam muito próximos.
*   **random**: Utilizada para gerar posições aleatórias para moedas e inimigos, além de definir velocidades variadas para os inimigos.

## 📝 Descrição dos Arquivos

### `main.py`
É o ponto de entrada do jogo. Gerencia o loop principal (`update` e `draw`), a máquina de estados (Menu, Fases, Game Over, Vitória) e a entrada do usuário (mouse e teclado). Também gerencia a reprodução da música de fundo.

### `jogo/constantes.py`
Contém variáveis globais que definem as configurações do jogo, como largura e altura da tela, cores, estados do jogo, velocidade do jogador, quantidade de inimigos e tempo de sobrevivência. Facilitando o balanceamento do jogo em um único lugar.

### `jogo/personagens.py`
Define a classe `Player`. Responsável por desenhar o jogador (um quadrado amarelo) e atualizar sua posição com base nas setas do teclado, garantindo que ele não saia dos limites da tela.

### `jogo/inimigos.py`
Define a classe `EnemyManager`. Gerencia a criação e atualização dos inimigos da Fase 2. Os inimigos (quadrados vermelhos) movem-se pela tela rebatendo nas paredes. A classe também verifica colisões com o jogador.

### `jogo/fases.py`
Define a classe `Level1`. Gerencia a lógica da primeira fase, onde o objetivo é coletar moedas. Controla a posição das moedas, a pontuação e verifica se o objetivo foi alcançado para avançar de fase.

### `jogo/menu.py`
Define a classe `Menu`. Responsável por desenhar a interface inicial com botões "Iniciar", "Som" (Ligado/Desligado) e "Sair". Trata os cliques do mouse para navegar entre as opções.

## 🎮 Funcionalidade do Jogo

1.  **Menu Principal**:
    *   O jogo inicia em um menu.
    *   **Iniciar**: Começa o jogo na Fase 1.
    *   **Som**: Liga ou desliga a música de fundo (requer arquivo na pasta `music`).
    *   **Sair**: Fecha a aplicação.

2.  **Fase 1 (Coleta)**:
    *   **Objetivo**: O jogador (quadrado amarelo) deve coletar 5 moedas (círculos dourados) espalhadas pela tela.
    *   **Controles**: Use as setas do teclado para mover.

3.  **Fase 2 (Sobrevivência)**:
    *   **Objetivo**: Após coletar as moedas, o jogador deve sobreviver por 10 segundos sem tocar nos inimigos.
    *   **Inimigos**: Quadrados vermelhos que se movem e rebatem nas paredes.
    *   **Derrota**: Se tocar em um inimigo, o jogo vai para a tela de "GAME OVER".
    *   **Vitória**: Se o tempo acabar e o jogador estiver vivo, vai para a tela de "VITÓRIA".

4.  **Telas Finais**:
    *   Tanto na vitória quanto na derrota, pressione **ESPAÇO** para voltar ao Menu Principal.

## 🎵 Como Adicionar Som

Para que a funcionalidade de som funcione corretamente:
1.  Crie uma pasta chamada `music` na raiz do projeto.
2.  Adicione um arquivo de áudio (MP3 ou OGG) chamado `musica_fundo.mp3` dentro dessa pasta.
