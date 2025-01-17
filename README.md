Russian


2048 Game with Reinforcement Learning Agent (DQN)
Описание
Это реализация популярной игры 2048 на Python с использованием библиотеки Pygame. Игра поддерживает ручное управление, а также интеграцию с обучением RL-агента (DQN). RL-агент можно использовать для автоматической игры и тренировки, чтобы достигать лучших результатов.

Особенности
Классическая механика игры 2048.
Система подсчёта очков.
Приятный интерфейс с закруглёнными плитками и адаптивными цветами.
Интеграция с библиотеками Gymnasium и Stable-Baselines3 для обучения RL-агента.
Как запустить игру
Скопируйте этот репозиторий:
2048 Game with Reinforcement Learning Agent (DQN)
Описание
Это реализация популярной игры 2048 на Python с использованием библиотеки Pygame. Игра поддерживает ручное управление, а также интеграцию с обучением RL-агента (DQN). RL-агент можно использовать для автоматической игры и тренировки, чтобы достигать лучших результатов.

Особенности
Классическая механика игры 2048.
Система подсчёта очков.
Приятный интерфейс с закруглёнными плитками и адаптивными цветами.
Интеграция с библиотеками Gymnasium и Stable-Baselines3 для обучения RL-агента.
Как запустить игру

Скопируйте этот репозиторий:

git clone https://github.com/your-repo/2048-game.git
cd 2048-game

Убедитесь, что установлены необходимые зависимости: pip install pygame


Запустите игру: python game.py



Управление
Стрелка влево: движение влево.
Стрелка вправо: движение вправо.
Стрелка вверх: движение вверх.
Стрелка вниз: движение вниз.
Инструкции для обучения RL-агента
Этот проект поддерживает обучение RL-агента с использованием DQN.

Установка зависимостей
Убедитесь, что у вас установлены библиотеки:

Gymnasium
Stable-Baselines3
PyTorch
Установить их можно следующей командой:


pip install gymnasium stable-baselines3 torch

Запуск обучения

Скопируйте репозиторий.

Запустите файл: train_agent.py:

python train_agent.py
Этот скрипт использует Stable-Baselines3 для обучения агента.
Структура проекта
yaml

2048-game/
│
├── game.py             # Реализация игры 2048
├── train_agent.py      # Тренировка RL-агента (DQN)
├── utils.py            # Утилиты для взаимодействия игры с Gymnasium
└── README.md           # Описание проекта
Состояние игры, действия и вознаграждение

Состояние

Состояние представляет собой текущее состояние игрового поля размером 4x4.

Действия

Доступные действия:

0: Вверх
1: Вправо
2: Вниз
3: Влево
Вознаграждение

Вознаграждение основывается на количестве очков, полученных за слияние плиток в текущем ходе.

Вклад
Проект создан в TUMO с использованием:
Pygame — для визуализации игры.
Gymnasium — для создания среды RL.
Stable-Baselines3 — для обучения агента.
Если у вас есть предложения или улучшения, не стесняйтесь вносить их через Pull Request!


English

2048 Game with Reinforcement Learning Agent (DQN)
Description
This is a Python implementation of the popular 2048 game using Pygame. The game supports manual play and is integrated with a Reinforcement Learning (RL) agent (DQN) for automatic gameplay and training to achieve higher scores.

How to Run the Game
Clone this repository:

git clone https://github.com/your-repo/2048-game.git
cd 2048-game

Install the required dependencies:

pip install pygame

Run the game:

python game.py

Controls

Left Arrow: Move left.
Right Arrow: Move right.
Up Arrow: Move up.
Down Arrow: Move down.
Instructions for Training the RL Agent
This project supports training an RL agent using DQN.

Install Dependencies
Ensure you have the following libraries installed:

Gymnasium
Stable-Baselines3
PyTorch
Install them using:

pip install gymnasium stable-baselines3 torch
Start Training

Clone the repository.

Run the train_agent.py script:

python train_agent.py

This script uses Stable-Baselines3 to train the agent.
Project Structure

2048-game/
│
├── game.py             # 2048 game implementation
├── train_agent.py      # RL agent (DQN) training
├── utils.py            # Utilities for Gymnasium environment integration
└── README.md           # Project description

Game State, Actions, and Rewards

State
The state is represented by the current 4x4 game grid.

Actions
Available Actions:

0: Up
1: Right
2: Down
3: Left
Reward

Rewards are based on the points gained for merging tiles during each move.
Contributions
This project was developed at TUMO using:

Pygame for game visualization.
Gymnasium to create the RL environment.
Stable-Baselines3 for agent training.
Feel free to contribute via Pull Requests if you have ideas or improvements!


Armenian

RL Գործակալին Ուսուցանելու Հրահանգներ
Այս նախագիծը աջակցում է RL գործակալի ուսուցմանը՝ DQN մեթոդով։

Տեղադրեք Կախվածությունները
Համոզվեք, որ տեղադրված են հետևյալ գրադարանները՝

Gymnasium
Stable-Baselines3
PyTorch
Տեղադրեք դրանք հետևյալ հրամանով՝


pip install gymnasium stable-baselines3 torch
Ուսուցման Սկիզբ

Կլոնավորեք պահոցը։

Գործարկեք train_agent.py ֆայլը՝

python train_agent.py

Այս սցենարը օգտագործում է Stable-Baselines3 գործակալին ուսուցանելու համար։
Նախագծի Կառուցվածքը

2048-game/
│
├── game.py             # 2048 խաղի իրականացում
├── train_agent.py      # RL գործակալի ուսուցում (DQN)
├── utils.py            # Gymnasium միջավայրի ինտեգրման համար
└── README.md           # Նախագծի նկարագրություն

Խաղի Վիճակ, Գործողություններ և Մրցանակներ

Վիճակ
Վիճակը ներկայացված է ընթացիկ 4x4 խաղային վանդակը։

Գործողություններ
Հասանելի Գործողություններ՝
0: Վերև
1: Աջ
2: Ներքև
3: Ձախ

Մրցանակ
Մրցանակները հիմնված են սալիկների միաձուլման ժամանակ ստացված միավորների վրա։
Ներդրումներ

Այս նախագիծը մշակվել է TUMO-ում՝ օգտագործելով՝
Pygame՝ խաղի վիզուալիզացիայի համար։
Gymnasium՝ RL միջավայրի ստեղծման համար։
Stable-Baselines3՝ գործակալի ուսուցման համար։
Եթե ունեք առաջարկներ կամ բարելավումներ, կարող եք ներմուծել Pull Request-ների միջոցով։

