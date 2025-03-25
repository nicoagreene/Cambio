class Hand:
    def __init__(self, cards):
        self.cards = cards #array of Card objects
        #im imagining cards to be oriented like so
#       card3   card4
#       card1   card2

    def toString(self):
        string = ""
        for i in range(len(self.cards)):
            string += "\nCard " + str(i + 1) + " is " + self.cards[i].toString()
        return string
    
    def getCard(self, cardLocation):
        if len(self.cards) < cardLocation:
            return None
        else:
            return self.cards[cardLocation - 1]


    def setCard(self, cardLocation, newCard): #swaps a card and return the old card
        if len(self.cards) < cardLocation:
            print("location out of bounds")
        else:
            oldCard = self.cards[cardLocation - 1]
            self.cards[cardLocation - 1] = newCard
            return oldCard