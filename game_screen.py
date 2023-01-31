import pygame
from config import FPS, WIDTH, HEIGHT, BLACK
from assets import carrega_arquivos
from sprites import Caixa
import random

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()


    WHITE = (255, 255, 255)
    DONE = 0
    PLAYING = 1
    state = PLAYING
    last_update = pygame.time.get_ticks()

    dicionario_de_arquivos = carrega_arquivos()

    lista_caixas = pygame.sprite.Group()

    caixa= Caixa(dicionario_de_arquivos)
    lista_caixas.add(caixa)

    #palavras que o jogador digita
    font = pygame.font.SysFont(None, 48)
    text = font.render(caixa.palavra  ,True,(0, 0, 0))

    
    palavra=""
    ponto=0
    listapalavra=['exceto', 'cinico',"banana","bala","batata","bateria","cacau","cadeado", "cadeira", "cafe" ,"cafune","domado","domino","doze","duvida","duzia", 'idoneo', 'ambito', 'nescio', 'exceto', 'cinico', 'idoneo', 'ambito','indole', 'jesus', 'vereda', 'apogeu']

    
    # ===== Loop principal =====
    while state != DONE:
        formatando_ponto= f'{ponto}'
        texto_formatado= font.render(formatando_ponto,True,WHITE)

        clock.tick(FPS)
        segundos=int(40-((pygame.time.get_ticks()-last_update)/1000))
        formatando_segundo= f'{segundos}'
        segundotela=font.render(formatando_segundo,True,WHITE)

        # ----- Trata eventos
        for event in pygame.event.get():
            
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            if event.type == pygame.KEYDOWN:
                palavra+=event.unicode
        if caixa.rect.y>700:
            if palavra== caixa.palavra:
                ponto+=1
            else:
                caixa.speedy+=2
            caixa.rect.x = random.randint(0,477)
            palavra=""
            caixa.rect.y =-76
            caixa.palavra= random.choice(listapalavra)
            #caixa.palavra= random.choice(caixa.listapalavra)
            text = font.render(caixa.palavra  ,True,(0, 0, 0))
        if segundos ==0:
            state=DONE
        if caixa.speedy==30:
            state=DONE

        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor branca
        lista_caixas.draw(window)
        window.blit(text, (caixa.rect.x+100, caixa.rect.y+4))

        #palavra que o jogador digita
        font = pygame.font.SysFont(None, 48)
        text2 = font.render(palavra,True,(0, 0, 0))
        window.blit(text2, (caixa.rect.x+70, caixa.rect.y+35))
        lista_caixas.update()
        #printa placar
        window.blit(texto_formatado,(30,10))
        #printa segundo
        window.blit(segundotela,(830,10))

        pygame.display.update()  # Mostra o novo frame para o jogador

    return state