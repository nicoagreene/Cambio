from .Player import Player #.player indicates that player is inside same gameLogic module
import random
#edit for new commit
class Bot(Player): #might want to have a player class and then bot class and you class as subclass
    knownCards = [0,0,0,0] # basically if index is an int bot doesnt know it, if its a card object bot does 
    # this is subject to change but should it be card object in list or just string? I think object  
   
    def __init__(self, name, difficulty="easy",):
        super().__init__(name)
        self.difficulty = difficulty
        self.knownCards = [0,0,0,0]
        #should I make something for top of discard?
    
    def firstPeek(self):  #adds first two cards from hand to known
        self.knownCards[0] = self.hand[0]
        self.knownCards[1] = self.hand[1]
    
    def takeTurn(self, game): # to pass in the gfame in game just do "self,"
        if self.difficulty == "easy":
            if random.random() < .1:
                game.callCambio()
            else:
                self.easyBotDrawPlay(game)
        if self.difficulty == "medium":
            pass
        if self.difficulty == "hard":
            pass

    def easyBotDrawPlay(self, game):
        #I think I should be able to replace with just self stuff 
        drawnCard = self.draw(game.deck.removeTop())
        if random.random() < .5: #randomly choose to swap or play
            positionOldCard = random.choice(range(len(self.hand))) #Can i do self.hand here even though it is a subclass ?
            oldCard = self.getCard(int(positionOldCard))
            self.setCard(int(positionOldCard), drawnCard)
            self.knownCards[positionOldCard] = drawnCard
            print(f"{self.name} switched their drawn card for their card {positionOldCard}")
            game.deck.addToDiscard(oldCard)
            print(f"{oldCard.toString()} added to discard ") #how can i make top card of discard public so bots know         
        else: #this if player decides to play drawn card 
            self.easyBotPlayCard(game, drawnCard)

    
    def easyBotPlayCard(self, game, drawnCard):
        if drawnCard.hasPower(): #for all these options also gotta add a option to not play the power 
            if drawnCard.toString()[0] == '7' or drawnCard.toString()[0] == '8':
                if random.random() < .8:
                    game.deck.addToDiscard(drawnCard)
                    print(f"{drawnCard.toString()} was added to the discard pile ")
                    for index, card in enumerate(self.knownCards):
                        if isinstance(card, int):
                            card = self.hand[index] #makes card known
                            print(f"{self.name} peeked at card at position {index}")
                            break
                else:
                    game.deck.addToDiscard(drawnCard)
                    print(f"{drawnCard.toString()} was added to the discard pile ")
            if drawnCard.toString()[0] == '9' or drawnCard.toString()[0] == 'T': # do I have to create tracking for everyone else? I feel like for easy no 
                    game.deck.addToDiscard(drawnCard)
                    print(f"Not playing ... {drawnCard.toString()} was added to the discard pile ") 
            if drawnCard.toString()[0] == 'J' or drawnCard.toString()[0] == 'Q':
                if random.random() < .5:
                    self.deck.addToDiscard(drawnCard)
                    print(f"{drawnCard.toString()} was added to the discard pile ")
                    playerSwap1 = random.choice(range(len(game.players))) # I should probably set up a feature so that you cant choose yourself but for now its fine
                    player1Card = random.choice(range(game.players[playerSwap1].getHandSize()))
                    playerSwap2 = random.choice(range(len(game.players)))
                    player2Card = random.choice(range(game.players[playerSwap1].getHandSize()))
                    print("swapping...")
                    player1oldCard = game.players[playerSwap1].getCard(player1Card)
                    player2oldCard = game.players[playerSwap2].getCard(player2Card)
                    game.players[playerSwap1].setCard(player1Card, player2oldCard)
                    game.players[playerSwap2].setCard(player2Card, player1oldCard)
                    print(f"{game.players[playerSwap1].toString()} and {game.players[playerSwap2].toString()} cards have been swapped!")
                else:
                    game.deck.addToDiscard(drawnCard)
                    print(f"Not playing...{drawnCard.toString()} was added to the discard pile ")
            elif drawnCard.toString()[0] == 'K': #only card left is black king 
                if random.random() < .5:
                    game.deck.addToDiscard(drawnCard)
                    print(f"Playing ... {drawnCard.toString()} was added to the discard pile ")
                    playerLook = random.choice(range(len(game.players)))
                    cardLook = random.choice(range(game.players[playerLook].getHandSize()))
                    opponentCard = game.players[playerLook].getCard(cardLook)
                    if opponentCard.getValue() < 6.3: #LEFT OFF HERE
                        myCardIndex = random.choice(range(len(self.hand)))
                        myCard = self.hand[myCardIndex]
                        print('swapping...')
                        self.setCard(myCardIndex, opponentCard)
                        game.players[playerLook].setCard(cardLook, myCard)
                        print(f"{self.toString()} swapped their {myCardIndex} with {game.players[playerLook].toString()}'s card at {cardLook}")
                else:
                    game.deck.addToDiscard(drawnCard)
                    print(f"Not playing ... {drawnCard.toString()} was added to the discard pile ")
                            
        else:
            game.deck.addToDiscard(drawnCard)
            print(f"Not playing ... {drawnCard.toString()} was added to the discard pile ")

    #
    


                    