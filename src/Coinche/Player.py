from .Hand import Hand


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.score = 0
        self.tricksWon = []
        self.cardsInRound = []
        self.team = None
        self.teammate = None

    def addCards(self, cards):
        self.hand.addCards(cards)
        self.hand.updateHand()

    def play(self, card):
        return self.hand.playCard(card)

    def trickWon(self, cards):
        self.cardsInRound += cards

    def removeCard(self, card):
        self.hand.removeCard(card)

    def discardTricks(self):
        self.tricksWon = []

    def resetRound(self):
        self.cardsInRound = []
        self.hand = Hand()
        self.score = 0

    def is_ai(self):
        return False


class RandomPlayer(Player):
    def getRandom(self):
        return self.hand.getRandomCard()


class AIPlayer(Player):
    def is_ai(self):
        return True

    
class Team:
    def __init__(self,team_number, player1, player2):
        self.teamNumber = team_number
        self.player1 = player1
        self.player2 = player2
        self.name = self.player1.name + " " + self.player2.name
        self.score = 0
        self.globalScore = 0
        self.tricksWon = []
        self.cardsInRound = []
        self.cardsInHand = []
        

    def updateRoundScore(self):
        self.score = self.player1.score + self.player2.score
    
    def discardTricks(self):
        self.tricksWon = []

    def resetRoundCards(self):
        self.cardsInRound = []

    def teamScore(self):
        return None
    
    def joinCards(self):
        '''Concatenates cards won by each player of the team during round'''
        self.cardsInRound = self.player1.cardsInRound + self.player2.cardsInRound
        
    def joinHands(self):
        '''Concatenates 16 cards from a team's hands '''
        self.cardsInHand = [c for suit in self.player1.hand.hand for c in suit] + [c for suit in self.player2.hand.hand for c in suit]

        