import random

class player():
    def __init__(self):
        self.name = ""
        self.isLiberal = False
        self.isChancellor = False
        self.isPresident = False
        self.isDead = False

class liberal(player):
    def __init__(self):
        self.IsLiberal = True
        

class fascist(player):
    def __init__(self):
        self.isHitler = False

class hitler(fascist):
    def __init__(self):
        self.isHitler = True

class gameDeck():

    def __init__(self):
        self.deck = []
        self.deck.extend(['liberal']*6)
        self.deck.extend(['fascist']*11)
        random.shuffle(self.deck)

    def draw(self):
        return self.deck.pop()

class game():
    def __init__(self):
        self.deck = gameDeck()
        self.players = []
        self.loby = []

    def addPlayer(self, player):
        self.players.append(player)

    def addPlayerToLoby(self, name):
        self.loby.append(name)

    def prepareRoles(self, playerCount):
        fascistCount = 1
        if playerCount >= 7:
            fascistCount +=1
        if playerCount >= 9:
            fascistCount +=1
        
        roles = ['H']
        roles.extend(['F']*fascistCount)
        roles.extend(['L']*(playerCount - len(roles)))
        random.shuffle(roles)
        return roles



        

