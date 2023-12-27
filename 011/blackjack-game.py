#! /usr/bin/env python3

import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()


def get_color_code(name):
    colors = {
        "red": "\033[31m",
        'black': "\033[30m",
        'white_bg': "\033[47m",
        'reset': "\033[0m",
    }
    return colors.get(name)

suit_dict = {
    'hearts': '♥',
    'diamonds': '♦',
    'spades': '♠',
    'clubs': '♣',
}

faces = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

deck_dict = {
    'hearts': [],
    'diamonds': [],
    'spades': [],
    'clubs': [],
}

blackjack_values = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,  # Jack
    'Q': 10,  # Queen
    'K': 10,  # King
    'A': 11   # Ace
}

for suit in deck_dict:
    # suits[suit].append(f"{face}{suit}")
    for face in faces:
        deck_dict[suit].append(f"{face}")

deck = []
for suit in deck_dict:
    for face in deck_dict[suit]:
        # print(f"{suit} {face}")
        if   suit == 'hearts':
            deck.append(f"{face:>2}{suit_dict[suit]}")
        elif suit == 'diamonds':
            deck.append(f"{face:>2}{suit_dict[suit]}")
        elif suit == 'spades':
            deck.append(f"{face:>2}{suit_dict[suit]}")
        elif suit == 'clubs':
            deck.append(f"{face:>2}{suit_dict[suit]}")


# input(f"Fresh Deck: {deck}")

# # Professionals shuffle 7 times! lol
# for _ in range(7):
#     # print(deck) # No peeking...
#     random.shuffle(deck)

def show_deal_card(card_dealt):
    face = card_dealt[:2]
    suit = card_dealt[-1]
    card = """
┌─────────┐ 
│{}       │ 
│         │ 
│    {}    │ 
│         │ 
│      {} │ 
└─────────┘.
""".format(face,suit,face,)
    # print(card)
    return card 

def show_card_facedown(card_dealt):
    card = """
┌─────────┐ 
│ ┌─────┐ │ 
│ │     │ │ 
│ │     │ │ 
│ │     │ │ 
│ └─────┘ │ 
└─────────┘.
"""
    return card 
"""
┌─────────┐ 
│\/\/\/\/\│ 
│/\/\/\/\/│ 
│\/\/\/\/\│ 
│/\/\/\/\/│ 
│\/\/\/\/\│ 
└─────────┘.
""" # Alternative...

def show_player_hand():
    print(f"Player's Hand: {', '.join(player_hand)}")

def deal_card():
    card_dealt = random.choice(deck)
    deck.remove(card_dealt)
    player_hand.append(card_dealt)
    return card_dealt

def format_player_hand():
    # for some reason I needed to put them back in to hearstrings
    in_hand = f"""
{player_hand_visual}
"""
    to_hand = f"""
{card_visual}
"""
    # Splitting the strings into lines
    in_hand = in_hand.strip().split('\n')
    to_hand = to_hand.strip().split('\n')

    # Pairing up lines and concatenating them with a space in between
    combined_lines = [line_a + ' ' + line_b for line_a, line_b in zip(in_hand, to_hand)]

    # Joining the combined lines into a single string
    endstate = '\n'.join(combined_lines)

    return endstate

def format_dealer_hand_inital():
    # for some reason I needed to put them back in to hearstrings
    in_hand = f"""
{dealer_hand_visual_initial}
"""
    to_hand = """
┌─────────┐ 
│ ┌─────┐ │ 
│ │     │ │ 
│ │     │ │ 
│ │     │ │ 
│ └─────┘ │ 
└─────────┘.
"""
    # Splitting the strings into lines
    in_hand = in_hand.strip().split('\n')
    to_hand = to_hand.strip().split('\n')

    # Pairing up lines and concatenating them with a space in between
    combined_lines = [line_a + ' ' + line_b for line_a, line_b in zip(in_hand, to_hand)]

    # Joining the combined lines into a single string
    endstate = '\n'.join(combined_lines)

    return endstate

