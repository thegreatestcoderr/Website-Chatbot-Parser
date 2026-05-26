import pygame as pg
pg.init()
screen = pg.display.set_mode((800, 800))
x = 200
y = 125
z = 275
a = 125
b = 275
pg.draw.line(screen, (255, 0, 0), (x, 200), (x, 560), 5)
pg.draw.line(screen, (255, 0, 0), (x, 560), (y, 720), 5)
pg.draw.line(screen, (255, 0, 0), (x, 560), (z, 720), 5)
pg.draw.line(screen, (255, 0, 0), (x, 300), (a, 460), 5)
pg.draw.line(screen, (255, 0, 0), (x, 300), (b, 460), 5)
pg.draw.circle(screen, (255, 0, 0), (x, 150), 50, 5)
pg.display.flip
pg.display.update()
run = True
while run == True:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit
            run = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                while x < 800:
                    pg.draw.line(screen, (0, 0, 0), (x, 200), (x, 560), 5)
                    pg.draw.line(screen, (0, 0, 0), (x, 560), (y, 720), 5)
                    pg.draw.line(screen, (0, 0, 0), (x, 560), (z, 720), 5)
                    pg.draw.line(screen, (0, 0, 0), (x, 300), (a, 460), 5)
                    pg.draw.line(screen, (0, 0, 0), (x, 300), (b, 460), 5)
                    pg.draw.circle(screen, (0, 0, 0), (x, 150), 50, 5)
                    pg.display.flip
                    pg.display.update()
                    x += 1
                    y += 10
                    z += 10
                    a += 10
                    b += 10
                    pg.draw.line(screen, (255, 0, 0), (x, 200), (x, 560), 5)
                    pg.draw.line(screen, (255, 0, 0), (x, 560), (y, 720), 5)
                    pg.draw.line(screen, (255, 0, 0), (x, 560), (z, 720), 5)
                    pg.draw.line(screen, (255, 0, 0), (x, 300), (a, 460), 5)
                    pg.draw.line(screen, (255, 0, 0), (x, 300), (b, 460), 5)
                    pg.draw.circle(screen, (255, 0, 0), (x, 150), 50, 5)
                    pg.display.flip
                    pg.display.update()
            if event.key == pg.K_RIGHT:
                while x > 0:
                    pg.draw.line(screen, (0, 0, 0), (x, 200), (x, 560), 5)
                    pg.draw.line(screen, (0, 0, 0), (x, 560), (y, 720), 5)
                    pg.draw.line(screen, (0, 0, 0), (x, 560), (z, 720), 5)
                    pg.draw.line(screen, (0, 0, 0), (x, 300), (a, 460), 5)
                    pg.draw.line(screen, (0, 0, 0), (x, 300), (b, 460), 5)
                    pg.draw.circle(screen, (0, 0, 0), (x, 150), 50, 5)
                    pg.display.flip
                    pg.display.update()
                    x -= 1
                    y -= 1
                    z -= 1
                    a -= 10
                    b -= 10
                    pg.draw.line(screen, (255, 0, 0), (x, 200), (x, 560), 5)
                    pg.draw.line(screen, (255, 0, 0), (x, 560), (y, 720), 5)
                    pg.draw.line(screen, (255, 0, 0), (x, 560), (z, 720), 5)
                    pg.draw.line(screen, (255, 0, 0), (x, 300), (a, 460), 5)
                    pg.draw.line(screen, (255, 0, 0), (x, 300), (b, 460), 5)
                    pg.draw.circle(screen, (255, 0, 0), (x, 150), 50, 5)
                    pg.display.flip
                    pg.display.update()
pg.quit
