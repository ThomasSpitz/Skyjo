import pygame
from pygame.locals import *
import jeu

def afficher_carte(x,y,background,screen,p,value=66):
    if value ==-2 :
        pygame.draw.rect(background,(47,54,155),Rect(x,y,7*p,7*p))
        pygame.draw.rect(background,"black",Rect(x+3*p,y+p,3*p,p))
        pygame.draw.rect(background,"black",Rect(x+5*p,y+2*p,p,p)) 
        pygame.draw.rect(background,"black",Rect(x+3*p,y+3*p,3*p,p))
        pygame.draw.rect(background,"black",Rect(x+3*p,y+4*p,p,p))
        pygame.draw.rect(background,"black",Rect(x+3*p,y+5*p,3*p,p))
        pygame.draw.rect(background,"black",Rect(x+p,y+3*p,p,p)) 

    elif value == -1:
        pygame.draw.rect(background,(47,54,155),Rect(x,y,7*p,7*p))
        pygame.draw.rect(background,"black",Rect(x+3*p,y+p,p,p))
        pygame.draw.rect(background,"black",Rect(x+4*p,y+p,p,5*p))
        pygame.draw.rect(background,"black",Rect(x+p,y+3*p,p,p)) 

    elif value == 0 :
        pygame.draw.rect(background,(155,217,234),Rect(x,y,7*p,7*p))
        pygame.draw.rect(background,"black",Rect(x+2*p,y+p,3*p,p))
        pygame.draw.rect(background,"black",Rect(x+2*p,y+2*p,p,4*p))
        pygame.draw.rect(background,"black",Rect(x+4*p,y+2*p,p,4*p))
        pygame.draw.rect(background,"black",Rect(x+3*p,y+5*p,2*p,p))

    elif value == 1:
        pygame.draw.rect(background,(168,230,29),Rect(x,y,7*p,7*p))
        pygame.draw.rect(background,"black",Rect(x+2*p,y+p,p,p))
        pygame.draw.rect(background,"black",Rect(x+3*p,y+p,p,5*p)) 

    elif value ==2 :
        pygame.draw.rect(background,(168,230,29),Rect(x,y,7*p,7*p))   
        pygame.draw.rect(background,"black",Rect(x+2*p,y+p,3*p,p))
        pygame.draw.rect(background,"black",Rect(x+4*p,y+2*p,p,p)) 
        pygame.draw.rect(background,"black",Rect(x+2*p,y+3*p,3*p,p))
        pygame.draw.rect(background,"black",Rect(x+2*p,y+4*p,p,p))
        pygame.draw.rect(background,"black",Rect(x+2*p,y+5*p,3*p,p))
  
    elif value == 3 :
        pygame.draw.rect(background,(168,230,29),Rect(x,y,7*p,7*p))    
        pygame.draw.rect(background,"black",Rect(x+2*p,y+p,3*p,p))
        pygame.draw.rect(background,"black",Rect(x+4*p,y+2*p,p,p)) 
        pygame.draw.rect(background,"black",Rect(x+2*p,y+3*p,3*p,p))
        pygame.draw.rect(background,"black",Rect(x+4*p,y+4*p,p,p))
        pygame.draw.rect(background,"black",Rect(x+2*p,y+5*p,3*p,p))
    
    elif value == 4:
        pygame.draw.rect(background,(168,230,29),Rect(x,y,7*p,7*p))    
        pygame.draw.rect(background,"black",Rect(x+2*p,y+p,p,3*p))
        pygame.draw.rect(background,"black",Rect(x+4*p,y+p,p,5*p)) 
        pygame.draw.rect(background,"black",Rect(x+3*p,y+3*p,p,p))
    
    elif value == 5:
        pygame.draw.rect(background,(255,242,0),Rect(x,y,7*p,7*p))   
        pygame.draw.rect(background,"black",Rect(x+2*p,y+p,3*p,p))
        pygame.draw.rect(background,"black",Rect(x+2*p,y+2*p,p,p)) 
        pygame.draw.rect(background,"black",Rect(x+2*p,y+3*p,3*p,p))
        pygame.draw.rect(background,"black",Rect(x+4*p,y+4*p,p,p))
        pygame.draw.rect(background,"black",Rect(x+2*p,y+5*p,3*p,p))

    elif value == 6:
        pygame.draw.rect(background,(255,242,0),Rect(x,y,7*p,7*p))   
        pygame.draw.rect(background,"black",Rect(x+2*p,y+p,3*p,p))
        pygame.draw.rect(background,"black",Rect(x+2*p,y+2*p,p,4*p)) 
        pygame.draw.rect(background,"black",Rect(x+2*p,y+3*p,3*p,p))
        pygame.draw.rect(background,"black",Rect(x+4*p,y+4*p,p,p))
        pygame.draw.rect(background,"black",Rect(x+2*p,y+5*p,3*p,p))

    elif value == 7 :
        pygame.draw.rect(background,(255,242,0),Rect(x,y,7*p,7*p))   
        pygame.draw.rect(background,"black",Rect(x+2*p,y+p,3*p,p))
        pygame.draw.rect(background,"black",Rect(x+4*p,y+2*p,p,4*p)) 

    elif value == 8 :
        pygame.draw.rect(background,(255,242,0),Rect(x,y,7*p,7*p))   
        pygame.draw.rect(background,"black",Rect(x+2*p,y+p,3*p,p))
        pygame.draw.rect(background,"black",Rect(x+2*p,y+2*p,p,4*p)) 
        pygame.draw.rect(background,"black",Rect(x+2*p,y+3*p,3*p,p))
        pygame.draw.rect(background,"black",Rect(x+4*p,y+2*p,p,4*p))
        pygame.draw.rect(background,"black",Rect(x+2*p,y+5*p,3*p,p))

    elif value == 9 :
        pygame.draw.rect(background,(237,28,36),Rect(x,y,7*p,7*p))   
        pygame.draw.rect(background,"black",Rect(x+2*p,y+p,3*p,p))
        pygame.draw.rect(background,"black",Rect(x+2*p,y+2*p,p,p)) 
        pygame.draw.rect(background,"black",Rect(x+2*p,y+3*p,3*p,p))
        pygame.draw.rect(background,"black",Rect(x+4*p,y+2*p,p,4*p))
        pygame.draw.rect(background,"black",Rect(x+2*p,y+5*p,3*p,p))

    elif value == 10 :
        pygame.draw.rect(background,(237,28,36),Rect(x,y,7*p,7*p))   
        pygame.draw.rect(background,"black",Rect(x+p,y+p,p,5*p))
        pygame.draw.rect(background,"black",Rect(x+3*p,y+p,3*p,p))
        pygame.draw.rect(background,"black",Rect(x+3*p,y+2*p,p,4*p))
        pygame.draw.rect(background,"black",Rect(x+5*p,y+2*p,p,4*p))
        pygame.draw.rect(background,"black",Rect(x+4*p,y+5*p,2*p,p))

    elif value == 11 :
        pygame.draw.rect(background,(237,28,36),Rect(x,y,7*p,7*p))   
        pygame.draw.rect(background,"black",Rect(x+2*p,y+p,p,5*p))
        pygame.draw.rect(background,"black",Rect(x+4*p,y+p,p,5*p))

    elif value == 12 :
        pygame.draw.rect(background,(237,28,36),Rect(x,y,7*p,7*p))   
        pygame.draw.rect(background,"black",Rect(x+p,y+p,p,5*p))    
        pygame.draw.rect(background,"black",Rect(x+3*p,y+p,3*p,p))
        pygame.draw.rect(background,"black",Rect(x+5*p,y+2*p,p,p)) 
        pygame.draw.rect(background,"black",Rect(x+3*p,y+3*p,3*p,p))
        pygame.draw.rect(background,"black",Rect(x+3*p,y+4*p,p,p))
        pygame.draw.rect(background,"black",Rect(x+3*p,y+5*p,3*p,p))

    elif value == 66:
        pygame.draw.rect(background,(47,54,155),Rect(x,y,2*p,2*p))    
        pygame.draw.rect(background,(112,154,209),Rect(x+2*p,y,p,2*p))  
        pygame.draw.rect(background,(155,217,234),Rect(x+3*p,y,p,2*p)) 
        pygame.draw.rect(background,(30,230,106),Rect(x+4*p,y,p,2*p))
        pygame.draw.rect(background,(168,230,29),Rect(x+5*p,y,2*p,2*p))

        pygame.draw.rect(background,(255,163,177),Rect(x,y+2*p,2*p,2*p))
        pygame.draw.rect(background,(153,0,48),Rect(x+2*p,y+2*p,p,2*p))
        pygame.draw.rect(background,(237,28,36),Rect(x+3*p,y+2*p,2*p,2*p))   
        pygame.draw.rect(background,(255,242,0),Rect(x+5*p,y+2*p,2*p,2*p))

        pygame.draw.rect(background,(255,242,0),Rect(x,y+4*p,2*p,p))        
        pygame.draw.rect(background,(237,28,36),Rect(x+2*p,y+4*p,2*p,p))
        pygame.draw.rect(background,(153,0,48),Rect(x+4*p,y+4*p,p,p))
        pygame.draw.rect(background,(255,165,177),Rect(x+5*p,y+4*p,2*p,p))

        pygame.draw.rect(background,(168,230,29),Rect(x,y+5*p,2*p,2*p))  
        pygame.draw.rect(background,(30,230,106),Rect(x+2*p,y+5*p,p,2*p)) 
        pygame.draw.rect(background,(155,217,234),Rect(x+3*p,y+5*p,p,2*p)) 
        pygame.draw.rect(background,(112,154,209),Rect(x+4*p,y+5*p,p,2*p))
        pygame.draw.rect(background,(47,54,153),Rect(x+5*p,y+5*p,2*p,2*p)) 
    
    else :
        pygame.draw.rect(background,"white",Rect(x,y,7*p,7*p))
    
    screen.blit(background, (0, 0))
    pygame.display.flip()



