from enviroment import Game2048, HEIGHT, WIDTH
import pygame
# Тестирование игры
from PIL import Image, ImageSequence
import sys

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
BLACK = (0,0,0)
WHITE = (255,255,255)
FONT_SIZE = 36

def play_gif(screen, gif_path):
    """Play a GIF file on the Pygame screen."""
    # Load GIF using Pillow
    gif = Image.open(gif_path)
    frames = [frame.copy() for frame in ImageSequence.Iterator(gif)]

    clock = pygame.time.Clock()

    for frame in frames:
        # Convert the frame to a surface
        mode = frame.mode
        size = frame.size
        data = frame.tobytes()
        frame_surface = pygame.image.fromstring(data, size, mode)
        
        # Display the frame
        screen.fill((0, 0, 0))
        screen.blit(frame_surface, ((WIDTH - size[0]) // 2, (HEIGHT - size[1]) // 2))
        pygame.display.flip()

        # Wait for the next frame
        clock.tick(2)  # Adjust this to control playback speed (2 FPS in this case)

    # Wait briefly after playing the GIF
    pygame.time.wait(1000)

def starting_screen(screen, font):
    """Display the starting screen with options to start the game or view a video."""
    start_screen_active = True
    while start_screen_active:
        screen.fill(WHITE)
        # Draw title
        title_text = font.render("2048 Game", True, BLACK)
        title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        screen.blit(title_text, title_rect)

        # Draw buttons
        start_button = pygame.Rect(WIDTH // 4, HEIGHT // 2, 50, 50)
        video_button = pygame.Rect(WIDTH // 4, HEIGHT // 2 + 50, 50, 50)

        pygame.draw.rect(screen, (187, 173, 160), start_button)
        pygame.draw.rect(screen, (187, 173, 160), video_button)

        start_text = font.render("Start Game", True, BLACK)
        video_text = font.render("Watch Video", True, BLACK)
        
        screen.blit(start_text, start_text.get_rect(center=start_button.center))
        screen.blit(video_text, video_text.get_rect(center=video_button.center))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    start_screen_active = False  # Start the game
                elif video_button.collidepoint(event.pos):
                    play_gif(screen, "game1.gif")



if __name__ == "__main__":
    env = Game2048()
    done = False
    env.reset()

# Show the starting screen
    screen = env.screen
    font = env.font
    starting_screen(screen, font)


    # Game loop
    while not done:
        env.render()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    action = 0
                    obs, reward, done, truncated, info = env.step(action)    
                elif event.key == pygame.K_RIGHT:
                    action = 1
                    obs, reward, done, truncated, info = env.step(action)    
                elif event.key == pygame.K_UP:
                    action = 3           
                    obs, reward, done, truncated, info = env.step(action)         
                elif event.key == pygame.K_DOWN:
                    action = 2
                    obs, reward, done, truncated, info = env.step(action)    


    print("Game Over!")

    pygame.quit()
