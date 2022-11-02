from logging import exception
import random

class player:
    def __init__(self, name):
        self.name = name
        self.isLiberal = False
        self.isChancellor = False
        self.isPresident = False
        self.isDead = False

class liberal(player):
    def __init__(self, name):
        player.__init__(self, name)
        self.IsLiberal = True
        

class fascist(player):
    def __init__(self, name):
        player.__init__(self, name)
        self.isHitler = False

class hitler(fascist):
    def __init__(self, name):
        player.__init__(self, name)
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

    def assignRolesToPlayers(self):
        myRoles = self.prepareRoles(len(self.loby))

        for playerName in self.loby:
            thisRole = myRoles.pop()
            self.addPlayer(self.giveRole(playerName, thisRole))

    def giveRole(self, playerName, role):
        match role:
            case 'H':
                self.addPlayer(hitler(playerName))
            case 'F':
                self.addPlayer(fascist(playerName))
            case 'L':
                self.addPlayer(liberal(playerName))
    



        

