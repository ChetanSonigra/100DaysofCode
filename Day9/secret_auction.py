import art,os
print('Welcome to Secret Auction Program')

print(art.logo)

def find_max_bidder(bids):
    max_bid = max(bids.values())
    for name in bids:
        if bids[name]==max_bid:
            print(f'{name} won with bid of ${max_bid}.')
            return

bids = {}
end_of_game = False
while not end_of_game:
    name = input('Enter your name: ')
    price = int(input('Enter your bid amount. $'))
    bids[name] = price
    
    ask = input('Are there other bidders?(y/n): ').lower()
    if ask == 'n':
        end_of_game = True
        find_max_bidder(bids)
    else:
        os.system('cls')