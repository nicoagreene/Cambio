from gameLogic.Player import Player
from gameLogic.Deck import Deck
from gameLogic.Bot import Bot


class Game:
    turn = 0 
    cambio = False 
    players = [] #I think just a list is the move. I have toString after all 
    deck = None

    def __init__(self, numPlayers, numBots, names):
        self.turn = 0
        self.cambio = False 
        self.players = []
        for i in range(numPlayers):
            self.players.append(Player(names[i]))
        for i in range(numBots):
            self.players.append(Bot('bum'))
        self.deck = Deck()

   #card orientation function that displays how your cards are layed out 


    def callCambio(self):
        self.cambio = True
        print("Cambio called!")
    
    def nextTurn(self):
        self.turn = (self.turn + 1) % len(self.players) #automatically adds to turn corecting as we go
        print("Next turn!" "It is now " + self.players[self.turn].toString() + "'s turn")

    def reveal(self):
        winner = ""
        bestScore = 1000
        print("Hands revealed:")
        for player in self.players:
            if player.handValue() < bestScore:
                winner = player.toString()
                bestScore = player.handValue()
            print(f"\n\n{player.toString()}'s hand was:")
            print(f"{player.handToString()}")
            print(f"{player.toString()}'s total was {player.handValue()}")

        print(f"The winner is ... {winner} with a score of {bestScore}")
     
    def deal(self):
        print("Shuffling deck...")
        self.deck.shuffle()
        print("Dealing cards...")
        for i in range(len(self.players)):
            for player in self.players:
                player.recieveCard(self.deck.removeTop())
        print("Ready to play")

    # I am printing everything right now but I have to return something for bots at some point
    def yourTurn(self): #gotta update this function to next turn after every possibility 
        currentPlayerS = self.players[self.turn].toString()
        currentPlayer = self.players[self.turn]
        print(f"It's {currentPlayerS}'s turn")
        if isinstance(currentPlayer, Bot):
            currentPlayer.takeTurn(self)
        else:
            cambioOrPlay = input("Would you like to: \n1)Call Cambio \nor\n2)Draw and play\nPlease enter a 1 of a 2:")
            if cambioOrPlay == '1': #if Cambio is already called i dont even need this conditionals
                self.callCambio()
                #every one else play once, then reveal, this is done in reveal
            else:
                drawnCard = self.players[self.turn].draw(self.deck.removeTop())#I dont think draw even  has to be a method in players
                print(f"{currentPlayerS} drew {drawnCard.toString()}")#this should only be for you
                #if len(player[1].getHandSize()) == 0 then automatic cant swap
                swapOrPlay = input("Would you like to: \n1)Swap the card you drew for one in your hand\nor\n2)Play\nPlease enter a 1 of a 2:")
                #maybe add a component of swap and play that doesnt let you swap if you have no cards left 
                if int(swapOrPlay) == 1:
                    positionOldCard = input(f"Which card would you like to swap{currentPlayer.cardsLeftString()}: ")
                    oldCard = currentPlayer.getCard(int(positionOldCard))
                    currentPlayer.setCard(int(positionOldCard), drawnCard)
                    print("Cards switched!")
                    self.deck.addToDiscard(oldCard)
                    print(f"{oldCard.toString()} added to discard ") #how can i make top card of discard public so bots know 
                    
                else: #this if player decides to play drawn card 
                    self.playCard(drawnCard)
    
    def playCard(self, drawnCard):
        currentPlayer = self.players[self.turn]
        if drawnCard.hasPower(): #for all these options also gotta add a option to not play the power 
            if drawnCard.toString()[0] == '7' or drawnCard.toString()[0] == '8':
                playOrNot = input("Would you like to look at your own card or not? enter 1 for yes and 2 for no: ")
                if playOrNot == '1':
                    self.deck.addToDiscard(drawnCard)
                    print(f"{drawnCard.toString()} was added to the discard pile ")
                    cardPeek = input(f"You can look at one of your own cards!\nWhich card would you like to look at{currentPlayer.cardsLeftString()}")
                    print(f"The card at {cardPeek} position is {currentPlayer.getCard(int(cardPeek)).toString()}")
                else:
                    self.deck.addToDiscard(drawnCard)
                    print(f"{drawnCard.toString()} was added to the discard pile ")
            if drawnCard.toString()[0] == '9' or drawnCard.toString()[0] == 'T':
                playOrNot = input("Would you like to look at another persons card or not? enter 1 for yes and 2 for no: ")
                if playOrNot == '1':
                    self.deck.addToDiscard(drawnCard)
                    print(f"{drawnCard.toString()} was added to the discard pile ")
                    nonCurrentPlayers = ""
                    for i in range(len(self.players)):
                        if i != self.turn:
                            nonCurrentPlayers += f"{i}: {self.players[i].toString()}, "
                    playerPeek = input(f"You can look at another player's card!\nWhich player would you like to peek? {nonCurrentPlayers}. Please enter the players number: ")
                    playersCardPeek = input(f"which of their cards would you like to peek? {self.players[int(playerPeek)].cardsLeftString()}")
                    print(f"{self.players[int(playerPeek)].toString()}'s card at position {playersCardPeek} is {self.players[int(playerPeek)].getCard(int(playersCardPeek)).toString()}" )
                else:
                    self.deck.addToDiscard(drawnCard)
                    print(f"{drawnCard.toString()} was added to the discard pile ") 
            currentPlayers = ""
            for i in range(len(self.players)):
                currentPlayers += f"{i}) {self.players[i].toString()}, "   
            if drawnCard.toString()[0] == 'J' or drawnCard.toString()[0] == 'Q':
                playOrNot = input("Would you like to play this blind swap or not? enter 1 for yes and 2 for no: ")
                if playOrNot == '1':
                    self.deck.addToDiscard(drawnCard)
                    print(f"{drawnCard.toString()} was added to the discard pile ")
                    playerSwap1 = input(f"Who is the first player you would like to swap? It does not matter who is the first and who is the seconds player. {currentPlayers}")#somehow gotta include that you are player 1
                    player1Card = input(f"Which one of {self.players[int(playerSwap1)].toString()} card's would you like to swap? {self.players[int(playerSwap1)].cardsLeftString()}")
                    playerSwap2 = input(f"Who is the second player you would like to swap? {currentPlayers}")
                    player2Card = input(f"Which one of {self.players[int(playerSwap2)].toString()} card's would you like to swap? {self.players[int(playerSwap2)].cardsLeftString()}: ")
                    print("swapping...")
                    player1oldCard = self.players[int(playerSwap1)].getCard(int(player1Card))
                    player2oldCard = self.players[int(playerSwap2)].getCard(int(player2Card))
                    self.players[int(playerSwap1)].setCard(int(player1Card), player2oldCard)
                    self.players[int(playerSwap2)].setCard(int(player2Card), player1oldCard)
                    print(f"{self.players[int(playerSwap1)].toString()} and {self.players[int(playerSwap2)].toString()} cards have been swapped!")
                else:
                    self.deck.addToDiscard(drawnCard)
                    print(f"Not playing...{drawnCard.toString()} was added to the discard pile ")
            elif drawnCard.toString()[0] == 'K': #only card left is black king 
                playOrNot = input("Would you like to use your look swap? enter 1 for yes and 2 for no: ")
                if playOrNot == '1':
                    self.deck.addToDiscard(drawnCard)
                    print(f"{drawnCard.toString()} was added to the discard pile ")
                    playerLook = input(f"Which player would you like to look at: {currentPlayers} ")
                    cardLook = input(f"Which of their cards would you like to look at: {self.players[int(playerLook)].cardsLeftString()}")
                    print(f"{self.players[int(playerLook)].toString()}'s card at {cardLook} is {self.players[int(playerLook)].getCard(cardLook).toString()}")
                    swapOrNot = input("Would you like to swap cards? enter 1 for yes and 2 for no")
                    if swapOrNot == '1':
                        playerSwap1 = input(f"Who is the first player you would like to swap? It does not matter who is the first and who is the seconds player. {currentPlayers}")#somehow gotta include that you are player 1
                        player1CardsLeft = "" #I really gotta do a function for this in player just makes everything so much more readable. 
                        for i in range(self.players[int(playerSwap1)].getHandSize()):
                            player1CardsLeft += f" {i},"
                        player1Card = input(f"Which one of {self.players[int(playerSwap1)].toString()} card's would you like to swap? {player1CardsLeft}")
                        playerSwap2 = input(f"Who is the second player you would like to swap? {currentPlayers}")
                        player2Card = input(f"Which one of {self.players[int(playerSwap2)].toString()} card's would you like to swap? {self.players[int(playerSwap2)].cardsLeftString()}: ")
                        print("swapping...")
                        player1oldCard = self.players[int(playerSwap1)].getCard(int(player1Card))
                        player2oldCard = self.players[int(playerSwap2)].getCard(int(player2Card))
                        self.players[playerSwap1].setCard(int(player1Card), player2oldCard)
                        self.players[playerSwap2].setCard(int(player2Card), player1oldCard)
                        print(f"{self.players[int(playerSwap1)].toString()} and {self.players[int(playerSwap2)].toString()} cards have been swapped!")
                else:
                    self.deck.addToDiscard(drawnCard)
                    print(f"{drawnCard.toString()} was added to the discard pile ")
                    
        else:
                self.deck.addToDiscard(drawnCard)
                print(f"{drawnCard.toString()} was added to the discard pile ")
                
                

    def otherTurn():
        pass


    def getPlayer(self):
        return self.players[0]

    def firstPeek(self):
        you = self.players[0]
        print(f"Your card at the 0 position is {you.getCard(0).toString()}, your card at the 1 position is {you.getCard(3).toString()}.")

    def playGame(self):
        self.deal()
        self.firstPeek()
        while not self.cambio:
            print(f"{self.players[self.turn].toString()} 's turn!")
            self.yourTurn()
            self.nextTurn()
        for i in range(len(self.players) - 1): #after cambio is called everyone should still a get  turn to play 
            self.yourTurn()
            self.nextTurn()
        self.reveal()
            



        
    
        
    

