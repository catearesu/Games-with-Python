import pygame
from sys import exit



pygame.init() # abre un comando en formato javascript/como queremos que sea la pantalla
screen = pygame.display.set_mode((800,400))

# crear la ventana original
# definir una imagen de icono y una descripción
programIcon = pygame.image.load("skylines/shield.png")
pygame.display.set_icon(programIcon)
pygame.display.set_caption("Minger")


# generar superficies
#test_surface = pygame.Surface((100,200)) # he creado un rectangulo
#test_surface.fill("Red")
sky_surface = pygame.image.load("skylines/basic.jpg").convert() # para que coja el tamaño que yo quiero/ solo me queda con la propria imagen
sky_surface = pygame.transform.scale(sky_surface, (800,300)) # toda la x y 3/4 partes de la y

ground_surface = pygame.image.load("skylines/ground.png").convert() # para que coja el tamaño que yo quiero/ solo me queda con la propria imagen
ground_surface = pygame.transform.scale(ground_surface, (800,100)) # toda la x y 3/4 partes de la y

# para que en el juego se vea el nombre del juego
# TEXT
test_font = pygame.font.Font(None, 50)
text_surface = test_font.render("MINGER GOT GAME", False, "Pink")
go_font=pygame.font.Font(None, 30)
# Game Over text
text_gameover=go_font.render("GAME OVER MINGER!", False, "Black")
text_continue=go_font.render("Press 'Space' to continue fightin caracooler or 'Q' to quit", False, "Black")

# CARACOOLER, the snail
snail_surface = pygame.image.load("skylines/snail1.png").convert_alpha() # convertir de fondo blanco/negro a nada
# definir posición inicial del caracol
snail_x_pos = 800
snail_rect = snail_surface.get_rect(bottomright = (700,310))

#Minger, el vikingo
player_surf=pygame.image.load("skylines/static_viking.png").convert()
player_surf = pygame.transform.scale(player_surf, (80,100)) # cambiar el tamaño/escala
# quitar todo lo que sea blanco
color = pygame.Color(255, 255, 255) # he definido blanco como el color de fondo para que no aparezca el blanco de la imagen
player_surf.set_colorkey(color)

player_rect = player_surf.get_rect(midbottom= (100, 320)) # el rectangulo empieza en el 100, 320

## More than 1 png for jumping
viking_jumping=pygame.image.load("skylines/jumping_viking.png").convert()
viking_jumping=pygame.transform.scale(viking_jumping, (80, 100))
viking_jumping.set_colorkey(color)

viking_falling=pygame.image.load("skylines/falling_viking.png").convert()
viking_falling=pygame.transform.scale(viking_falling, (80, 100))
viking_falling.set_colorkey(color)

# setear el frame rate //los eventos pasan a una velocidad concreta
clock = pygame.time.Clock() # cada cuanto cada iteracción se vaya generando
# snail count
count = 0
# jumping
gravity = 0
game_active = True
position = 0
# SPEED INCREASE
velocity=4

while True:
    #Draw all our elements
    # Update everything
    snailcount=go_font.render(f"Snail Count: {count}", False, "Black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active == True:
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE and player_rect.bottom==320:
                    #print("jump")
                    gravity=-12
        else: 
            if event.type==pygame.KEYDOWN:
                if event.key== pygame.K_SPACE:
                    game_active=True
                    snail_rect.left=800
                elif event.key==pygame.K_q:
                    exit()
            
    if game_active:
        screen.blit(sky_surface, (0,0)) # de izquierda a derecha, de arriba a abajo
        screen.blit(ground_surface, (0,300))
        screen.blit(text_surface, (370, 350))
        screen.blit(snailcount, (550, 310))
        # demo of first screen surface     

        # SNAIL
        snail_x_pos-=5 # se desplaza de derecha a izquierda
        # screen.blit(snail_surface, (snail_x_pos, 270))
        #if snail_x_pos<=-100:
        #    snail_x_pos=900
        screen.blit(snail_surface, snail_rect)
        snail_rect.x -= velocity # se desplaza de derecha a izquierda
        # screen.blit(player_surf, (100, 215))
        if snail_rect.right<=0: # cuando se queda en la misma posición
            snail_rect.left=800
            count+=1
            if (count)%3==0: 
                velocity+=1
        
        #VIKING
        # screen.blit(player_surf, (100, 200))
        # screen.blit(player_surf, player_rect)
        player_rect.y += gravity
        if player_rect.bottom >= 320:
            player_rect.bottom = 320

        if position==player_rect.y:
            screen.blit(player_surf, player_rect)
        elif position<=player_rect.y:
            screen.blit(viking_falling, player_rect)
        else: 
            screen.blit(viking_jumping, player_rect)
        
        #print(player_rect.y)
        #Gravity style
        gravity += 0.4 # inicialmente la posición es 0, si saltas es -12 
        position = player_rect.y

        ## COLLISION BETWEEN RECTANGLES
        # print(player_rect.colliderect(snail_rect))

        #Playing with the MOUSE: 

        #if event.type==pygame.MOUSEMOTION: 
        #    print(event.pos)
        #if event.type==pygame.MOUSEBUTTONDOWN: #MOUSEBUTTONUP 
        #    print(mouse down)  #mouse up
        
        ## GAME OVER: 
        if snail_rect.colliderect(player_rect):
            game_active=False
            screen.blit(text_gameover, (250, 200))
            screen.blit(text_continue, (210, 230))
            count=0
            velocity=4

    pygame.display.update()
    clock.tick(60)
    


