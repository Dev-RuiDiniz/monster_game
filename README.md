# 🐉 Pykémon - Um RPG de Monstro com Pygame e POO

Bem-vindo ao repositório do projeto **Pykémon**, um jogo de RPG de aventura e batalha de monstros desenvolvido em Python, utilizando a biblioteca Pygame. O foco principal deste projeto é aplicar sólidos princípios de Programação Orientada a Objetos (POO), Clean Code e modularidade.

---

## 🎯 Objetivo do Projeto

Desenvolver um sistema de jogo escalável que inclui:

* Sistema de Batalha por Turnos (Combate)
* Sistema de Mapa e Exploração (Movimentação e Colisão)
* Gerenciamento de Entidades (Pokémons, Treinadores, Itens)
* Gerenciamento de Estado de Jogo (Cenas: Menu, Mapa, Batalha)

## ⚙️ Configuração e Execução

Para rodar o projeto localmente, siga os passos abaixo.

### Pré-requisitos

* Python 3.8+
* Git

### 1. Clonar o Repositório

```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd monster_game
```

2. Configurar o Ambiente Virtual

É altamente recomendável utilizar um ambiente virtual (venv) para isolar as dependências do sistema.

```
# Cria e ativa o ambiente virtual
python -m venv venv
source venv/bin/activate  # macOS/Linux
# .\venv\Scripts\Activate.ps1 # Windows PowerShell
```

3. Instalar Dependências
Com o ambiente virtual ativado, instale o Pygame usando o arquivo requirements.txt:

```
pip install -r requirements.txt
```
4. Executar o Jogo
Para iniciar o Game Loop e abrir a janela do Pygame:

```
python src/main.py
```

## 📂 Estrutura do Projeto
O projeto segue uma arquitetura modular baseada em separação de preocupações:

monster_game/
├── assets/          # Recursos (Imagens, Áudio, Fontes)
├── src/             # Código Fonte do Jogo
│   ├── main.py      # Game Loop e Inicialização
│   ├── settings.py  # Constantes Globais
│   ├── entities/    # Classes POO (Pokemon, Trainer)
│   ├── scenes/      # Classes de Gerenciamento de Estado (Batalha, Menu)
│   └── utils/       # Funções Utilitárias
└── data/            # Dados (Saves e Configurações JSON)

## 🤝 Contribuições
Este projeto está em desenvolvimento inicial. Contribuições, sugestões de melhoria (especialmente em POO e otimização de Pygame) são bem-vindas!