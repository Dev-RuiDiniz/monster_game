monster_game/
├── venv/                 # Ambiente virtual (ignorada pelo Git)
├── assets/               # Recursos: Imagens, sons, fontes.
│   ├── images/           # Sprites e planos de fundo
│   ├── audio/            # Efeitos sonoros e músicas
│   └── fonts/            # Arquivos de fontes
├── src/                  # Código Fonte Principal (Onde a mágica acontece)
│   ├── __init__.py       # Pacote Python
│   ├── main.py           # Ponto de entrada do jogo, loop principal
│   ├── settings.py       # Constantes globais (dimensões, cores, FPS)
│   ├── entities/         # Classes POO: Pokemon, Trainer, Npc, Item
│   │   ├── __init__.py
│   │   ├── pokemon.py
│   │   └── trainer.py
│   ├── scenes/           # Classes para gerenciar estados do jogo (Menu, Batalha, Mapa)
│   │   ├── __init__.py
│   │   ├── menu.py
│   │   └── battle.py
│   └── utils/            # Funções utilitárias (carregar assets, cálculos)
├── data/                 # Dados do jogo (saves, JSONs de configurações de pokémon base)
├── requirements.txt      # Lista de dependências (Pygame)
├── .gitignore            # Arquivo para controle de versão
├── README.md
└── estrutura.md