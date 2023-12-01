#! /usr/bin/env python3

import random

coin_toss = random.randint(1,2)
if coin_toss == 1:
    side = 'heads'
elif coin_toss == 2:
    side = 'tails'
print(f"Tossing the coin... it landed on {side}")

