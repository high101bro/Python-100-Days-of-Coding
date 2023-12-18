#! /usr/bin/env python3

import os
import random

def clear():
    if os.name == 'posix':  # Unix/Linux/macOS
        os.system('clear')
    elif os.name == 'nt':  # Windows
        os.system('cls')
        
banner =f"""
###########################
#  Silent Action Bidding  #
###########################
"""

silent_bids = {}

while True:
    clear()
    print(banner)
    print(f"There are a total of {len(silent_bids)} bids.\n")
    while True:
        participate = input(f"Would you like to bid? (yes/no) ")
        if participate == 'yes':
            name = input(f"Enter your name: ")
            phone = input(f"Enter your phone number: ")
            email = input(f"Enter your email address: ")
            while True:
                try:
                    bid  = int(input(f"Enter your bid amount in whole dollars: (exampel, 10) "))
                    break
                except:
                    print(f"Please make a valid entry.")
            print(f"""
Please verify:
  Name:  {name}
  Phone: {phone}
  Email: {email}
  Bid:   {bid}
""")
            while True:
                verify = input(f"Is the above is correct: (yes/no) ").lower()
                if verify == 'yes':
                    unique_name = f"{name} # {random.randint(1,10000000)}"
                    silent_bids[unique_name] = {
                        "Name": None,
                        "Phone": None,
                        "Email": None,
                        "Bid": None,
                    }
                    silent_bids[unique_name]["Name"] = name
                    silent_bids[unique_name]["Phone"] = phone
                    silent_bids[unique_name]["Email"] = email
                    silent_bids[unique_name]["Bid"] = bid

                    print(f"Thank you for your bid.")
                    break
                elif verify == 'no':
                    print(f"Your bid was not entered")
                    break
                else:
                    print(f"Invalide entry")
            break
        elif participate == 'no':
            break
        elif participate == 'see-bids':
            # print_pretyy = json.dumps(silent_bids,indent=4)
            # print(print_pretyy)
            print(silent_bids)
            input(f"Press enter to continue")
            break
        elif participate == 'see-highest':
            # try:
                highest_bid = 0
                winner_name = None

                for key in silent_bids:
                    if bid > highest_bid:
                        highest_bid = bid
                        winner_name = silent_bids[key]['Name']

                # Print the name of the winner and their highest bidyesyes
                
                print("Winner:", winner_name)
                print("Highest Bid:", highest_bid)
                input(f"Press enter to continue")
            # except:yes
            
            #     passyes
            # break
        else:
            input(f"Please make a valid entry. Press Enter to continue.")
            break