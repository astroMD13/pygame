print('A carregar codigo',end='\r')
import pygame
import time
import random


pygame.font.init()
WIDTH,HEIGHT=1000, 650

win=pygame.display.set_mode((WIDTH, HEIGHT))

#cria o nome da janela
pygame.display.set_caption('Space Dodge')

#carrega uma imagem
BG=pygame.transform.scale(pygame.image.load('ChatGPT Image 8_10_2026, 09_27_38.png'), (WIDTH, HEIGHT))

player_widh=40
player_height=60
player_vel=10
clock=pygame.time.Clock()
start=time.time()
elapsed=0
star_widht=10
star_height=20
star_vel=3
#tipo de fonte  tamanho da fonte
FONT=pygame.font.SysFont('comicsans',30)


#desenha coisas no fundo
#usas argumentos para poder usar dentro da funçao variaveis
def draw(player,elapsed, stars, player_hitbox):
    win.blit(BG, (0,0))
    text_time=FONT.render(f'Tempo: {round(elapsed)}s',1,'white')
    #texto  cordenadas
    win.blit(text_time,(10,10))
    #onde desenhar  cor  que rectangulo
    win.blit(player,player_hitbox)
    for star in stars:
        pygame.draw.rect(win,'white',star)

    pygame.display.update()

def main():
    run=True
    #cria um retangulo 
    #cordenada x   cordenada y   largura do retangulo   altura do retangulo
    player=pygame.transform.scale(pygame.image.load('5811839.png'),(player_widh, player_height))
    player_hitbox=pygame.Rect(500,HEIGHT-player_height, player_widh,player_height)
    star_add_increment=2000
    star_count=0
    stars=[]
    hit=False

    while run:
        #devolve o nº de milisegundos desde o ultimo tick
        star_count+=clock.tick(30)

        elapsed=time.time()-start
        if star_count>star_add_increment:
            for _ in range(3):
                star_x=random.randint(0, WIDTH-star_widht)
                #para nao aparecer no ecra
                star=pygame.Rect(star_x,-star_height,star_widht,star_height)
                stars.append(star)
                # max é para manter sempre no mesmo valor, aqui é 200
            star_add_increment=max(200, star_add_increment-50) 
            star_count=0   
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                break
        keys=pygame.key.get_pressed()   
        if keys[pygame.K_a] and player_hitbox.x-player_vel>=0:
            player_hitbox.x-=player_vel
        if keys[pygame.K_d] and player_hitbox.x + player_vel+player_widh<=WIDTH:
            player_hitbox.x+=player_vel
            # [:] <- isto copia a lista para nao dar erro e demois altera a lista de um vez
        for star in stars[:]:
            star.y+=star_vel
            if star.y>HEIGHT:
                # da lista remove algo
                stars.remove(star)
            elif star.y+ star.height >= player_hitbox.y and star.colliderect(player_hitbox):
                stars.remove(star)
                hit=True
                break
        if hit:
            lost_text=FONT.render('Perdeste!',1,'red') 
            #texto que escreve    cordenadas
            win.blit(lost_text,(WIDTH/2-lost_text.get_width()/2,HEIGHT/2-lost_text.get_height()/2))   
            pygame.display.update()
            #isto sao 4 segundos
            pygame.time.delay(4000)
            break
        draw(player, elapsed, stars,player_hitbox)    
    pygame.quit()

if __name__=='__main__':
    main()