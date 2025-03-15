from gameLogic.Card import Card
import random
class Deck:
    defaultDeckStrings = ['jk', 'jk', 'AH', 'AD', 'AS', 'AC', '2H', '2D', '2S', '2C','3H', '3D', '3S', '3C', '4H', '4D', '4S', '4C',
    '5H', '5D', '5S', '5C', '6H', '6D', '6S', '6C','7H', '7D', '7S', '7C','8H', '8D', '8S', '8C', '9H', '9D', '9S', '9C',
    'TH', 'TD', 'TS', 'TC', 'JH', 'JD', 'JS', 'JC', 'QH', 'QD', 'QS', 'QC', 'KH', 'KD', 'KS', 'KC' ]
    defaultDeckCards = []
    for element in defaultDeckStrings:
        cardObject = Card(element)
        defaultDeckCards.append(cardObject)
    

    def __init__(self, deck = defaultDeckCards, discard = []):
        self.deck = deck #list of Card objects
        self.discard = discard #list of card objects 

    
    def shuffle(self): #gotta figure this out once I'm done 
        random.shuffle(self.deck)
    def getDeck(self):
        return self.deck
    def getDiscard(self):
        return self.discard

    def deckToString(self):
        deckStrings = []
        for element in self.deck:
            deckStrings.append(element.toString())
        return deckStrings

    def discardToString(self):#gotta debug this w/ gpt for some reason its not working 
        discardStrings = []
        for element in self.discard:
            discardStrings.append(element.toString())
        return discardStrings
    
    def removeTop(self): #removes top and returns it -- should I just call this draw?
        top = self.deck[0]
        del self.deck[0]
        self.addToDiscard(top)
        return top 

    def addToDiscard(self, card):
        self.discard.append(card)

    def reshuffle(self): # if cards run out reshuffle discard into new deck
        for element in self.discard:
            self.deck.append(element)
        self.shuffle()
        self.discard = []

    def getTop(self):
        return self.deck[1]

        

