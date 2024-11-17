import random as rd
import affichages
import pygame

def get_lc(p,x,y):
            if x>=500-3.5 * p and x <= 500+3.5 * p and y>= 500-7.5 *p and y <= 500-0.5*p :
                return (-2,-1,-1)
            elif x>=500-3.5 * p and x <= 500+3.5 * p and y>= 500+0.5 *p and y <= 500+7.5*p :
                return (-1,-1,-1)
            for i in range(3):
                for j in range(4):
                    if x>=p + i*8*p and x <=p+ i*8*p + 7*p and y>=500-15.5*p+j*8*p and y <= 500-15.5*p+j*8*p + 7*p :
                        return (1,i,j)
                    elif x>=500-15.5*p + j*8*p and x <= 500-15.5*p + j*8*p + 7*p and y >= 1000-8*p-i*8*p and y <= 1000-8*p-i*8*p + 7*p :
                        return (0,i,j)
                    elif x>=500-15.5*p + j*8*p and x<= 500-15.5*p + j*8*p +7*p and y>=p+i*8*p and y<= p+i*8*p + 7*p :
                        return (2,i,j)
                    elif x>= 1000 -8*p - i*8*p and x <= 1000 -8*p - i*8*p +7*p and y>=500-15.5*p+j*8*p and y <= 500-15.5*p+j*8*p +7*p :
                        return (3,i,j)
            return (-3,-1,-1)
 
class Carte ():
    def __init__(self,value):
        self.value = value
        self.revealed = False
        self.player = -2
        self.line = -1
        self.column = -1

    def getcoord(self,p):
            if self.player == 0 :
                return (500-15.5*p + self.column*8*p,1000-8*p-self.line*8*p)
            elif self.player == 1:
                return (p + self.line*8*p,500-15.5*p+self.column*8*p)
            elif self.player == 2:
                return (500-15.5*p + self.column*8*p,p+self.line*8*p)
            elif self.player == 3 :
                return (1000 -8*p - self.line*8*p,500-15.5*p+self.column*8*p)
            elif self.player == -2 : ##carte dans la pioche
                return 500-3.5*p,500-7.5*p
            elif self.player == -1:
                return 500-3.5*p,500+0.5*p                    
        
                     
    def afficher(self,p,background,screen):
        if self.revealed :
            (x,y)=self.getcoord(p)
            affichages.afficher_carte(x,y,background,screen,p,self.value)
        else :
            (x,y)=self.getcoord(p)
            affichages.afficher_carte(x,y,background,screen,p)
      
    def reveal(self,p,background,screen,centre = False):
        if centre  :
            self.player = -1
        self.revealed = True
        self.afficher(p,background,screen)

    def attribuer(self,player,i,j,p,background,screen):
        self.player = player
        self.line = i
        self.column = j
        self.afficher(p,background,screen)
        return self

class Player ():
    def __init__(self,bot,id,cards) -> None:
        self.is_a_bot = bot
        self.id = id
        self.cards = cards
        self.revealed = 0
    
    def compter_points(self) :
        count = 0 
        for c in self.cards :
            for k in c:
                if k.revealed :
                    count += k.value
        return count

class Pioche ():
    def __init__(self) -> None:
        tmp = [-2 for i in range(5)]+ [-1 for i in range(10)]+[0 for i in range(15)]\
        +[1 for i in range(10)]+ [2 for i in range(10)]+[3 for i in range(10)]\
            +[4 for i in range(10)]+ [5 for i in range(10)]+[6 for i in range(10)]\
                +[7 for i in range(10)]+ [8 for i in range(10)]+[9 for i in range(10)]\
                    +[10 for i in range(10)]+ [11 for i in range(10)]+[12 for i in range(10)]
        self.pioche = [Carte(c) for c in tmp]
        self.shuffle()


    def shuffle(self):
        rd.shuffle(self.pioche)

    def pick(self,begin=False,i=-1,j=-1,player = -1):
        if begin :
            card= self.pioche.pop()
            card.player = player
            card.line = i
            card.column = j
            return card
        else : ##quand on pioche une carte pendant le jeu dans la pioche
            card= self.pioche.pop()
            card.revealed= True
            return card



