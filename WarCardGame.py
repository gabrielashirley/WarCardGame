#WarCardGame
import random

# initialize array of all cards
arrayOfCards = list(range(52))

# shuffle the cards
random.shuffle(arrayOfCards)

# split the cards for 2 players
player1 = arrayOfCards[0:26]
player2 = arrayOfCards[26:]

# function
def warCardGame(player1, player2, stack):
    # case when player 1 runs out of card, last card plays
    if len(player1) < 4:
        lastCard1 = player1[-1]
        one2, two2, three2, four2, *player2 = player2

        # integer division by 4 where 0-3 represent 2, 4-7 represent 3, and so on until 51-54 represent A
        if lastCard1 // 4 > four2 // 4:
            player1.extend([one2, two2, three2, four2] + stack)
            return player1, player2
            
        else:
            print('Player 2 wins')
            return [], player2

    # case when player 2 runs out of card, last card plays
    elif len(player2) < 4:
        lastCard2 = player2[-1]
        one1, two1, three1, four1, *player1 = player1

        if lastCard2 // 4 > four1 // 4:
            player2.extend([one1, two1, three1, four1] + stack)
            return player1, player2

        else:
            print('Player 1 wins')
            return player1, []
    
    else:
        one1, two1, three1, four1, *player1 = player1
        one2, two2, three2, four2, *player2 = player2

        # Renew the stack
        stack.extend([one1, one2, two1, two2, three1, three2, four1, four2])
        
        # Fourth card revealed, compared
        if four1 // 4 > four2 // 4:
            # if player 1 >, player 1 stacks both cards to his deck
            player1.extend(stack)

        elif four1 // 4 < four2 // 4:
            # if player 2 >, player 2 stacks both cards to his deck
            player2.extend(stack)

        else:
            player1, player2 = warCardGame(player1, player2, stack)

        return player1, player2
    
# loop while player1 and player2 have cards
while player1 and player2: 
    # reveal top of the deck of each player
    head1, *player1 = player1
    head2, *player2 = player2

    # initialize stack
    stack = [head1, head2]
    
    # compare head of each
    # integer division by 4 where 0-3 represent 2, 4-7 represent 3, and so on until 51-54 represent A
    if head1 // 4 > head2 // 4:
        # if player 1 >, player 1 stacks both cards to his deck
        player1.extend(stack)

    elif head1 // 4 < head2 // 4:
        # if player 2 >, player 2 stacks both cards to his deck
        player2.extend(stack)

    else:
        # this is when the war happens
        player1, player2 = warCardGame(player1, player2, stack)

    print("Player 1: ", player1)
    print("Player 2: ", player2)

# end of game case
if player1 and not player2:
    print('Player 1 wins')
elif player2 and not player1:
    print('Player 2 wins')    