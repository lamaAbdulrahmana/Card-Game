import random
from operator import attrgetter

class IncorrectChoiceError(Exception):
    "Please enter a correct choice from the menu."
    pass
class IncorrectPlayersNumberError(Exception):
    "players must be at least 2"
    pass
class Card(object):
    
    def __init__(self,value,suit,card_score,suit_score):
        self.value = value
        self.suit = suit
        self.card_score = card_score
        self.suit_score = suit_score
        
    def __str__(self):
        return '{} {}'.format(self.value, self.suit)
    
    def __repr__(self) -> str:
        print('{} {}'.format(self.value, self.suit))  
     
    def __lt__(self, c2):
        if self.card_score < c2.card_score:
            return True
        else:
            if self.card_score == c2.card_score:
                if self.suit_score < c2.suit_score:
                    return True
        return False

    def __gt__(self, c2):
        if self.card_score > c2.card_score:
            return True
        else:
            if self.card_score == c2.card_score:
                if self.suit_score > c2.suit_score:
                    return True
        return False
     
        
class Deck(object):
    
    def __init__(self):
        self.cards = []
        self.set_up()
    
    def set_up(self):
        suit_score = 4
        for s in ['♠','♥','♦','♣']: # Alphabetical order: clubs (lowest), followed by diamonds, hearts, and spades (highest). 
            card_score = 13
            for v in ['A','K','Q','J','10','9','8','7','6','5','4','3','2']:
                self.cards.append(Card(v,s,card_score,suit_score))
                card_score-=1
            suit_score-=1
        self.shuffle()

    def __str__(self):
        for card in self.cards:
            card.__str__()
    
    def __len__(self):
        return len(self.cards)  
    
    def shuffle(self):
        random.shuffle(self.cards)
        
    def draw(self):
        return self.cards.pop()
        

class Player(object):
    
    def __init__(self,name):
        self.name = name
        self.cards = []
        self.wins = 0
    
    def __str__(self):
        print('My name is {}, I have {} wins'.format(self.name,self.wins))
        
    def add_card(self,deck):
        return self.cards.append(deck.draw())
    
    def round_winner(self):
        self.wins += 1 

 
 
class Game(object):
    
    def __init__(self,deck):
        self.deck = deck
    
    def play_game(self):
        print('Welcome to the card game ♠♥♦♣ created by lama')
        players_numbers = int(input('Enter numbers of players: '))
        players = []
        for number in range(players_numbers):
            name = str(input('Please enter player {} name: '.format(number+1)))
            p = Player(name)
            players.append(p)
        choice = 1
        for round in range(int(52/len(players))):
            if (choice == 1):
                print('''Choose an option to play or quit:
                1. draw card
                2. quit game''')
                choice = int(input('Choose an option: '))
                for player in players:
                    player.add_card(self.deck)
                    print('{} has pulled {}'.format(player.name,player.cards[0].__str__()))
                played_cards = []
                for player in players:
                    played_cards.append(player.cards.pop())
                winner_card = max(played_cards)
                round_winner = players[played_cards.index(winner_card)]
                round_winner.round_winner()
                print('{} won round # {}'.format(round_winner.name,round+1))
            else:
                print('you choose to quit the game bye')
                break
        winner = max(players, key=attrgetter('wins'))
        print('The winner is {} with {} wins HORAY'.format(winner.name, winner.wins)) 
        
             
deck = Deck()       
game = Game(deck)
game.play_game()              
# d.shuffle()
# d.__str__()
# print(len(d.cards))
# p = Player('Lama')
# p.draw_card(d).draw_card(d).draw_card(d)
# p.__str__()
