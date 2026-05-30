import pygame

#inicializar
pygame.init()

tamanho_tela = (800, 800)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("brick breaker")

tamanho_bola = 15
bola = pygame.Rect(400, 500, tamanho_bola, tamanho_bola)
tamanho_jogador = 100
jogador = pygame.Rect(0, 750,  tamanho_jogador, 20)
quantidade_blocos_linha = 8
quantidade_linhas = 5
quantidade_total_blocos = quantidade_blocos_linha * quantidade_linhas

def criar_blocos(quantidade_blocos_linha, quantidade_linhas):
    blocos = []
    #criar blocos
    return blocos

cores = {
    "branco": (255, 255, 255),
    "preto": (0, 0, 0),
    "amarelo": (255, 255, 0),
    "azul": (0, 0, 255),
    "verde": (0, 255, 0)
}

fim_jogo = False

pontuacao = 0

movimento_bola = [1, 1]

#criar as funçoes

#desenhar o que aparecerá na tela
tela.fill(cores["preto"])

#cria um loop infinito
while not fim_jogo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim_jogo = True
    pygame.time.wait(1)
    pygame.display.flip()

pygame.quit()