def format_dealer_hand():
    # for some reason I needed to put them back in to hearstrings
    in_hand = f"""
{dealer_hand_visual}
"""
    to_hand = f"""
{card_visual}
"""
    # Splitting the strings into lines
    in_hand = in_hand.strip().split('\n')
    to_hand = to_hand.strip().split('\n')

    # Pairing up lines and concatenating them with a space in between
    combined_lines = [line_a + ' ' + line_b for line_a, line_b in zip(in_hand, to_hand)]

    # Joining the combined lines into a single string
    endstate = '\n'.join(combined_lines)

    return endstate

def show_player_money():
    if insurance == False:
        insurance_report = 0
    elif insurance == 'Declined':
        insurance_report = 'Declined'
    else:
        insurance_report = int(insurance_amount)
    wider = '─' * (2 + 5 + 4 + 4)

    player_bar = f"""
┌───────{wider}──────────────────────────────────────────┐
│ Round: {int(blackjack_round):<2}     Money: {int(player_money):<5}     Wager: {int(player_wager):<4}     Insurance: {insurance_report:<4} │
└───────{wider}──────────────────────────────────────────┘
""".split('\n')
    player_bar = '\n'.join(player_bar[1:])
    print(player_bar)


def show_hands_initial(action):
    clear()
    print(f"[Action] {action}\n")
    print(f"{dealer_hand_visual_initial}\nDealer's Hand... {dealer_hand_value_initial}/21\n")
    if player_hand_visual == "":
        player_hand_visual_empty = """






"""
        print(f"{player_hand_visual_empty}Player's Hand... {player_hand_value}/21\n")
    else:
        print(f"{player_hand_visual}Player's Hand... {player_hand_value}/21\n")
    show_player_money()

def show_hands(action):
    clear()
    print(f"[Action] {action}\n")
    print(f"{dealer_hand_visual}\nDealer's Hand... {dealer_hand_value}/21\n")
    print(f"{player_hand_visual}Player's Hand... {player_hand_value}/21\n")
    show_player_money()

def show_dealer_wins():
    print(f"You lost the hand. The Croupier proceeds to collect your wager.")
    print(f"The dealer wins with {dealer_hand_value}/21.")
    print(f"The player loses with {player_hand_value}/21.")
    global player_money
    player_money -= player_wager
    show_player_money()

def show_dealer_wins_without_showing_hole_card():
    print(f"You lost the hand. The Croupier proceeds to collect your wager.")
    print(f"The dealer wins with {dealer_hand_value_initial}/21.")
    print(f"The player loses with {player_hand_value}/21.")
    global player_money
    player_money -= player_wager
    show_player_money()

def show_player_wins(type='Standard'):
    print(f"Congratulations!")
    print(f"The dealer loses with {dealer_hand_value}/21.")
    print(f"The player wins with {player_hand_value}/21.")
    global player_money
    if type == 'Standard':
        player_money += standard_payout
    elif type == 'Blackjack':
        player_money += blackjack_payout
    show_player_money()

def show_player_dealer_draw():
    print(f"Push... Your bet is returned.")
    print(f"The dealer draws with {dealer_hand_value}/21.")
    print(f"The player draws with {player_hand_value}/21.")
    global player_money
    player_money = player_money
    show_player_money()


#TODO
# Reshuffle cards after x many games...............
# spliting two 10s..........................

player_money = 10000
player_wager = 10
standard_payout = player_wager * 1.5 #(player_wager * .5) + player_wager
blackjack_payout = player_wager * 6

