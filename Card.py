class Card:
    def __init__(self, card):
        self.card = card    

    def toString(self):
        return self.card
    
    def getValue(self):
        if self.card[0]  == 'j':
            return 0 
        if self.card[0] == 'A':
            return 1
        if self.card[0] == 'K':
            if self.card[1] == 'H' or self.card[1] == 'D':
                return -1
        if self.card[0] in ['2','3','4','5','6','7','8','9']:
            return int(self.card[0])
        else:
            return 10
    def getPower(self): #might have to change this up a little for actual implementation
        if self.hasPower() == False:
            return "This card has no power"
        if self.card[0] == '7' or self.card[0] == '8':
            return 'Look at your own card'
        if self.card[0] == '9' or self.card[0] == 'T':
            return "Look at someone else's card"
        if self.card[0] == 'J' or self.card[0] == 'Q':
            return "Blind swap any two cards"
        else: #only card left is black king
            return "Look at any card and then choose to swap any two cards"
    
    def hasPower(self):
        if self.getValue() >= 7:
            return True
        else:
            return False