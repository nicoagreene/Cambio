
#I think it might make sense to have different classes for my player vs the bots 
class Player: 
    name = ""
    hand = []
#    card3   card4
#    card1   card2
    def __init__(self, name):
        self.hand = []
        self.name = name

    
    def recieveCard(self, card):
        self.hand.append(card)

    def draw(self, card):
        return card

    def discard(self, card):
        return card

    def stack(self, position):
        return self.hand.getCard(position)

    def handValue(self):
        value = 0
        for card in self.hand:
            value += card.getValue()
        return value

    def getHandSize(self):
        return len(self.hand)

    def toString(self):
        return self.name

    def cardsLeftString(self):
        cardsLeft = ""
        for i in range(len(self.hand)):
            cardsLeft += f" {i},"
        return cardsLeft

    
    def handToString(self):
        string = ""
        for i in range(len(self.hand)):
            string += f"\nCard {str(i)} is {self.hand[i].toString()}"
        return string

    def getCard(self, cardLocation):
        if len(self.hand) < cardLocation:
            return None
        else:
            return self.hand[cardLocation]

    def setCard(self, cardLocation, newCard): #swaps a card and return the old card
        if len(self.hand) < cardLocation:
            print("location out of bounds")
        else:
            oldCard = self.hand[cardLocation]
            self.hand[cardLocation] = newCard
            return oldCard
    #player and hand classes might need to be consolidated into one