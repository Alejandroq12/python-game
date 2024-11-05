import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for player_element in updatable:
            player_element.update(dt)

            screen.fill("black")

        for player_element in drawable:
            player_element.draw(screen)   
        

            pygame.display.flip()
            
            # limit the framerate to 60 fps
            dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