def indicateur(n_joueur,background,screen,p):
    if n_joueur == 0 :
        pygame.draw.rect(background,"red",Rect(500-18*p,1000-27*p,p,27*p)) 
        pygame.draw.rect(background,"red",Rect(500-18*p,1000-27*p,36*p,p)) 
        pygame.draw.rect(background,"red",Rect(500+17*p,1000-27*p,p,27*p))
    elif n_joueur == 1 :
        pygame.draw.rect(background,"red",Rect(0,500-18*p,27*p,p)) 
        pygame.draw.rect(background,"red",Rect(27*p,500-18*p,p,36*p)) 
        pygame.draw.rect(background,"red",Rect(0,500+17*p,27*p,p))
    elif n_joueur == 2 :
        pygame.draw.rect(background,"red",Rect(500-18*p,0,p,27*p)) 
        pygame.draw.rect(background,"red",Rect(500-18*p,27*p,36*p,p)) 
        pygame.draw.rect(background,"red",Rect(500+17*p,0,p,27*p))
    elif n_joueur ==3 : 
        pygame.draw.rect(background,"red",Rect(1000-27*p,500-18*p,27*p,p)) 
        pygame.draw.rect(background,"red",Rect(1000-27*p,500-18*p,p,36*p)) 
        pygame.draw.rect(background,"red",Rect(1000-27*p,500+18*p,27*p,p))

    screen.blit(background, (0, 0))
    pygame.display.flip()

