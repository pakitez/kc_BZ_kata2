import pygame as pg
from random import randrange

TAMANNO = (800,600)

class Movil():
    def __init__(self, x, y, w, h, color = (255,255,255)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
    
    def actualizate(self):
        pass 

    def dibujate(self, lienzo):
        pg.draw.rect(lienzo, self.color, pg.Rect(self.x, self.y, self.w, self.h))

    @property
    def derecha(self):
        return self.x + self.w

    @derecha.setter
    def derecha(self, valor):
         self.x + self.w

    @property
    def izquierda(self):
        return self.x

    @izquierda.setter
    def izquierda(self, valor):
        self.x = valor

    @property
    def arriba(self):
        return self.y

    @arriba.setter
    def arriba(self, valor):
        self.y = valor

    @property
    def abajo(self):
        return self.y + self.h

    @abajo.setter
    def abajo(self, valor):
        self.y = valor - self.h 

    def procesa_eventos(self, lista_eventos=[]):
        pass
    

class Raqueta(Movil):
    def __init__(self, x, y, color = (255,255,255)):
        Movil.__init__(self, x, y, 20, 120, color)

        self.tecla_arriba = pg.K_UP
        self.tecla_abajo = pg.K_DOWN

    def procesa_eventos(self, lista_eventos=[]):
        if pg.key.get_pressed()[self.tecla_arriba]:
            self.y -= 5

        if pg.key.get_pressed()[self.tecla_abajo]:
            self.y += 5

        if self.arriba <= 0:
            self.y = 0

        if self.abajo >= TAMANNO[1]:
            self.abajo = TAMANNO[1]
            #self.y = TAMANNO[1] - self.h




class Bola(Movil):
    def __init__(self, x, y, color = (255,255,255)):
        super().__init__(x, y, 20, 20, color)
        #self.x = x
        #self.y = y
        #self.w = w
        #self.h = h
        #self.color = color
        self.derecha = True
        self.arriba = True

        self.incrementox = 5
        self.incrementoy = 5

    def actualizate(self):
        """""
        if self.derecha:
            self.x += 5
        else:
            self.x -= 5

        if self.x+20 >= TAMANNO[0]:
            self.derecha = False

        if self.x<= 0:
            self.derecha = True

        if self.arriba:
            self.y += 5
        else:
            self.y -= 5

        if self.y+20 >= TAMANNO[1]:
            self.arriba = False

        if self.y<= 0:
            self.arriba = True


        #self.x += 5
        #self.y -= 5
        """

        self.x += self.incrementox
        self.y += self.incrementoy

        if self.x + self.w > TAMANNO[0] or self.x < 0:
            self.incrementox *= -1

        if self.y + self.h > TAMANNO[1] or self.y < 0:
            self.incrementoy *= -1



class Game():

    def __init__(self):
        
        self.pantalla = pg.display.set_mode(TAMANNO)
        self.reloj = pg.time.Clock()
        #self.bolas = []
        #self.players = []

        self.moviles = []

        self.player1 =  Raqueta(10, (TAMANNO[1] - 120)// 2)
        self.player2 =  Raqueta(TAMANNO[0]-20 -10, (TAMANNO[1]- 120)// 2)

        self.player1.tecla_abajo = pg.K_s
        self.player1.tecla_arriba = pg.K_w


        for i in range(1):
            #tamanyo = randrange(10,41)
            bola = Bola(TAMANNO[0] // 2 -10, 
                                        TAMANNO[1] // 2 - 10,
                                        (randrange(256),randrange(256),randrange(256)))
            
            self.derecha = randrange(2)==1
            self.arriba = randrange(2)==1
            #self.bolas.append(bola)
            self.moviles.append(bola)

            #self.players.append(self.player1)
            #self.players.append(self.player2)
            self.moviles.append(self.player1)
            self.moviles.append(self.player2)

        #self.bola = Bola(700-10, TAMANNO[1]//2-10, 20, 30)
        #self.bola2 = Bola(0, 0, 15, 15, (255,0,0))

    def bucle_principal(self):
        #bola = Bola(TAMANNO[0]//2 - 10, TAMANNO[1]//2 - 10, 20,20)
        game_over = False
        pg.init()

        while not game_over:
            self.reloj.tick(60)

            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over = True

                '''
                if pg.key.get_pressed()[pg.K_UP]:
                    self.player2.y -= 5

                if pg.key.get_pressed()[pg.K_DOWN]:
                    self.player2.y += 5

                if pg.key.get_pressed()[pg.K_w]:
                    self.player1.y -= 5

                if pg.key.get_pressed()[pg.K_S]:
                    self.player1.y += 5


                
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_UP:
                        self.player2.y -= 5

                    if evento.key == pg.K_DOWN:
                        self.player2.y += 5

                    if evento.key == pg.K_w:
                        self.player1.y -= 5

                    if evento.key == pg.K_s:
                        self.player1.y += 5

            
            self.bola.actualizarBola()
            self.bola2.actualizarBola()

            for i in range(len(self.bolas)):
                self.bolas[i].actualizate()'''

            for movil in self.moviles:
                movil.procesa_eventos()
                movil.actualizate()
            

            self.pantalla.fill((0,0,0))

            for movil in self.moviles:
                movil.dibujate(self.pantalla)

            '''
            for bola in self.bolas:
                pg.draw.rect(self.pantalla, bola.color, pg.Rect(bola.x, bola.y, bola.w, bola.h))

            for player in self.players:
                pg.draw.rect(self.pantalla, player.color, pg.Rect(player.x, player.y, player.w, player.h))

            '''            
            
            pg.display.flip()

        pg.quit()




if __name__ == "__main__":
    juego = Game()
    juego.bucle_principal()
