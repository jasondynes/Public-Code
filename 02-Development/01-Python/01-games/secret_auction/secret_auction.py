logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

bids = {}

def find_highest_bid():
    # iterate through list to get max bid
    max_bid = 0
    max_name = ""
    for name, bid in bids.items():
        if bid > max_bid:
            max_bid = bid
            max_name = name
    return (max_name, max_bid)

def data_input():
    print(logo)
    print("Welcome to the secret auction program.")
    more_bids = True
    while more_bids:
        name = input("What is your name?: ")
        bid = input("What's your bid?: ")
        if input(str("Are there any other bidders? Type 'yes' or 'no'.")) == "no":
            bids[name] = int(bid)
            more_bids = False
        else:
            bids[name] = int(bid)

# main code
def main():
    data_input()
    max_name, max_bid = find_highest_bid()
    print(f"The winner is {max_name} with a bid of {max_bid}")

if __name__ == "__main__":
    main()
