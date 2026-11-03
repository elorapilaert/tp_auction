# pylint: disable=missing-docstring

from utils import Cli
from itertools import count


class EnglishAuction():

    def __init__(self, cli=None):
        self.cli = cli if cli else Cli()

    def play(self):
        # Input opening bid
        self.cli.display('Started auction of type: Blind')
        opening_bid = self.cli.prompt('Please enter the amount for the opening bid:')
        opening_bid = int(opening_bid)
        self.cli.display(f"Opening bid is: {opening_bid}")

        # Input bidders
        bidders = []
        for index in count(1):
            bidder = self.cli.prompt(
                f"Enter name for bidder {index} (enter nothing to move on):"
            )
            if not bidder:
                break
            bidders.append(bidder)
        self.cli.display(f"\nBidders are: {', '.join(bidders)}\n")
        print(bidders)
        # Collect bids
        standing_bid = opening_bid
        winner = None
        bid_state=[True for k in range(len(bidders))]
        End=[False for k in range(len(bidders))]
        while bid_state!=End:
            for k in range(len(bidders)):
                bidder=bidders[k]
                bid = self.cli.prompt(f"Standing bid is {standing_bid}. {bidder} bids:"
            )
                if not bid :
                    bid_state[k]=False
                else :
                    bid = int(bid)
                    if bid > standing_bid:
                        standing_bid = bid
                        winner = bidder
                        End=[False for k in range(len(bidders))]
                

            

        # Display winner
        self.cli.display("\n~~~~~~~~\n")
        self.cli.display(f"Winner is {winner}. Winning bid is {standing_bid}.")



if __name__ == "__main__":
    auction = EnglishAuction()
    auction.play()
