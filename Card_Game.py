import random

class IncorrectChoiceError(Exception):
    "Please enter a correct choice from the menu."
    pass
class Card(object):
    
    def __init__(self,value,suit,score):
        self.value = value
        self.suit = suit
        self.score = score
        
    def __str__(self):
        print('{} of {}'.format(self.value, self.suit))
        
class Deck(object):
    
    def __init__(self):
        self.cards = []
        self.set_up()
    
    def set_up(self):
        i = 4
        for s in ['spades ♠','hearts ♥','diamonds ♦','clubs ♣' ]: # Alphabetical order: clubs (lowest), followed by diamonds, hearts, and spades (highest). 
            score = 13*i
            for v in ['ace','king','queen','jack','2','3','4','5','6','7','8','9','10']:
                self.cards.append(Card(v,s,score))
                score-=1
            i-=1
    
    def __str__(self):
        for card in self.cards:
            card.__str__()  
    
    def shuffle(self):
        random.shuffle(self.cards)
        
    def draw(self):
        self.shuffle()
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
    
    def draw_card(self,deck):
        self.cards.append(deck.draw())
        return self # return self so you can always call method without an object ex: instead of obj.func() then obj.func() i can do obj.func().func() instead
    
    def discard_card(self):
        return self.cards.pop()
 
 
class Game(object):
    
    def __init__(self,deck,players):
        self.deck = deck
        self.players = players
    
    # def turn_winner(self):
    #     max = []
    #     for player in self.players:
    #         for card in player.cards:
    #             max.append(card.score)
        
    #     return (self.players.)
    
    def play_game(self,player):
        players_turn = []
        print('''It's {} turn, Please enter a choice from the menu:
                1.draw
                2.quit '''.format(player.name))
        choice = 1
        while(len(self.deck) > 0):
            while(choice != 2):
                try:
                    choice = int(input('Choice: '))
                    if choice > 2:
                        raise IncorrectChoiceError
                    players_turn.append(player.draw_card(self.deck))
                except ValueError:
                    print('Please enter a valid intger choice.')
                    continue
                except IncorrectChoiceError:
                    print("Please enter a correct choice from the menu.")
                    continue
            self.turn_winner(players_turn)
        print('The war is over!')    
    
    def turn_winner(players_card): # get the player with highest score in a turn
            return max(players_card)
    
    def play_game(self):
        
        while(len(self.deck.cards) > 0):
            for player in self.players:
                print('''It's {} turn, Please enter a choice from the menu:
                1.draw
                2.quit '''.format(player.name))
                choice = 5
                while(choice != 2):
                    try:
                        choice = int(input('Choice: '))
                        if choice > 2:
                            raise IncorrectChoiceError
                        player.draw_card(self.deck)
                    except ValueError:
                        print('Please enter a valid intger choice.')
                        continue
                    except IncorrectChoiceError:
                        print("Please enter a correct choice from the menu.")
                        continue
            # calc winner    
        print("The war is over") # end of while(len(self.deck.cards) > 0) loop       




def main():
    players = []
    try:
        players_number = int(input('''Welcome to the card game ♠♥♦♣ created by lama
                
                Please enter the players number: '''))
    except ValueError:
        print("Please enter a valid intger")
        players_number = int(input('Players number: '))

    for num in players_number:
        try:
            name = str(input('Player #{} please enter your name: '.format(num)))
            player = Player(name)
            players.append(player)
        except ValueError:
            print("Please enter a valid name")
            name = int(input('Players name: '))
            player = Player(name)
            players.append(player)
    
    deck = Deck() # create new deck
    game = Game(deck,players) # create new game with players and deck
    
    while(deck.cards > 0):
        for player in game.players:
            game.play_game(player)
    
    print('The war is over!')    
 
 
main()   
# d = Deck() 
# d.shuffle()
# d.__str__()
# print(len(d.cards))
# p = Player('Lama')
# p.draw_card(d).draw_card(d).draw_card(d)
# p.__str__()
