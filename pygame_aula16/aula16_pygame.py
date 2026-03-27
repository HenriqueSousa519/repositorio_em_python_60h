import pygame

pygame.init()
tela  =  pygame.display.set_mode((500,500))
run = True
while run:
    for event in pygame.event.get():
        if event.type  == pygame.QUIT:
            run = False
            
    tela.fill((83,20,205))
    pygame.draw.rect(tela, ('#ffffff'),(235,235,30,30)) 
    pygame.display.update()    
pygame.quit()