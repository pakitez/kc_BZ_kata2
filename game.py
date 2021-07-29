import pygame as pg

TAMANNO = (800,600)

class Bola():
    def __init__(self, x, y, w, h, color = (255,255,255)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        #self.derecha = True
        #self.arriba = True

        self.incrementox = 5
        self.incrementoy = 5

    def actualizarBola(self):
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
        #self.reloj = pg.time.Clock()
        self.bucle_principal()

    def bucle_principal(self):
        bola = Bola(TAMANNO[0]//2 - 10, TAMANNO[1]//2 - 10, 20,20)
        game_over = False
        pg.init()

        while not game_over:
            #self.reloj.tick(60)

            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over = True

            bola.actualizarBola()

            self.pantalla.fill((0,0,0))
            pg.draw.rect(self.pantalla, bola.color, pg.Rect(bola.x, bola.y, bola.w, bola.h))
            pg.display.flip()

        pg.quit()



juego = Game()

if __name__ == "__main__":
    juego = Game()
