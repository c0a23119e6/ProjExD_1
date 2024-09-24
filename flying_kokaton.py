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
    kk_rct = kk_img.get_rect() #8
    kk_rct.center = 300, 200 #8
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed() #8-3

        a = 0 #縦
        b = 0 #横

        if key_lst[pg.K_UP]: #上矢印キーがTrueなら
            a = -1 #こうかとんの縦座標を-1にする
        if key_lst[pg.K_DOWN]: #下矢印キーがTrueなら
            a = 1 #こうかとんの縦座標を1にする
        if key_lst[pg.K_LEFT]: #左矢印キーがTrueなら
            b = -1 #こうかとんの横座標を-1にする
        if key_lst[pg.K_RIGHT]: #右矢印キーがTrueなら
            b =  1 #こうかとんの縦座標を1にする
        else:
            b = -1

        kk_rct.move_ip((b,a))

        x = -(tmr%3200) #6
        screen.blit(bg_img, [x, 0]) #6
        screen.blit(bg2_img, [x+1600, 0]) #7-2
        screen.blit(bg_img, [x+3200, 0]) #7-2
        screen.blit(bg2_img, [x+4800, 0]) #7-2
        screen.blit(kk_img, kk_rct) #8-5
        pg.display.update()
        tmr += 1        
        clock.tick(400) #5


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()