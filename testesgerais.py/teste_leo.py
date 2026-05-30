import pygame
import sys

# --- Inicialização ---
pygame.init()

LARGURA, ALTURA = 600, 400
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Meu Primeiro Pygame")

relogio = pygame.time.Clock()

# --- Configurações do quadrado ---
x, y = 270, 170        # posição inicial (centro)
tamanho = 50
velocidade = 5

COR_FUNDO   = (30, 30, 30)   # cinza escuro
COR_QUADRADO = (0, 200, 255) # azul cyan

# --- Loop principal ---
while True:

    # 1) Eventos (fechar janela, teclas, etc.)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 2) Leitura contínua das teclas pressionadas
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        x -= velocidade
    if teclas[pygame.K_RIGHT]:
        x += velocidade
    if teclas[pygame.K_UP]:
        y -= velocidade
    if teclas[pygame.K_DOWN]:
        y += velocidade

    # Impede o quadrado de sair da tela
    x = max(0, min(x, LARGURA - tamanho))
    y = max(0, min(y, ALTURA  - tamanho))

    # 3) Desenho
    tela.fill(COR_FUNDO)                                    # limpa a tela
    pygame.draw.rect(tela, COR_QUADRADO, (x, y, tamanho, tamanho))

    # 4) Atualiza a janela e limita a 60 FPS
    pygame.display.flip()
    relogio.tick(60)


