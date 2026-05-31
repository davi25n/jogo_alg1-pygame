import pygame


tamanho_tela = (1200, 800)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("labirinto")

#definir parametros que serão usados

tamanho_jogador = 5
jogador = pygame.Rect(2, 2, tamanho_jogador, tamanho_jogador)
tamanho_monstro = 5
monstro = pygame.Rect(x, y, tamanho_monstro, tamanho_monstro)

parede = pygame.Rect(0, 0, 1200, 800)
distancia_parede = 20
#as paredes terão de ser desenhadas a mão, ou então precisamos descobrir um algoritmo de aleatoriedade
#que crie as paredes desenhando-as conforme parametros pre estabelecidos de distancia
def criar_paredes():
    paredes = []
    for x in range(tamanho_tela[0] // distancia_parede):
        parede = pygame.Rect(x*distancia_parede, 0, 20, 800)
        paredes.append(parede)
    for y in range(tamanho_tela[1] // distancia_parede):
        parede = pygame.Rect(0, y*distancia_parede, 1200, 20)
        paredes.append(parede)
    return paredes

paredes = criar_paredes()
