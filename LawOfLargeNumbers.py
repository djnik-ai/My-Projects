import random

heads = 0
tails = 0

message = int(input('How many times do you want to flip the coin?\n'))

for i in range(message):
    number = random.randint(1, 2)
    if number == 1:
        heads += 1
    else:
        tails += 1

print(f'''You have gotten {heads} heads, and {tails} tails.
          Heads: {100*heads/(heads+tails)}% | Tails: {100*tails/(heads+tails)}%''')
