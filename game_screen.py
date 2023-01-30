import pygame
from config import FPS, WIDTH, HEIGHT, BLACK
from assets import carrega_arquivos
from sprites import Caixa


def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()



    DONE = 0
    PLAYING = 1
    state = PLAYING
    last_update = pygame.time.get_ticks()

    dicionario_de_arquivos = carrega_arquivos()

    lista_caixas = pygame.sprite.Group()

    caixa= Caixa(dicionario_de_arquivos)
    lista_caixas.add(caixa)

    font = pygame.font.SysFont(None, 48)
    text = font.render(caixa.palavra  ,True,(0, 0, 0))
    palavra=""
    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)
        segundos = int(pygame.time.get_ticks() - last_update)
        #print(segundos)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            if event.type == pygame.KEYDOWN:
                palavra+=event.unicode
         
        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor branca
        lista_caixas.draw(window)
        window.blit(text, (caixa.rect.x+100, caixa.rect.y+4))

        #palavra
        font = pygame.font.SysFont(None, 48)
        text2 = font.render(palavra  ,True,(0, 0, 0))
        window.blit(text2, (caixa.rect.x+70, caixa.rect.y+35))
        
        lista_caixas.update()

        pygame.display.update()  # Mostra o novo frame para o jogador

    return state
