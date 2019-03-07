    import pygame
"""import nemesis.py;"""

pygame.init();
screen = pygame.display.set_mode((400,300));
pygame.display.set_caption("menu");
menuAtivo = True;

start_button = pygame.draw.rect(screen,(0,0,240),(150,90,100,50));
continue_button = pygame.draw.rect(screen,(0,244,0),(150,160,100,50));
quit_button = pygame.draw.rect(screen,(244,0,0),(150,230,100,50));


pygame.display.flip();


while menuAtivo:
    for evento in pygame.event.get():
        print(evento);
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos() >= (150,230):
                if pygame.mouse.get_pos() <= (250,280):
                        pygame.quit();
