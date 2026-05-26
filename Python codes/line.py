import pygame as pg
pg.init()
screen = pg.display.set_mode((800, 800))
pg.draw.line(screen, (255, 0, 0), (60, 80), (60, 580))
pg.draw.line(screen, (255, 0, 0), (60, 250), (200, 250))
pg.draw.line(screen, (255, 0, 0), (60, 80), (200, 80))
pg.draw.line(screen, (255, 0, 0), (200, 80), (200, 580))
pg.draw.line(screen, (255, 0, 0), (240, 580), (240, 400))
pg.draw.line(screen, (255, 0, 0), (240, 400), (380, 400))
pg.draw.line(screen, (255, 0, 0), (380, 400), (380, 580))
pg.draw.line(screen, (255, 0, 0), (420, 580), (420, 400))
pg.draw.line(screen, (255, 0, 0), (420, 400), (560, 400))
pg.draw.line(screen, (255, 0, 0), (560, 380), (560, 580))
pg.draw.line(screen, (255, 0, 0), (420, 580), (580, 580))
pg.draw.line(screen, (255, 0, 0), (620, 580), (620, 400))
pg.draw.line(screen, (255, 0, 0), (620, 580), (760, 580))
pg.draw.line(screen, (255, 0, 0), (760, 400), (760, 750))
pg.draw.line(screen, (255, 0, 0), (760, 750), (620, 750))
pg.display.flip()
run = True
while run == True:
    pg.draw.rect(screen, (255, 0, 0), (300, 250, 50, 50))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit
            run = False
pg.quit()            
