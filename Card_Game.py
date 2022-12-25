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
        self.__value = value
        self.__suit = suit
        self.__card_score = card_score
        self.__suit_score = suit_score
        
    def __str__(self):
        return '{} {}'.format(self.__value, self.__suit)
    
    def __repr__(self) -> str:
        print('{} {}'.format(self.__value, self.__suit))  
     
    def __lt__(self, c2):
        if self.__card_score < c2.__card_score:
            return True
        else:
            if self.__card_score == c2.__card_score:
                if self.__suit_score < c2.__suit_score:
                    return True
        return False

    def __gt__(self, c2):
        if self.__card_score > c2.__card_score:
            return True
        else:
            if self.__card_score == c2.__card_score:
                if self.__suit_score > c2.__suit_score:
                    return True
        return False
    
    def get_value(self):
        return self.__value
    
    def get_suit(self):
        return self.__suit
    
    def get_card_score(self):
        return self.__card_score
    
    def get_suit_score(self):
        return self.__suit_score
        
class Deck(object):
    
    def __init__(self):
        self.__cards = []
        self.set_up()
    
    def set_up(self):
        suit_score = 4
        for s in ['♠','♥','♦','♣']: # Alphabetical order: clubs (lowest), followed by diamonds, hearts, and spades (highest). 
            card_score = 13
            for v in ['A','K','Q','J','10','9','8','7','6','5','4','3','2']:
                self.__cards.append(Card(v,s,card_score,suit_score))
                card_score-=1
            suit_score-=1
        self.shuffle()

    def __str__(self):
        for card in self.__cards:
            card.__str__()
    
    def __len__(self):
        return len(self.__cards)  
    
    def shuffle(self):
        random.shuffle(self.__cards)
        
    def draw(self):
        return self.__cards.pop()
    
    def get_cards(self):
        return self.__cards   

class Player(object):
    
    def __init__(self,name):
        self.__name = name
        self.__cards = []
        self.wins = 0
    
    def __str__(self):
        print('My name is {}, I have {} wins'.format(self.__name,self.__wins))
        
    def add_card(self,deck):
        return self.__cards.append(deck.draw())
    
    def round_winner(self):
        self.wins += 1 
        
    def get_name(self):
        return self.__name
    
    def get_cards(self):
        return self.__cards
 
 
class Game(object):
    
    def __init__(self,deck):
        self.__deck = deck
    
    def get_deck(self):
        return self.__deck
    
    def play_game(self):
        print('Welcome to the card game ♠♥♦♣ created by lama')
        while True:
            try:
                players_numbers = int(input('Enter numbers of players: '))
                if players_numbers <= 1:
                    raise IncorrectPlayersNumberError()
                break
            except ValueError:
                print('Please enter an intger')
            except IncorrectPlayersNumberError:
                print('Please enter a number more than 2, because players must be at least 2')
        players = []
        for number in range(players_numbers):
            while True:
                try:
                    name = str(input('Please enter player {} name: '.format(number+1)))
                    break
                except ValueError:
                    print('Please enter a valid name')
            p = Player(name)
            players.append(p)
            choice = 1
        for round in range(int(52/len(players))):
            if (choice == 1):
                print('''Choose an option to play or quit:
                1. draw card
                2. quit game''')
                while True:
                    try:
                        choice = int(input('Choose an option: '))
                        if (choice > 2):
                            raise IncorrectChoiceError()
                        break
                    except ValueError:
                        print('Please enter an intger')
                    except IncorrectChoiceError:
                        print('Please choose a number from the menu')
                if choice == 2:
                    break
                for player in players:
                    player.add_card(self.__deck)
                    print('{} has pulled {}'.format(player.get_name(),player.get_cards()[0].__str__()))
                played_cards = []
                for player in players:
                    played_cards.append(player.get_cards().pop())
                winner_card = max(played_cards)
                round_winner = players[played_cards.index(winner_card)]
                round_winner.round_winner()
                print('{} won round # {}'.format(round_winner.get_name(),round+1))
            else:
                print('you choose to quit the game bye')
                break
        print('The war is over!')
        winner = max(players, key=attrgetter('wins'))
        print('The winner is {} with {} wins HORAY'.format(winner.get_name(), winner.wins)) 
        
             
deck = Deck()       
game = Game(deck)
game.play_game()              
