import pygame
import random

class Caixa(pygame.sprite.Sprite):
    def __init__(self, dicionario_de_arquivos):

        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # TODO 1: Defina as informações abaixo
        self.image = dicionario_de_arquivos['input'] # Carregue a imagem do input disponível em dicionario_de_arquivos
        self.image= pygame.transform.scale(self.image, (273,76))
        self.rect = self.image.get_rect()
        listapalavra=['exceto', 'cinico',"banana","bala","batata","bateria","cacau","cadeado", "cadeira", "cafe" ,"cafune","domado","domino","doze","duvida","duzia", 'idoneo', 'ambito', 'nescio', 'exceto', 'cinico', 'idoneo', 'ambito','indole', 'jesus', 'vereda', 'apogeu']
        self.palavra= random.choice(listapalavra)
        self.rect.x = random.randint(0,477)
        self.rect.y =-76
        self.speedy = 3

    def update(self):
        #Atualização da posição da nave
        self.rect.y+= self.speedy
        #Aqui você deve definir a lógica para fazer a caixa cair


class Botao(pygame.sprite.Sprite):
    def __init__(self, dicionario_de_arquivos, nome_do_jogo):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.dicionario_de_arquivos = dicionario_de_arquivos
        self.image = dicionario_de_arquivos['btn'] # assets é um dicionário de imagens, sons e fonts
        self.mask = pygame.mask.from_surface(self.image)
        #todo objeto precisa de um rect
        # rect é a representação de retangulo feita pelo pygame
        self.rect = self.image.get_rect()
        # é preciso definir onde a imagem deve aparecer no jogo
        self.rect.x = 0
        self.rect.y = 0

        self.nome_do_jogo = nome_do_jogo

    def mouse_over(self, over):
        # Toda a lógica de movimentação deve ser feita aqui
        # Atualização da posição da nave
        if over:
            self.image = self.dicionario_de_arquivos['btn_hover']
        else:
            self.image = self.dicionario_de_arquivos['btn']
