import pygame as pg
import sys,random

def make_button(self, pos, text, color, action=None, textsize=20):
        mouse = pg.mouse.get_pos()
        oldpos = pos
        rect = pg.Rect(pos)
        pos = rect.topleft
        rect.topleft = 0,0
        rectangle = pg.Surface(rect.size,pg.SRCALPHA)
        
        circle = pg.Surface([min(rect.size)*3]*2,pg.SRCALPHA)
        pg.draw.ellipse(circle,(0,0,0),circle.get_rect(),0)
        circle  = pg.transform.smoothscale(circle,[int(min(rect.size)*0.5)]*2)
        
        radius = rectangle.blit(circle,(0,0))
        radius.bottomright = rect.bottomright
        rectangle.blit(circle,radius)
        radius.topright     = rect.topright
        rectangle.blit(circle,radius)
        radius.bottomleft   = rect.bottomleft
        rectangle.blit(circle,radius)
        

        rectangle.fill((0,0,0),rect.inflate(-radius.w,0))
        rectangle.fill((0,0,0),rect.inflate(0,-radius.h))
        pos = oldpos
        if (pos[0]+pos[2]) > mouse[0] > pos[0] and (pos[1]+pos[3]) > mouse[1] > pos[1]:
            self.hover = True
            self.buttonclick = action
            color = pg.Color(*color[1])
            alpha = color.a
            color.a = 0
        else:
            color = pg.Color(*color[0])
            alpha = color.a
            color.a = 0
            self.hover = False
        rectangle.fill(color,special_flags=pg.BLEND_RGBA_MAX)
        rectangle.fill((255,255,255, alpha),special_flags=pg.BLEND_RGBA_MIN)   
        self.screen.blit(rectangle,pos)
        txts = pg.font.SysFont('Courier New',textsize).render(text,True,(0,0,0))
        txtrect = txts.get_rect()
        txtrect.center =(pos[0]+pos[2]/2), (pos[1]+pos[3]/2)
        self.screen.blit(txts,txtrect)