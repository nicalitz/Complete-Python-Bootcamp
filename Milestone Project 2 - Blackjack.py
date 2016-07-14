from __future__ import print_function
import itertools,random

class Player(object):
    def __init__(self,money):
        self.money = money

    def bet(self,amount):
        self.money -= amount

    def winnings(self,amount):
        self.money += amount


class Deck(object):
    def __init__(self):
        self.suits = ['Diamonds','Clubs','Hearts','Spades']
        self.deck = list(itertools.product(range(2,11)+['Jack','Queen','King','Ace'],self.suits))

    def shuffle(self):
        print('Dealer is shuffling the cards...')
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()

class Hand(object):
    def __init__(self):
        self.cards = []

    def score(self):
        sum = 0
        ace_count = 0
        for card in self.cards:
            if isinstance(card[0],int):
                sum += int(card[0])
            elif card[0] in ['Jack','Queen','King']:
                sum += 10
            else:
                ace_count += 1
                sum += 11
        while sum > 21:
            if ace_count > 0:
                sum -= 10
                ace_count -= 1
                continue
            break
        return sum

    def draw_card(self,card):
        self.cards += card

    def dealer_score(self):
        if self.score() >= 17:
            return True
        else:
            return False

def game():
    player = Player(400)

    while True:
        bet_amount = 0
        print('You have',player.money)
        while True:
            bet_amount = raw_input('How much would you like to bet? ')
            try:
                bet_amount = int(bet_amount)
                break
            except:
                print('Please enter a numerical value')
        player.bet(bet_amount)

        game_result = None

        new_deck = Deck()
        new_deck.shuffle()

        player_hand = Hand()
        dealer_hand = Hand()

        print('Cards are dealt...')
        for i in (1,2):
            player_hand.draw_card([new_deck.deck.pop()])
            dealer_hand.draw_card([new_deck.deck.pop()])

        show_hands(player_hand,dealer_hand)

        while True:
            add_card = raw_input("Would you like another card? (y/n) ")

            if add_card == 'y':
                player_hand.draw_card([new_deck.deck.pop()])
                show_hands(player_hand,dealer_hand)
                if player_hand.score() > 21:
                    print('You are bust! Dealer wins')
                    game_result = -1
                    break
                elif len(player_hand.cards) >= 5:
                    print('Monkey! You win')
                    game_result = 1
                    break
            elif add_card == 'n':
                break
            else:
                print('Not a valid entry')

        if game_result != -1:
            while not dealer_hand.dealer_score():
                dealer_hand.draw_card([new_deck.deck.pop()])

            game_result = results(player_hand,dealer_hand,bet_amount)

        if game_result == 1:
            player.winnings(2*bet_amount)
        if game_result == 0:
            player.winnings(bet_amount)

        print('You have',player.money,end='\n\n')


        new_game = raw_input('Would you like to play another game? (y/n)' )
        if new_game == 'y':
            continue
        else:
            print('You ended up with',player.money)
            break


def results(player_hand,dealer_hand,bet_amount):
    print('')
    print('Your score:',player_hand.score())
    print('Dealer score:',dealer_hand.score())
    if (dealer_hand.score() > 21):
        print('Dealer is bust. You win',2*bet_amount)
        return 1
    elif (player_hand.score() > dealer_hand.score()):
        print('You win',2*bet_amount)
        return 1
    elif (player_hand.score() < dealer_hand.score()):
        print('You lose')
        return -1
    else:
        print('Tie game')
        return 0


def show_hands(player_hand,dealer_hand):
    print('')
    print('You have: ',player_hand.cards,'which adds up to',player_hand.score())
    print('The dealer has: ',dealer_hand.cards[0])

if __name__ == '__main__':
    game()