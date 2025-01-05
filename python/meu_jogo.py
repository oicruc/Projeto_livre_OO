import pygame
from sys import exit
from pygame.locals import *


class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.__vidamax = 100
        self.__vida = 100
        
    def vida_personagem(self,vida):
        self.__vida = vida
        self.__vidamax = vida
    
    def mostra_vida(self):
        return self.__vida
    
    def mostra_vida_max(self):
        return self.__vidamax

    
    def restore(self, mais):
        if self.__vida + mais <= self.__vidamax:
            self.__vida+= mais
        else:
            self.__vida = self.__vidamax

    
    def recebe(self, dano):
        if self.__vida - dano <= 0 :
            self.__vida = 0
            return self.__vida
        else:
            self.__vida -=dano
            return self.__vida


class Slime(Personagem):
    def __init__(self,imortal):
        Personagem.__init__(self)
        self.__imortal = imortal


        self.__sprite =[]
        self.__sprite.append(pygame.image.load('slime/rwefbu4z4zsb1.png'))
        self.image = self.__sprite[0]
        self.image = pygame.transform.scale(self.image,(208//2,120//2))
        self.rect = self.image.get_rect()
        self.__x = 100
        self.__y = 190
        self.rect.topleft = self.__x, self.__y
    
    def andar (self,xi,yi):
        if xi ==1:
            self.__x += 5
        elif yi==1:
            self.__y += 5
        elif xi== -1:
            self.__x-= 5
        else:
            self.__y-= 5
        self.rect.topleft = self.__x, self.__y

    def pos(self,x2,y2):
        self.__x = x2
        self.__y = y2
        self.rect.topleft = self.__x, self.__y
    def tamanho(self,x):
        self.image = pygame.transform.scale(self.image,(208//x,120//x))
    def ent_posx(self):
        return self.__x
    def ent_posy(self):
        return self.__y

    def isimortal(self):
        return self.__imortal


class Boss(Personagem):
    def __init__(self):
        Personagem.__init__(self)
        self.__laser = pygame.image.load("king_slime/laser.png")
        self.__laser = pygame.transform.scale(self.__laser,(32*20,32*20))

pygame.init()
tela = pygame.display.set_mode((640,480))
prox = 1
todas_as_sprites = pygame.sprite.Group()
pygame.display.set_caption("meu jogo")

fonte = pygame.font.SysFont('arial', 60, bold=False, italic=True)
texto = fonte.render("Meu Jogo",True,(255,0,0))
fonte_sub = pygame.font.SysFont('arial',30,False, False)
texto_sub = fonte_sub.render("aperte qualquer tecla para jogar",True,(0,0,0))

while prox: #tela inicial
    tela.fill((255,255,255))
    tela.blit(texto, (190,30))
    tela.blit(texto_sub,(150, 220))
    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                player = Slime(1)
                todas_as_sprites.add(player)
                prox = 0
            else:
                player = Slime(0)
                todas_as_sprites.add(player)
                prox = 0


    pygame.display.update()
prox = 1

# imagem da tela
telas_de_fundo =[]
telas_de_fundo.append(pygame.image.load("mapa/tela_casa.png"))
telas_de_fundo.append(pygame.image.load("mapa/foradecasa.png"))
telas_de_fundo.append(pygame.image.load("mapa/caminho_1.png"))
telas_de_fundo.append(pygame.image.load("mapa/caminho_2.png"))
telas_de_fundo.append(pygame.image.load("mapa/templo_fora.png"))
telas_de_fundo.append(pygame.image.load("mapa/dojo.png"))
telas_de_fundo.append(pygame.image.load("mapa/imagem_batalha.png"))


for x in range(0,6+1):
    telas_de_fundo[x] = pygame.transform.scale(telas_de_fundo[x],(640,480))
fala_maior_nome = (0,480-150,640,150)
fala_nome =       (0,480-150-50,170 ,50)

prox_palavra = 0

frases = [] #frases escritas
frases.append("Era uma vez, em um reino distante, uma geléia chamada Oli e um ninja chamado Gold")
frases.append("não pergunte o porquê.")
frases.append("Eles viviam em uma casa, longe de problemas.")
frases.append("O Gold sempre falava de seu mestre, o Sensei que vivia à leste da região.")
frases.append("Seu mestre o ensinara desde criança a arte dos ninjas") 
frases.append("Até que um dia, uma geléia gigante entrou na casa deles ")
frases.append("e engoliu o Gold sem nenhuma explicação")
frases.append("Em sua agonia Oli apenas entendeu uma frase de seu amigo")
frases.append("VÁ AO SENSEI")
fonte = pygame.font.SysFont("arial", 20, bold=False, italic=False)
fonte2= pygame.font.SysFont("arial", 20, bold=False, italic=True)

ninja = pygame.image.load("ninja/d4rx4gs-0db63355-e4f1-410f-9b7c-e96a15ae60f5.png")
ninja = pygame.transform.scale(ninja, (332//7,444//7))

boss = pygame.image.load("king_slime/KingSlime.png")
boss = pygame.transform.scale(boss,(1134//5,1015//5))
try_this = 640

while prox: #história
    for event in pygame.event.get():
        if event.type ==QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                prox_palavra +=1
        if prox_palavra == 9:
            prox = 0

    if prox_palavra < 9:
        telas_de_fundo[0] =pygame.transform.scale(telas_de_fundo[0],(640,480-150))
        tela.blit(telas_de_fundo[0],(0,0))
        pygame.draw.rect(tela, (75,50,50),fala_maior_nome)
        pygame.draw.rect(tela,(200,200,200),fala_nome)
        tela.blit((fonte.render(frases[prox_palavra],True,(255,255,255))),fala_maior_nome)
        tela.blit((fonte2.render("Locutor",True,(0,0,0))),(30, 480-150-40))
        tela.blit((fonte2.render("aperte espaço para continuar",True,(0,0,0))),(375,480-40))
        todas_as_sprites.draw(tela)
        if prox_palavra < 6:
            tela.blit(ninja,(400,210))
        else:
            while try_this > 300:
                try_this-=1
                pygame.display.flip()
                tela.blit(boss,(try_this, 50))
            try_this =300
            tela.blit(boss,(try_this, 100))

   
    pygame.display.flip()

prox=1
player.pos(370,310)
relogio = pygame.time.Clock()
mundo = 1
maior = 370
aviso =0
player.tamanho(3)

while prox: #caminho para o templo
    relogio.tick(50)
    if player.ent_posy() < 360 and aviso == 0:
        player.andar(0,1)
        player.andar(1,0)
    if player.ent_posx()  == 640 and aviso ==0 :
        mundo = 2
        player.pos(370,450)
        aviso = 1
        maior = 300
    if player.ent_posx()  == 640 and aviso ==1 :
        mundo = 4
        player.pos(250,390)
        player.tamanho(4)
        aviso = 2
    if aviso ==2 and player.ent_posx() == 310:
        prox = 0

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    if pygame.key.get_pressed()[K_d]:
        player.andar(1,0)
    if pygame.key.get_pressed()[K_a] and (aviso ==0 or aviso ==2) :
        if aviso !=2:
            player.andar(-1,0)
        elif aviso ==2 and player.ent_posx() >= 250:
            player.andar(-1,0)
    if pygame.key.get_pressed()[K_a] and aviso ==1 and player.ent_posx() >= 370 :
        player.andar(-1,0)
    if pygame.key.get_pressed()[K_s] and aviso != 2:
        player.andar(0,1)
    if pygame.key.get_pressed()[K_w] and aviso != 2:
        if player.ent_posy() >= maior:
            player.andar(0,-1)        
    tela.blit(telas_de_fundo[mundo],(0,0))
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    
    pygame.display.flip()

prox =1
prox_palavra = 0
player.pos(250,260)
player.tamanho(2)

frases = [] 
frases.append("Boa noite, o senhor é o sensei que o Gold sempre falou?")
frases.append("Provavelmente, conheço o Gold desde quando ele era uma pequena criança.")
frases.append("Ele foi raptado, por uma geléia com uma coroa dourada e me disse para ir até você.")
frases.append("Esta geléia que você me falou, é azul?")
frases.append("Sim, ela é sim. Como sabia?")
frases.append("Na época de minha juventude, meu sensei trouxe uma geléia azul para este dojo")
frases.append("Nós sempre treinávamos juntos, mas sempre nas lutas eu via algo sombrio nela.")
frases.append("No último dia de vida do meu sensei, ele quis passar suas armas poderosas")
frases.append("Ele deu à geléia a coroa-do-ultimo-sobrevivente,")
frases.append("uma arma poderosa capaz de matar todos a sua volta, mas tinha uma única condição")
frases.append("utilizar de toda sua energia numm único golpe, sendo obrigado a descansar por um dia.")
frases.append("Ainda consigo lembrar de sua áurea sombria ao encostar naquela coroa")
frases.append("No momento seguinte, ele me prendeu dentro de si mesmo")
frases.append("e utilizando da minha energia, destruiu o local de cerimônias.")
frases.append("Não me lembro de mais nada daquele dia.")
frases.append("só do dia seguinte, quando vi meu sensei morto")
frases.append("e em sua mão tinha uma carta, dizendo:")
frases.append("Querido aluno, eu lhe dou a única arma que pode ir contra a coroa, a adaga-do-redentor")
frases.append("Peço que continue o dojo como sensei, e salve o mundo com esta adaga")
frases.append("Creio que ele quer usar o Gold para o mesmo feito, irei te acomapnhar nesta jornada")
frases.append("creio que sei onde ele está")

sensei = pygame.image.load("sensei/sensei.png")
sensei = pygame.transform.scale(sensei,(32*7,32*7))

telas_de_fundo[5] =pygame.transform.scale(telas_de_fundo[5],(640,480-150))

while prox: #história no templo
    relogio.tick(100)
    tela.blit(telas_de_fundo[5],(0,0))
    for event in pygame.event.get():
        if event.type ==QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                prox_palavra +=1
        if prox_palavra == 21:
            prox = 0
    if prox_palavra < 21:
        tela.blit(telas_de_fundo[5],(0,0))
        pygame.draw.rect(tela, (75,50,50),fala_maior_nome)
        pygame.draw.rect(tela,(200,200,200),fala_nome)
        tela.blit((fonte.render(frases[prox_palavra],True,(255,255,255))),fala_maior_nome)
        if prox_palavra == 0 or prox_palavra ==2 or prox_palavra ==4:
             tela.blit((fonte2.render("Oli",True,(0,0,0))),(30, 480-150-40))
        else:
            tela.blit((fonte2.render("Sensei",True,(0,0,0))),(30, 480-150-40))
        tela.blit((fonte2.render("aperte espaço para continuar",True,(0,0,0))),(375,480-40))
    todas_as_sprites.draw(tela)
    tela.blit(sensei,(400,150))
    pygame.display.flip()

prox =1
prox_palavra = 0
frases = [] 
frases.append("Aqui é o lugar onde a cerimônia ocorreu") #0
frases.append("Sim, eu me lembro, velho amigo") #1
frases.append("Sabia que te encontraria aqui, geléia") #2
frases.append("Agora me diga como se chama agora?") #3
frases.append("Para os inimigos, King Slime") #4
frases.append("você desonrou o nosso sensei com esta coroa, o que pretende fazer com Gold?") #5
frases.append("Este menino? O mesmo que fiz com você") #6
frases.append("porém desta vez, eu irei te parar. Agora me diga, o que devo escrever no seu túmulo?") #7
frases.append("NÂO ESTARÁ VIVO PARA ESCREVER") #8
frases.append("O King Slime carrega sua coroa com a energia do Gold que grita dentro da geléia") #9
frases.append("não terei outra escolha se não usar minha adaga.")#10
frases.append("") #11
frases.append("peço que tire o Gold dele caso eu não consiga, já que usei toda a minha energia") #12

telas_de_fundo[3] =pygame.transform.scale(telas_de_fundo[3],(640,480-150))
sensei = pygame.transform.scale(sensei,((32*7)//2,(32*7)//2))
player.tamanho(4)
player.pos(220,260)
boss = pygame.transform.scale(boss,(1134//10,1015//10))
try_this = 637 
while prox: # historia luta
    relogio.tick(50)
    for event in pygame.event.get():
        if event.type ==QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                prox_palavra +=1
        if prox_palavra == 13:
            prox = 0
    if prox_palavra < 13:
        tela.blit(telas_de_fundo[3],(0,0))
        pygame.draw.rect(tela, (75,50,50),fala_maior_nome)
        pygame.draw.rect(tela,(200,200,200),fala_nome)
        tela.blit((fonte.render(frases[prox_palavra],True,(255,255,255))),fala_maior_nome)
        tela.blit((fonte2.render("aperte espaço para continuar",True,(0,0,0))),(375,480-40))
        todas_as_sprites.draw(tela)
        if prox_palavra == 0:
            tela.blit(sensei,(255,240))
        elif prox_palavra > 0 and prox_palavra !=11:
            sensei = pygame.image.load("sensei/sensei_de lado.png")
            sensei = pygame.transform.scale(sensei,((32*7)//2,(32*7)//2))
            if try_this > (255 +32*6):
                try_this -= 5
            tela.blit(sensei,(255,240))
            tela.blit(boss,(try_this, 220))
        else:
            sensei = pygame.image.load("sensei/sensei_adaga.png")
            sensei = pygame.transform.scale(sensei,((32*7)//2,(32*7)//2))
            tela.blit(sensei,(255,240))
            tela.blit(boss,(255 + (32)*6, 220))
            laser = pygame.image.load("king_slime/laser.png")
            laser = pygame.transform.scale(laser,((32*7)//2,(32*7)//2))
            tela.blit(laser,(255 + (32)*3,240))
        if prox_palavra == 9 or prox_palavra == 11 :
            tela.blit((fonte2.render("Locutor",True,(0,0,0))),(30, 480-150-40))
        elif prox_palavra == 1 :
            tela.blit((fonte2.render("???????",True,(0,0,0))),(30, 480-150-40))
        elif prox_palavra == 4 or prox_palavra == 6 or  prox_palavra == 8:
            tela.blit((fonte2.render("King Slime",True,(0,0,0))),(30, 480-150-40))
        else:
            tela.blit((fonte2.render("Sensei",True,(0,0,0))),(30, 480-150-40))
    pygame.display.flip()
        
prox = 1
geleia = Boss()
vez = 0
defe = 0
player.pos(100,300)
geleia.vida_personagem(100)
vit = 0
player.tamanho(2)
boss = pygame.transform.scale(boss,(1134//5,1015//5))

fonte = pygame.font.SysFont('arial', 60, bold=False, italic=True)
texto = fonte.render("Voce perdeu",True,(255,0,0))
fonte_sub = pygame.font.SysFont('arial',30,False, False)
texto_sub = fonte_sub.render("aperte espaço para continuar",True,(0,0,0))
fonte_ajuda =  pygame.font.SysFont('arial',30,False, False)
texto_ajuda = fonte_ajuda.render("(A) para atacar, (C) para cura, (D) para defesa",True,(255,255,255))

while prox: #luta final
    relogio.tick(1)
    if vez == 1:
        vez = 0
        if defe == 0:
            player.recebe(30)
        else :
            player.recebe(15)
            geleia.recebe(5)
        
    for event in pygame.event.get():
        if event.type ==QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN and vez == 0:
            if event.key == K_a:
                geleia.recebe(10)
                vez = 1
            elif event.key == K_c:
                player.restore(45)
                vez = 1
            elif event.key == K_d:
                defe = 1
                vez = 1
    if player.mostra_vida() == 0:
        prox2 = 1
        player.vida_personagem(100)
        geleia.vida_personagem(100)
        while prox2:
            tela.fill((255,255,255))
            tela.blit(texto, (190,30))
            tela.blit(texto_sub,(150, 220))
            for event in pygame.event.get():
                if event.type == QUIT :
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        prox2 =0
            pygame.display.flip()


    elif geleia.mostra_vida() == 0:
        prox = 0
        vit = 1
    tela.blit(telas_de_fundo[6],(0,0))
    todas_as_sprites.draw(tela)
    tela.blit(boss,(340, 170))
    pygame.draw.rect(tela,(255,0,0),(105,370,(player.mostra_vida_max()*2)//3,6))
    pygame.draw.rect(tela,(0,255,0),(105,370,(player.mostra_vida()*2)//3,6))
    pygame.draw.rect(tela,(255,0,0),(350,385,geleia.mostra_vida_max()*2,6))
    pygame.draw.rect(tela,(0,255,0),(350,385,(geleia.mostra_vida()*2),6))
    tela.blit(texto_ajuda,(0,0))
    pygame.display.flip()

prox = 1
fonte = pygame.font.SysFont('arial', 60, bold=False, italic=True)
texto = fonte.render("Voce venceu",True,(0,255,0))
fonte_sub = pygame.font.SysFont('arial',30,False, False)
texto_sub = fonte_sub.render("aperte espaço para acabar",True,(0,0,0))
while prox:
    tela.fill((255,255,255))
    tela.blit(texto, (150,30))
    tela.blit(texto_sub,(150, 220))
    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pygame.quit()
                    exit()
    pygame.display.flip()