class Jeu():
    def __init__(self,nbr_players,nbr_bots) -> None:
        self.pioche = Pioche()
        self.nbr_players = nbr_players
        self.nbr_bots = nbr_bots
        self.players = []
        self.p = 10
        self.centre = Carte(0)
        self.defausse = []
        self.background = -1
        self.screen = -1
        self.distribuer()

    def distribuer(self):
        for n in range(self.nbr_players):
            if n < self.nbr_players - self.nbr_bots :
                l = [[Pioche.pick(self.pioche,True,i,j,n) for j in range(4)] for i in range(3)]
                p = Player(False,n,l)
            else :
                l = [[Pioche.pick(self.pioche,True,i,j,n) for j in range(4)] for i in range(3)]
                p = Player(True,n,l)
            self.players.append(p)
        self.init_plateau()

    def init_plateau(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000,1000))
        pygame.display.set_caption('')

        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill('white')


        for n in range(self.nbr_players):
            for i in range(3):
                for j in range (4):
                    self.players[n].cards[i][j].afficher(self.p,self.background,self.screen)
        
        affichages.afficher_carte(500-3.5*self.p,500-7.5*self.p,self.background,self.screen,self.p)
        self.centre = self.pioche.pick(True)
        self.centre.revealed = True
        self.centre.afficher(self.p,self.background,self.screen)
        self.debut()

    def count_revealed(self):
        count = 0
        for p in self.players :
            count += p.revealed
        return count

    

    def debut(self):
        p=self.p
        while self.count_revealed() < 2*self.nbr_players : 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.MOUSEBUTTONDOWN :
                    (x,y) = pygame.mouse.get_pos()
                    (n,i,j)= get_lc(self.p,x,y)
                    if n>=0 and self.players[n].revealed < 2:
                        if not self.players[n].cards[i][j].revealed :
                            self.players[n].cards[i][j].revealed = True
                            self.players[n].revealed +=1
                            self.players[n].cards[i][j].afficher(p,self.background,self.screen)
        max,max_player= self.players[0].compter_points(), 0 ##A MODIFIER SELON LES VRAIES REGLES
        for i in range(1,self.nbr_players):
            if self.players[i].compter_points()>max : ##RAJOUTER LA CONDITION SUR LES PLUS GROSSES VALEURS
                max, max_player = self.players[i].compter_points(), i
        self.mid_game(max_player)

    def mid_game(self,tour):
        affichages.cancel_indicateur((tour -1)%self.nbr_players,self.background,self.screen,self.p)
        affichages.indicateur(tour,self.background,self.screen,self.p)
        while 1 :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.MOUSEBUTTONDOWN :
                    (x,y) = pygame.mouse.get_pos()
                    (n,i,j)= get_lc(self.p,x,y)
                    if n == -2 :        ##cas ou le joueur appuie sur la pioche
                        current_card = self.pioche.pick(False)
                        current_card.afficher(self.p,self.background,self.screen)
                        while 1 :
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    return
                                if event.type == pygame.MOUSEBUTTONDOWN :
                                    (x,y) = pygame.mouse.get_pos()
                                    (n,i,j)= get_lc(self.p,x,y)
                                    if n == tour :  ##cas ou le joueur appuie sur une de ses cartes
                                        self.centre.player = -3
                                        self.defausse.append(self.centre)
                                        affichages.afficher_carte(500-3.5*self.p,500-7.5*self.p,self.background,self.screen,self.p)
                                        self.centre = self.players[tour].cards[i][j]
                                        self.centre.reveal(self.p,self.background,self.screen,True)
                                        self.players[tour].cards[i][j] = current_card.attribuer(tour,i,j,self.p,self.background,self.screen)
                                        return self.mid_game((tour + 1)%self.nbr_players)
                                    elif n==-1 :        ##cas ou le joueur appuie sur la carte du centre
                                        self.centre.player = -3
                                        self.defausse.append(self.centre)
                                        affichages.afficher_carte(500-3.5*self.p,500-7.5*self.p,self.background,self.screen,self.p)
                                        self.centre = current_card
                                        self.centre.reveal(self.p,self.background,self.screen,True)
                                        while 1 :
                                            for event in pygame.event.get():
                                                if event.type == pygame.QUIT:
                                                    return
                                                if event.type == pygame.MOUSEBUTTONDOWN :
                                                    (x,y) = pygame.mouse.get_pos()
                                                    (n,i,j)= get_lc(self.p,x,y)
                                                    if n==tour and self.players[tour].cards[i][j].revealed == False:
                                                        self.players[tour].cards[i][j].reveal(self.p,self.background,self.screen)
                                                        return self.mid_game((tour+1)%self.nbr_players)
                    elif n == -1 : ##cas ou le joueur appuie sur la carte du centre
                        current_card = self.centre
                        while 1:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    return
                                if event.type == pygame.MOUSEBUTTONDOWN :
                                    (x,y) = pygame.mouse.get_pos()
                                    (n,i,j)= get_lc(self.p,x,y)
                                    if n == tour :##cas ou le joueur appuie sur une de ses cartes
                                        self.centre = self.players[tour].cards[i][j]
                                        self.players[tour].cards[i][j] = current_card.attribuer(tour,i,j,self.p,self.background,self.screen)
                                        self.centre.reveal(self.p,self.background,self.screen,True)
                                        
                                        return self.mid_game((tour + 1)%self.nbr_players)

                        