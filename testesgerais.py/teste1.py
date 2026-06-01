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
    altura_tela = tamanho_tela[1]
    largura_tela = tamanho_tela[0]
    distancia_blocos = 5
    largura_bloco = (largura_tela // quantidade_blocos_linha) - distancia_blocos
    altura_bloco = 20
    blocos = []
    #criar blocos
    for j in range(quantidade_linhas):
        for i in range(quantidade_blocos_linha):
            bloco = pygame.Rect(i*(largura_bloco + distancia_blocos), j*(altura_bloco + distancia_blocos*2), largura_bloco, altura_bloco)
            blocos.append(bloco)
    return blocos

cores = {
    "branco": (255, 255, 255),
    "preto": (0, 0, 0),
    "amarelo": (255, 255, 0),
    "azul": (0, 0, 255),
    "verde": (0, 255, 0)
}

# Variável GLOBAL que controla o loop do jogo
# Quando fim_jogo = True, o loop while encerra
fim_jogo = False

pontuacao = 0


movimento_bola = [3, -3]

#criar as funçoes
def movimentar_jogador(evento):
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_RIGHT and jogador.right < tamanho_tela[0]:
            jogador.x += 2
        if evento.key == pygame.K_LEFT and jogador.left > 0:
            jogador.x -= 2

def movimentar_bola(bola):
    movimento = movimento_bola
    bola.x += movimento[0]
    bola.y += movimento[1]
    if bola.x  <= 0 or bola.x + tamanho_bola >= tamanho_tela[0]:
        movimento[0] *= -1
    if bola.y <= 0:
        movimento[1] *= -1
    if bola.y + tamanho_bola >= tamanho_tela[1]:
        movimento = None
    if jogador.collidepoint(bola.x, bola.y):
        movimento[1] *= -1
    for bloco in blocos:
        if bloco.collidepoint(bola.x, bola.y):
            movimento[1] *= -1
            blocos.remove(bloco)
    return movimento

def atualizar_pontuacao(pontuacao):
    fonte = pygame.font.Font(None, 30)
    texto = fonte.render(f"Pontuação: {pontuacao}", 1, cores["verde"])
    tela.blit(texto, (10, 150))
    if pontuacao >= quantidade_total_blocos:
        return True
    return False

#desenhar o que aparecerá na tela
def desenhar_inicio_jogo(): 
    tela.fill(cores["preto"])
    pygame.draw.rect(tela, cores["azul"], jogador)
    pygame.draw.rect(tela, cores["branco"], bola)
def desenhar_blocos(blocos):
    for bloco in blocos:
        pygame.draw.rect(tela, cores["amarelo"], bloco)

    

blocos = criar_blocos(quantidade_blocos_linha, quantidade_linhas)


#cria um loop infinito
while not fim_jogo:
    desenhar_inicio_jogo()
    desenhar_blocos(blocos)
    fim_jogo = atualizar_pontuacao(quantidade_total_blocos - len(blocos))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim_jogo = True
    movimentar_jogador(evento)
    movimento_bola = movimentar_bola(bola)
    if not movimento_bola:
        fim_jogo = True
    pygame.time.wait(2)
    pygame.display.flip()
print("game over")
pygame.quit()