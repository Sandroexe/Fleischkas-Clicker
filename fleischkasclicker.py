print("Starte Fleischkas-Clicker...")

import pygame

print("Starte Pygame...")
pygame.init()

pygame.display.set_caption("Fleischkas-Clicker")
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

# Platzhalter für Button (Kreis)
button_rect = pygame.Rect(350, 250, 100, 100)

score = 0
font = pygame.font.SysFont(None, 48)

is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                score += 1

    window_surface.blit(background, (0, 0))
    # Button zeichnen (Platzhalter)
    pygame.draw.ellipse(window_surface, (200, 100, 50), button_rect)
    # Score anzeigen
    score_surf = font.render(f"Punkte: {score}", True, (255, 255, 255))
    window_surface.blit(score_surf, (20, 20))

    pygame.display.update()
