import random
import pygame
import numpy as np
import gymnasium as gym
from gymnasium import spaces

# Размеры окна игры
WIDTH, HEIGHT = 480, 800
GRID_SIZE = 4
TILE_SIZE = WIDTH // GRID_SIZE
FONT_SIZE = 40

# Цвета
BACKGROUND_COLOR = (255, 255, 255)
GAME_AREA_COLOR = (255, 243, 204)
TILE_COLORS = {
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}
TEXT_COLOR = (119, 110, 101)
SCORE_COLOR = (0, 0, 0)

# Инициализация Pygame
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")
clock = pygame.time.Clock()

# Шрифты
try:
    FONT = pygame.font.SysFont("arial", FONT_SIZE)
except pygame.error:
    FONT = pygame.font.Font(None, FONT_SIZE)


class Game2048(gym.Env):
    def __init__(self):
        super(Game2048, self).__init__()
        self.state = None
        self.reward = 0
        self.action_space = spaces.Discrete(4)  # 4 действия: влево, вправо, вверх, вниз
        self.observation_space = spaces.Box(
            low=0, high=2048, shape=(GRID_SIZE * GRID_SIZE,), dtype=np.int32
        )

        # Pygame setup
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("2048")
        self.clock = pygame.time.Clock()

    def reset(self, seed=None, options=None, return_info=False):
        super().reset(seed=seed)
        self.state = self.initialize_state()
        self.reward = 0
        obs = np.array(self.state).flatten()
        if return_info:
            return obs, {}
        return obs, {}

    def step(self, action):
        old_state = [row[:] for row in self.state]

        # Выполняем действие
        if action == 0:  # Влево
            self.move_left()
        elif action == 1:  # Вправо
            self.move_right()
        elif action == 2:  # Вверх
            self.move_up()
        elif action == 3:  # Вниз
            self.move_down()

        # Проверяем, изменилась ли сетка
        done = self.is_game_over()
        reward = self.reward if old_state != self.state else 0

        # Добавляем новую плитку, если игра не окончена
        if not done:
            self.add_new_tile()

        # Возвращаем новое состояние
        return np.array(self.state).flatten(), reward, done, False, {}

    def render(self, mode="human"):
        self.screen.fill(BACKGROUND_COLOR)
        self.draw_board()
        self.draw_score()
        pygame.display.flip()
        self.clock.tick(60)

        # Return the surface for capturing
        return self.screen  # Return the Pygame surface

    def draw_board(self):
        game_area_x = (WIDTH - TILE_SIZE * GRID_SIZE) // 2
        game_area_y = (HEIGHT - TILE_SIZE * GRID_SIZE) // 2
        pygame.draw.rect(
            self.screen, GAME_AREA_COLOR,
            (game_area_x, game_area_y, TILE_SIZE * GRID_SIZE, TILE_SIZE * GRID_SIZE), border_radius=15
        )

        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                self.draw_tile(r, c, game_area_x, game_area_y)

    def draw_tile(self, r, c, game_area_x, game_area_y):
        value = self.state[r][c]
        tile_color = TILE_COLORS.get(value, (60, 58, 50))
        pygame.draw.rect(
            self.screen,
            tile_color,
            (game_area_x + c * TILE_SIZE + 10, game_area_y + r * TILE_SIZE + 10, TILE_SIZE - 20, TILE_SIZE - 20),
            border_radius=10
        )
        if value != 0:
            text = FONT.render(str(value), True, TEXT_COLOR)
            text_rect = text.get_rect(
                center=(game_area_x + c * TILE_SIZE + TILE_SIZE // 2, game_area_y + r * TILE_SIZE + TILE_SIZE // 2)
            )
            self.screen.blit(text, text_rect)

    def draw_score(self):
        score_text = FONT.render(f"Score: {self.reward}", True, SCORE_COLOR)
        self.screen.blit(score_text, (20, 20))

    def initialize_state(self):
        board = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
        self.add_new_tile(board)
        self.add_new_tile(board)
        return board

    def add_new_tile(self, board=None):
        if board is None:
            board = self.state
        empty_tiles = [(r, c) for r in range(GRID_SIZE) for c in range(GRID_SIZE) if board[r][c] == 0]
        if empty_tiles:
            r, c = random.choice(empty_tiles)
            board[r][c] = random.choice([2, 4])

    def move_left(self):
        self.compress()
        self.merge()
        self.compress()

    def move_right(self):
        self.state = [row[::-1] for row in self.state]
        self.move_left()
        self.state = [row[::-1] for row in self.state]

    def move_up(self):
        self.state = self.rotate_board()
        self.move_left()
        self.state = self.rotate_board(inverse=True)

    def move_down(self):
        self.state = self.rotate_board(inverse=True)
        self.move_left()
        self.state = self.rotate_board()

    def rotate_board(self, inverse=False):
        if not inverse:
            return [[self.state[GRID_SIZE - 1 - c][r] for c in range(GRID_SIZE)] for r in range(GRID_SIZE)]
        else:
            return [[self.state[c][GRID_SIZE - 1 - r] for c in range(GRID_SIZE)] for r in range(GRID_SIZE)]

    def compress(self):
        for r in range(GRID_SIZE):
            new_row = [tile for tile in self.state[r] if tile != 0]
            new_row += [0] * (GRID_SIZE - len(new_row))
            self.state[r] = new_row

    def merge(self):
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE - 1):
                if self.state[r][c] == self.state[r][c + 1] and self.state[r][c] != 0:
                    self.state[r][c] *= 2
                    self.state[r][c + 1] = 0
                    self.reward += self.state[r][c]

    def is_game_over(self):
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                if self.state[r][c] == 0:
                    return False
                if r < GRID_SIZE - 1 and self.state[r][c] == self.state[r + 1][c]:
                    return False
                if c < GRID_SIZE - 1 and self.state[r][c] == self.state[r][c + 1]:
                    return False
        return True