def cancel_indicateur(n_joueur,background,screen,p):
    if n_joueur == 0 :
        pygame.draw.rect(background,"white",Rect(500-18*p,1000-27*p,p,27*p)) 
        pygame.draw.rect(background,"white",Rect(500-18*p,1000-27*p,36*p,p)) 
        pygame.draw.rect(background,"white",Rect(500+17*p,1000-27*p,p,27*p))
    elif n_joueur == 1 :
        pygame.draw.rect(background,"white",Rect(0,500-18*p,27*p,p)) 
        pygame.draw.rect(background,"white",Rect(27*p,500-18*p,p,36*p)) 
        pygame.draw.rect(background,"white",Rect(0,500+17*p,27*p,p))
    elif n_joueur == 2 :
        pygame.draw.rect(background,"white",Rect(500-18*p,0,p,27*p)) 
        pygame.draw.rect(background,"white",Rect(500-18*p,27*p,36*p,p)) 
        pygame.draw.rect(background,"white",Rect(500+17*p,0,p,27*p))
    elif n_joueur ==3 : 
        pygame.draw.rect(background,"white",Rect(1000-27*p,500-18*p,27*p,p)) 
        pygame.draw.rect(background,"white",Rect(1000-27*p,500-18*p,p,36*p)) 
        pygame.draw.rect(background,"white",Rect(1000-27*p,500+18*p,27*p,p))

    screen.blit(background, (0, 0))
    pygame.display.flip()

