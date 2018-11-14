# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    
second_shape = [CARD_BACK_CENTER[0] + CARD_BACK_SIZE[0], CARD_BACK_CENTER[1]]

# initialize some useful global variables
in_play = False
outcome = ""
state = ""
score = 0
middle = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        arr = ''
        for i in range (len(self.cards)):
            arr += str(self.cards[i]) + ' '
        return 'Hand contains '+ arr

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        total = 0
        there_A = False
        for c in self.cards:
            if VALUES[c.get_rank()] == 1:
                there_A = True
            total += VALUES[c.get_rank()]
        
        if not there_A:
            return total
        else:
            if total + 10 <= 21:
                return total + 10
            else:
                return total
   
    def draw(self, canvas, pos):
        pass	# draw a hand on the canvas, use the draw method for cards
        for i in range(len(self.cards)):
            self.cards[i].draw(canvas, [pos[0] + CARD_SIZE[0] * i * 1.2, pos[1]])

 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for s in SUITS:
            for r in RANKS:
                self.deck.append(Card(s, r))
        

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)

    def deal_card(self):
        c = self.deck.pop()
        return c
    
    def __str__(self):
        arr = ''
        for i in range(len(self.deck)):
            arr += str(self.deck[i]) + ' '
        return arr


#define event handlers for buttons
def deal():
    global outcome, in_play, player, dealer, deck_board, state, score, middle

    if in_play and middle > 0:
        state = "You Lose!"
        outcome = "Hit or Stand?"
        score -= 1
        in_play = False
        middle = 0
    else:
        state = ""

    # your code goes here
    deck_board = Deck()
    deck_board.shuffle()
    player = Hand()
    dealer = Hand()
    # add two cards for the player
    player.add_card(deck_board.deal_card())
    player.add_card(deck_board.deal_card())
    # add two cards for the dealer
    dealer.add_card(deck_board.deal_card())
    dealer.add_card(deck_board.deal_card())

    print 'Player '+str(player)
    print 'Dealer '+str(dealer)
    outcome = "Hit or Stand?"
    

    
    
    in_play = True

def hit():
    global outcome, in_play, state, score, middle
    middle += 1
    pass	# replace with your code below

    # if the hand is in play, hit the player
    if in_play and player.get_value() <= 21:
        player.add_card(deck_board.deal_card())
        print 'Player '+str(player)
   
    # if busted, assign a message to outcome, update in_play and score
    if player.get_value() > 21:
        state = "You went bust and lose"
        score -= 1
        outcome = 'New Deal?'
        in_play = False
       
def stand():
    global outcome, score, in_play, state
    in_play = False

    """
    Implement the handler for a "Stand" button.
    If the player has busted, remind the player that they have busted.
    Otherwise, repeatedly hit the dealer until his hand has value 17 or more (using a while loop).
    If the dealer busts, let the player know.
    Otherwise, compare the value of the player's and dealer's hands.
    If the value of the player's hand is less than or equal to the dealer's hand, the dealer wins.
    Otherwise the player has won. Remember the dealer wins ties in our version.
    """
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if player.get_value() > 21: # If the player has busted, remind the player that they have busted.
        state = "You have been busted already!"
    else: # Otherwise, repeatedly hit the dealer until his hand has value 17 or more (using a while loop).
        while dealer.get_value() < 17:
            dealer.add_card(deck_board.deal_card())
            print 'Dealer '+str(dealer)
        if dealer.get_value() > 21: # If the dealer busts, let the player know.
            state = "The dealer has been busted :)"
            outcome = 'New Deal?'
        else: # Otherwise, compare the value of the player's and dealer's hands.
            if player.get_value() <= dealer.get_value(): #If the value of the player's hand is less than or equal to the dealer's hand, the dealer wins.
                state = "You Lose :("
                score -= 1
            else: # Otherwise the player has won. Remember the dealer wins ties in our version.
                state = "You win :)"
                score += 1
            outcome = 'New Deal?'


    # assign a message to outcome, update in_play and score

# draw handler
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Blackjack", [250, 50], 40, "Aqua")
    
    canvas.draw_text("Score : "+str(score), [370, 270], 28, "Yellow")
    canvas.draw_text(state, [230, 200], 28, "White")
    canvas.draw_text(outcome, [230, 450], 28, "White")
    player.draw(canvas, [50, 580 - CARD_SIZE[1]])
    dealer.draw(canvas, [50, 70])
    if in_play:
        canvas.draw_image(card_back, second_shape, CARD_BACK_SIZE, [50 + CARD_BACK_CENTER[0], 70 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric