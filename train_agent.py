import random
import pygame
import numpy as np
import gymnasium as gym
from gymnasium import spaces
import imageio
from IPython.display import Image
import os
from stable_baselines3 import DQN
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.env_util import BaseCallback

from enviroment import Game2048

class RewardLoggerCallback(BaseCallback):
    def __init__(self):
        super(RewardLoggerCallback, self).__init__()
        self.rewards = []

    def _on_step(self) -> bool:
        # Record the reward of the current step
        self.rewards.append(self.locals["rewards"])
        return True


# Register the environment
gym.envs.registration.register(
    id='2048Env-v0',
    entry_point='__main__:Game2048',
)


# Create the environment
env = make_vec_env(lambda: Game2048(), n_envs=1)

model = DQN("MlpPolicy", env, verbose=1)

# Указываем количество временных шагов для обучения
timesteps = 800000  # Примерное количество шагов (можно изменить)

# Создаем callback для логирования
reward_callback = RewardLoggerCallback()

# Обучаем модель
model.learn(total_timesteps=timesteps, callback=reward_callback)

# Сохраняем модель
model_path = "dqn_2048_model"
model.save(model_path)

print(f"Model saved to {model_path}")

# Test and create GIF

for _ in range(500):
        action, _ = model.predict(obs, deterministic=True)  # Assuming `model` is defined elsewhere
        obs, reward, done, truncated, info = env.step(action)

        # Render the current state to a Pygame surface and capture it
        screen = env.render()
        frame = pygame.surfarray.array3d(screen)
        frame = frame.swapaxes(0, 1)  # Swap axes for correct frame orientation
        frames.append(frame)

        if done:
            break

    # Save the frames as a GIF
gif_path = "game.gif"
imageio.mimsave(gif_path, frames, fps=10)

    # Output the GIF in Colab
Image(filename=gif_path)