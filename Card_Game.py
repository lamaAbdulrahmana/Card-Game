import random

class IncorrectChoiceError(Exception):
    "Please enter a correct choice from the menu."
    pass
class IncorrectPlayersNumberError(Exception):
    "players must be at least 2"
    pass
class Card(object):
    
    def __init__(self,value,suit,score):
        self.value = value
        self.suit = suit
        self.score = score
        
    def __str__(self):
        print('{} {}'.format(self.value, self.suit))
        
    def __lt__(self, c2):
        if self.score < c2.score:
            return True
        if self.score == c2.score:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.score > c2.score:
            return True
        if self.score == c2.score:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False
     
        
class Deck(object):
    
    def __init__(self):
        self.cards = []
        self.set_up()
    
    def set_up(self):
        for s in ['♠','♥','♦','♣', ]: # Alphabetical order: clubs (lowest), followed by diamonds, hearts, and spades (highest). 
            score = 13
            for v in ['2','3','4','5','6','7','8','9','10','J','Q','K','A']:
                self.cards.append(Card(v,s,score))
                score-=1
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
        print('My name is {}, I have {} wins and my cards are:'.format(self.name,self.wins))
        for card in self.cards:
            card.__str__()
        
    def add_card(self,deck):
        return self.cards.append(deck.draw())
    
    def round_winner(self):
        self.wins += 1 

 
 
class Game(object):
    
    def __init__(self,deck,players):
        self.deck = deck
        self.players = players
        
            

def main():
    players = []
    print('Welcome to the card game ♠♥♦♣ created by lama')
 
main()   
d = Deck()

p1 = Player('Lama')
p2 = Player('Maha')
p3 = Player('Dana')
p4 = Player('Nouf')

players = [p1,p2,p3,p4]

while len(d.cards)>0:
    for player in players:
        player.add_card(d) 

    
for round in range(int(52/len(players))):
    played_cards = []
    for player in players:
        played_cards.append(player.cards.pop())
    
    for card in played_cards:
        card.__str__()
    maxi = max(played_cards).__str__()
    print('max card is {}'.format(maxi))
    
# d.shuffle()
# d.__str__()
# print(len(d.cards))
# p = Player('Lama')
# p.draw_card(d).draw_card(d).draw_card(d)
# p.__str__()
