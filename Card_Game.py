import random

class Card(object):
    
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit
        
    def __str__(self):
        print('{} of {}'.format(self.value, self.suit))
        
class Deck(object):
    
    def __init__(self):
        self.cards = []
        self.set_up()
    
    def set_up(self):
        for s in ['clubs ♣', 'diamonds ♦', 'hearts ♥' , 'spades ♠']:
            for v in ['ace',2,3,4,5,6,7,8,9,10,'jack','queen','king']:
              self.cards.append(Card(v,s))
    
    def __str__(self):
        for card in self.cards:
            card.__str__()  
    
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
        for i in p.cards:
            i.__str__()
    
    def add_card(self,deck):
        self.cards.append(deck.draw())
    
    
d = Deck()
d.shuffle()
p = Player('Lama')
p.add_card(d)
p.add_card(d)
p.__str__()