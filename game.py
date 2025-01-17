from enviroment import Game2048
import pygame
# Тестирование игры
if __name__ == "__main__":
    env = Game2048()
    obs = env.reset()
    done = False
    while not done:
        action = env.action_space.sample()  # Случайное действие
        obs, reward, done, _, _ = env.step(action)
        env.render()
    print("Game Over!")
