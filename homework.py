import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Wildlife Information Display")

background_image = pygame.transform.scale(
    pygame.image.load("pexels-pixabay-46254.jpg").convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

wildlife_image = pygame.transform.scale(
    pygame.image.load("lion.jpg").convert_alpha(),
    (200, 200)
)

wildlife_rect = wildlife_image.get_rect(center=(SCREEN_WIDTH // 2, 220))

text = pygame.font.Font(None, 36).render(
    "Lions live in groups called prides.",
    True,
    pygame.Color("white")
)

text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 420))

def game_loop():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.blit(background_image, (0, 0))
        display_surface.blit(wildlife_image, wildlife_rect)
        display_surface.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    game_loop()