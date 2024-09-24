import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg2_img = pg.transform.flip(bg_img,True,False) #7-1
    kk_img = pg.image.load("fig/3.png") #練習２
    kk_img = pg.transform.flip(kk_img,True,False) #練習２
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = -(tmr%3200) #6
        screen.blit(bg_img, [x, 0]) #6
        screen.blit(bg2_img, [x+1600, 0]) #7-2
        screen.blit(bg_img, [x+3200, 0]) #7-2
        screen.blit(bg2_img, [x+4800, 0]) #7-2
        screen.blit(kk_img, [300, 200]) #4
        pg.display.update()
        tmr += 1        
        clock.tick(200) #5


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()