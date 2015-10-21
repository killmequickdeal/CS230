""" cardGame.py
    basic card game framework
    keeps track of card locations for as many hands as needed
"""
from random import *

NUMCARDS = 52
DECK = 0
PLAYER = 1
COMP = 2
INPLAY = 3
PDISCARD = 4
CDISCARD = 5


cardLoc = [0] * NUMCARDS
suitName = ("hearts", "diamonds", "spades", "clubs")
rankName = ("Two", "Three", "Four", "Five", "Six", "Seven", 
            "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
playerName = ("deck", "player", "computer", "In Play")

def main():
  clearDeck()
  keepGoing = True
  while keepGoing:
      response = menu()
      clearDeck()
      if response == "1":#runs the function based on response from menu
          for i in range(5):
            assignCard(PLAYER)
            assignCard(COMP)

          showDeck()
          showHand(PLAYER)
          showHand(COMP)
      elif response == "2":
          war()
      elif response == "3":
          print("Haha you think I actually coded that")
      elif response == "0":
          print("Thanks for playing")
          keepGoing = False
      else:
         print ("I don't know what you want to do...") 
    

def clearDeck():#set the location of all cards to the deck
    for i in range(52):
        cardLoc[i] = DECK
        
def assignCard(location):
    keepGoing = True
    while keepGoing:#choose a random card, if it is in the deck then assign it to the specified player
        selected = randint(0,51)
        if cardLoc[selected] == DECK:
            cardLoc[selected] = location
            keepGoing = False

def showDeck():#Show the location of all the cards
    print("""Location of all cards
#         card             location""")
    for i in range(52):
        print("{} {} {}".format(str(i).ljust(5), cardName(i).ljust(20), playerName[cardLoc[i]].ljust(27)))
        
def showHand(user):#show what cards each player has in their hand
    print("Displaying {} hand:".format(playerName[user]))
    cards=0
    for i  in range(52):
        if cardLoc[i] == user:#reference what card it is
            print("{}".format(cardName(i)))

            
        

def cardName(index):#assign card suits and ranks
    suit = index//13#dividing by 13 gives a value between 0 and 3 which represent the 4 suits
    rank = index%13#finding the remaining using % gives a value between 0 and 12 representing the ranks 
    cardSuit = suitName[suit]
    cardRank = rankName[rank]#reference the arrays to find what the integer represents
    result = cardRank + " of " + cardSuit#build the card
    return result

def menu():#gives a menu that lets the user choose a game
    print("""CARD GAME MAIN MENU

0) Quit
1) Main card game
2) War
3) Caravan""")
    response = input("What do you want to do? ")#returns the response to run the correct function
    return response

def war():
    
    PLAYERDECK = 26#set decks to 1/2 a full deck size to start
    COMPDECK = 26
    PLAYERDISCARD = 0#set discard piles so data isn't contaminated by multiple versions of the same card
    COMPDISCARD = 0
    
    for i in range(26):
       assignCard(PLAYER)#assign cards to the players
       assignCard(COMP)
   
    keepGoing = True
    while keepGoing:#menu to decide what to do
        print("""WAR GAME MENU
0)Quit
1)Show Possible Cards
2)Play round""")
        answer = input("What do you want to do? ")
        if answer == "2":
            print("Cards in PLAYERDECK: {}".format(PLAYERDECK))#prints cards in each area
            print("Cards in PLAYERDISCARD: {}".format(PLAYERDISCARD))
            print("Cards in COMPDECK: {}".format(COMPDECK))
            print("Cards in COMPDISCARD: {}".format(COMPDISCARD))
            if PLAYERDECK <= 0:#EVERY instance of this function checks after changing a deck and discard pile size to see if the piles need to be reset
                if PLAYERDISCARD == 0:#if they cannot be reset this means the other player wins
                    print("Computer wins the game")
                PLAYERDECK=PLAYERDISCARD#reset deck from discard
                for i in range(52):
                    if cardLoc[i] == PDISCARD:
                        cardLoc[i] = PLAYER#change correct cards back to deck
                PLAYERDISCARD=0#reset discard
                    
            PLAYERDECK = PLAYERDECK - 1#represent playing a card
            if PLAYERDECK <= 0:
                if PLAYERDISCARD == 0:
                    print("Computer wins the game")
                PLAYERDECK=PLAYERDISCARD
                for i in range(52):
                    if cardLoc[i] == PDISCARD:
                        cardLoc[i] = PLAYER
                PLAYERDISCARD=0
                    
            
            
            playerCard = chooseCard(PLAYER)#choose a card
            cardLoc[playerCard]= INPLAY#puts the card in play so it cannot be chosen again
            baseRankPlayer = playedCard%13#finds the "rank" which is an integer of said card
            if COMPDECK <= 0:
                if COMPDISCARD == 0:
                    print("Player wins the game")
                COMPDECK=COMPDISCARD
                for i in range(52):
                    if cardLoc[i]==CDISCARD:
                        cardLoc[i]=COMP
                COMPDISCARD=0
            COMPDECK = COMPDECK - 1
            if COMPDECK <= 0:
                if COMPDISCARD == 0:
                    print("Player wins the game")
                COMPDECK=COMPDISCARD
                for i in range(52):
                    if cardLoc[i]==CDISCARD:
                        cardLoc[i]=COMP
                COMPDISCARD=0
                
            
            compCard = chooseCard(COMP)
            cardLoc[compCard]=INPLAY
            baseRankComp = playedCard%13
            if baseRankPlayer == baseRankComp:
                PLAYERDECK=PLAYERDECK-1
                if PLAYERDECK <= 0:
                    if PLAYERDISCARD == 0:
                        print("Computer wins the game")
                    for i in range(52):
                        if cardLoc[i]==PDISCARD:
                            cardLoc[i]==PLAYER
                            PLAYERDECK=PLAYERDISCARD
                                    
                PLAYERDECK=PLAYERDECK-1
                if PLAYERDECK <= 0:
                    if PLAYERDISCARD == 0:
                        print("Computer wins the game")
                    for i in range(52):
                        if cardLoc[i]==PDISCARD:
                            cardLoc[i]==PLAYER
                            PLAYERDECK=PLAYERDISCARD
                    PLAYERDISCARD=0
                    
                COMPDECK=COMPDECK-1
                if COMPDECK <= 0:
                    if COMPDISCARD == 0:
                        print("Player wins the game")
                    for i in range(52):
                        if cardLoc[i]==CDISCARD:
                            cardLoc[i]==COMP
                            COMPDECK=COMPDISCARD
                        
                COMPDECK=COMPDECK-1
                if COMPDECK <= 0:
                    if COMPDISCARD == 0:
                        print("Player wins the game")
                    for i in range(52):
                        if cardLoc[i]==CDISCARD:
                            cardLoc[i]==COMP
                            COMPDECK=COMPDISCARD
                    COMPDISCARD=0
                winner =tieFunction(PLAYERDECK,COMPDECK,PLAYERDISCARD,COMPDISCARD)
                if winner ==  PLAYER:#checks for the winner of a tiebreaker,does not account for DOUBLE or higher wars
                    PLAYERDISCARD=PLAYERDISCARD+6
                elif winner == COMP:
                    COMPDISCARD=COMPDISCARD+6
            elif baseRankPlayer > baseRankComp:
                print("Player Wins!")#checks if player wins
                for i in range(52):
                    if cardLoc[i]==INPLAY:#puts both player cards in player discard
                            cardLoc[i]= PDISCARD
                PLAYERDISCARD = PLAYERDISCARD + 2
            elif baseRankPlayer < baseRankComp:
                print("Computer Wins!")
                for i in range(52):#checks if computer wins
                    if cardLoc[i]==INPLAY:#puts both player cards in computer discard
                        cardLoc[i]= CDISCARD
                COMPDISCARD = COMPDISCARD + 2
            else:
                print("error")
        if answer == "1":
            showHand(PLAYER)
            showHand(COMP)#shows the cards that are possiblities
        if answer == "0":
            main()#goes back to main
            keepGoing=False

def tieFunction(PLAYERDECK,COMPDECK,PLAYERDISCARD,COMPDISCARD):#for wars
    faceDownPlayer = chooseCard(PLAYER)#makes a facedown card and puts in play
    cardLoc[faceDownPlayer]= INPLAY
    
    faceUpPlayer = chooseCard(PLAYER)#makes faceup card to face off against computers face up card
    cardLoc[faceUpPlayer]= INPLAY
    baseRankFUP = playedCard%13
    
    faceDownComp = chooseCard(COMP)
    cardLoc[faceDownComp]= INPLAY
    
    faceUpComp = chooseCard(COMP)
    cardLoc[faceUpComp]= INPLAY
    baseRankFUC = playedCard%13
    if baseRankFUP == baseRankFUC:#similar to original war function through checking who won
        tieFunction(PLAYERDECK,COMPDECK,PLAYERDISCARD,COMPDISCARD)
    elif baseRankFUP > baseRankFUC:
        print("Player wins!")
        for i in range(52):
            if cardLoc[i]==INPLAY:
                cardLoc[i]= PDISCARD
        winner = PLAYER
    elif baseRankFUP < baseRankFUC:
        print("Computer wins!")
        for i in range(52):
            if cardLoc[i]==INPLAY:
                cardLoc[i]= CDISCARD
        winner = COMP
    else:
        print("error")
    return winner#returns the winning player
            
def chooseCard(user):#choosing the card which the player will play via a randint and checking if in the players cards
    keepGoing = True
    while keepGoing:
        global playedCard
        playedCard = randint(0,51)
        if cardLoc[playedCard] == user:
            print("the {}'s card is {}".format(playerName[user], cardName(playedCard)))
            return warCardName(playedCard)#finds the integer which will be compared against the other players card
            keepGoing = False
def warCardName(playedCard):
    rank = playedCard%13
    suit = playedCard//13
    rank = rank + suit*13
    return rank
    
main()