blackjack_round = 0
playing_blackjack = True
while playing_blackjack:
    blackjack_round += 1
    insurance = False
    insurance_amount = 0
    insurance_payout_multiplier = 4 #normally 2 in casinos...
    while True:
        dealer_hand = []
        dealer_hand_value = 0
        dealer_hand_value_initial = 0
        dealer_hand_visual_initial = ""
        dealer_hand_visual = ""
        dealer_hand_hole_card = 0
        dealer_check_if_blackjack = False

        player_hand = []
        player_hand_visual = ""
        player_hand_value = 0


        clear()
        blackjack_banner = f"""
______ _            _    ┌─────────┐┌─────────┐     _    
| ___ \ |          | |   │J        ││A        │    | |   
| |_/ / | __ _  ___| | __│         ││         │ ___| | __
| ___ \ |/ _` |/ __| |/ /│    ♥    ││    ♣    │/ __| |/ /
| |_/ / | (_| | (__|   < │         ││         │ (__|   < 
\____/|_|\__,_|\___|_|\_\│       J ││       A │\___|_|\_\ 
                         └─────────┘└─────────┘
[3 tot 2 payout, dealer must hit soft '17', insurance = 1/2 bet and pays 4:1, normally in casino's it's 2:1]
Player Blackjacks auto-win, and get a 6:2 payout vs the typical 3:2.
"""
        print(blackjack_banner)
        show_player_money()
        try:
            player_wager = input("How much would you like to wager? (minimum is 10) ")

            # Check if the input is empty and set default
            if player_wager.strip() == '':
                player_wager = 10
            else:
                player_wager = int(player_wager)

            # Check if wager is more than available money
            if player_wager > player_money:
                raise ValueError("You have insufficient funds to make this wager.")
            elif player_wager < 10:
                raise ValueError("Minimum wager is 10.")

            # If all checks pass, break the loop
            # input(f"Press enter to continue 1")
            break

        except ValueError as e:
            print(e)
            input(f"Please enter a valid amount of money.")


    currnet_hand = 1
    playing_round = True
    player_hand_card_num = 0
    while playing_round:
        # The initial dealing of the cards
        if currnet_hand == 1:
            ##### Dealer #####

            # Display Card
            card_dealt = deal_card()
            dealer_hand.append(card_dealt)
            # #!!!!!!!!!!!!!!!!!testing insurance
            # card_dealt = " A♣"

            card_visual = show_deal_card(card_dealt)
            dealer_hand_visual         = '\n'.join(card_visual.split('\n')[1:9])
            dealer_hand_visual_initial = '\n'.join(card_visual.split('\n')[1:9])
            card_value = blackjack_values.get(card_dealt[:2].strip())
            dealer_hand_value += card_value
            dealer_hand_value_initial += card_value

            show_hands_initial("The Croupier dealt their first card.")
            ##### print(f"{dealer_hand_visual_initial}\nDealer's Hand... {dealer_hand_value_initial}/21\n")


            if dealer_hand_value_initial == 11: # An Ace
                while True:
                    insurance_offer = input(f"The Croupier offers insurance against a potential Blackjack. (y/n) ")
                    if insurance_offer == 'y':
                        insurance_amount = player_wager * 0.5
                        try:
                            # Check if wager is more than available money
                            if insurance_amount > (player_money - player_wager):
                                print(f"You have insufficient funds to pay for this insurance amount.")
                                insurance = False
                                insurance_amount = 'None'
                                break
                            elif insurance_amount > (player_wager * 0.5):
                                insurance = False
                                insurance_amount = 'None'
                                # This won't trigger until I make insurance rangable....
                                raise ValueError(f"You can only get insurance for up to 1/2 your wager, so up to {player_wager * 0.5}")
                            else:
                                insurance = True
                            # If all checks pass, break the loop
                            print(f"\nThe player accepts taking insurance.\n")
                            break

                        except ValueError as e:
                            print(e)
                            input(f"Please enter a valid amount of money.")
                        break

                    elif insurance_offer == 'n':
                        print(f"\nThe player declines taking insurance.\n")
                        insurance = 'Declined'
                        insurance_amount = 'None'
                        break

                    else:
                        print(f"Please make a valid input")
 
            input(f"Press enter to continue 2")


            card_dealt = deal_card()
            dealer_hand.append(card_dealt)
            # #!!!!!!!!!!!!!!!!!testing insurance
            # card_dealt = " K♣"

            card_visual = show_deal_card(card_dealt)

            dealer_hand_visual         += format_dealer_hand()
            dealer_hand_visual_initial += format_dealer_hand_inital()

            dealer_hand_visual         = '\n'.join(dealer_hand_visual.split('\n')[7:16]) + '\n'
            dealer_hand_visual_initial = '\n'.join(dealer_hand_visual_initial.split('\n')[7:16]) + '\n'

            card_value = blackjack_values.get(card_dealt[:2].strip())
            dealer_hand_value += card_value
            # dealer_hand_value_initial = dealer_hand_value_initial # Doesn't not change

            # print(f"{dealer_hand_visual_initial}\nDealer's Hand... {dealer_hand_value_initial}/21\n")
            show_hands_initial("The Croupier dealt their hole card.")

            input(f"Press enter to continue 3")
            # print(dealer_hand_hole_card)


            ##### Player #####
            card_dealt = deal_card()
            player_hand.append(card_dealt)
            player_hand_card_num += 1
            # show_player_hand()
            card_visual = show_deal_card(card_dealt)
            # print(card_visual)
            # player_hand_visual = card_visual
            player_hand_visual = '\n'.join(card_visual.split('\n')[1:9])
            card_value = blackjack_values.get(card_dealt[:2].strip())
            player_hand_value += card_value
            show_hands_initial("The Croupier dealt your first card...")

            # print(f"Peek at Deck: {deck}")
        # Player gets dealt second card
        else:
            if hit == 'y':
                clear()
                card_dealt = deal_card()
                player_hand.append(card_dealt)
                player_hand_card_num += 1
                # show_player_hand()
                card_visual = show_deal_card(card_dealt)
                # print(card_visual)
                player_hand_visual += format_player_hand()

                # Split the string into lines
                # Remove the first 7 lines, rather, keeps the last 7
                # Join the remaining lines back into a string
                player_hand_visual = '\n'.join(player_hand_visual.split('\n')[7:16]) + '\n'

                # print(player_hand_visual)

                card_value = blackjack_values.get(card_dealt[:2].strip())
                if card_value == 11 and player_hand_value >= 11:
                    player_hand_value += 1
                else:
                    player_hand_value += card_value
        
                show_hands_initial("The Croupier dealt you another card...")
                # input(f"Press enter to continue 4")
                # print(f"Peek at Deck: {deck}")

            else:
                exit

                
        if player_hand_value > 21:
            clear()
            show_hands_initial(f"The Croupier announces that you've BUSTED.")
            # print('TS: for some reason I asked for one card and got and busted...')
            # print(f"BUSTED!!! You lost with {player_hand_value}.")
            show_dealer_wins_without_showing_hole_card()
            input(f"Press enter to continue 5")
            break
        elif player_hand_value == 21:
            # If the player has blackjack (two cards), the player auto wins
            if player_hand_card_num == 2:
                show_hands(f"The Croupier exclaims BLACKJACK, and awards you the wager.")
                show_player_wins()
                input(f"Press enter to continue 6")
            # If the player has 21, but more than two cards, the dealer get's to check if they have blackjack.
            elif player_hand_card_num > 2:
                dealer_check_if_blackjack = True
                input(f"Player has 21, the Croupier will play to see if they have Blackjack")
                # input(f"Press enter to continue 7")
            # print(f"You won with {player_hand_value}.")
                
        elif player_hand_value < 21 or (player_hand_value == 21 and dealer_check_if_blackjack == True):
            if currnet_hand == 1:
                currnet_hand += 1
                hit = 'y'
                input('Press enter to continue 9')
            else:
                hit = input(f"\nDo you want another card? (y/n) ")

            if hit == 'y':
                clear()
                # show_hands(f"The Croupier hits, and took another card.")

            elif hit == 'n':
                # Finally the Dealer's turn to reveal the hole card
                dealer_flipped_hole_card = False
                dealer_keeps_hitting = True
                while dealer_keeps_hitting:
                    if dealer_flipped_hole_card == False:
                        dealer_flipped_hole_card = True
                        show_hands(f"The Croupier reveals their hole card.")

                        input(f"Press enter to continue 10")
                    elif dealer_hand_value == 21 and dealer_check_if_blackjack == True:
                        input(f"Dealer Wins with blackjack!!!!!!!!!!!!!!!!!!!!!")
                    elif dealer_hand_value < 17:

                        clear()
                        card_dealt = deal_card()
                        dealer_hand.append(card_dealt)
                        # print(card_dealt)
                        card_visual = show_deal_card(card_dealt)
                        dealer_hand_visual += format_dealer_hand()
                        dealer_hand_visual = '\n'.join(dealer_hand_visual.split('\n')[7:16]) + '\n'
                        card_value = blackjack_values.get(card_dealt[:2].strip())
                        if card_value == 11 and dealer_hand_value >= 11:
                            dealer_hand_value += 1
                        else:
                            dealer_hand_value += card_value

                        show_hands(f"The Croupier hits, and took another card.")
                        input(f"Press enter to continue 11")

                    elif dealer_hand_value == 21:
                        if insurance == True and len(dealer_hand) == 2:
                            # This accounts for the scenarior if the player has 21, but not blackjack, and the dealer has blackjack and wins
                            insurance_payout = insurance_amount * insurance_payout_multiplier
                            player_money += insurance_payout
                            show_hands(f"The Croupier applauds your insurance decision, and awards you {insurance_payout}.")
                            show_dealer_wins()
                            input(f"Press enter to continue 12")
                        elif insurance == True and len(dealer_hand) > 2:
                            player_money -= insurance_amount
                            show_hands(f"The Croupier comments on your decision to take insurance, and collects {insurance_amount}.")
                            show_dealer_wins()
                            input(f"Press enter to continue 13")
                        elif insurance == 'Decline' and len(dealer_hand) == 2:
                            # No insurance deducted, as you didn't accept
                            show_hands("The Croupier comments on the odds of your decision with insurance or not.")
                            show_dealer_wins()
                            input(f"Press enter to continue 14")
                        else:
                            show_hands("The Croupier empathizes with your loss.")
                            show_dealer_wins()
                            input(f"Press enter to continue")
                        break
                    elif dealer_hand_value > 21:
                        show_hands(f"The Croupier congratulates you on the win.")
                        show_player_wins()
                        input(f"Press enter to continue 16")
                        break                    
                    else: # Covers 17 to 20
                        show_hands(f"The Croupier stands.")
                        print(f"The dealer stands at {dealer_hand_value}/21.")
                        input(f"Press enter to continue 17")

                        if dealer_hand_value > player_hand_value:
                            show_hands("The Croupier empathizes with your loss.")
                            show_dealer_wins()
                            # input(f"Press enter to continue 18")
                        elif dealer_hand_value < player_hand_value:
                            show_hands(f"The Croupier congratulates you on the win.")
                            show_player_wins()
                            # input(f"Press enter to continue 19")
                        elif dealer_hand_value == player_hand_value:
                            show_hands(f"The Croupier announces a push.")
                            show_player_dealer_draw()
                            # input(f"Press enter to continue 20")

                        # input(f"Press enter to continue 21")
                        break
                # print(f"Peek at Deck: {deck}")
                # show_player_dealer_draw()
                # input('wait.... Press enter to continue 22')
                break
            else:
                show_hands_initial("The Croupier looks at you patiently, awaiting your decision...")
                print(f"Make a valid entry.")
    hit = 'n'
    print(f"End of Blackjack round...")
    input('Press enter to continue 23')


