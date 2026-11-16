# J'ai fait unee autre méthode que la méthode indiquée en indice, et je ne voulais pas la modifier comme elle était fonctionnelle

from itertools import count

# CLI = Command Line Interface
from utils import Cli

class Auction() :

    def __init__(self, cli=None):
            self.cli = cli if cli else Cli()
            self.opening_bid =None
            self.winner =None
            self.bidders=[]
    
    def play(self):
        # Input opening bid
        self.cli.display('Started auction of type: Blind')
        opening_bid= self.cli.prompt('Please enter the amount for the opening bid:')
        self.opening_bid= int(opening_bid)
        self.cli.display(f"Opening bid is: {self.opening_bid()}")
    
        # Input bidders
        self.bidders=[]
    
        for index in count(1):
            bidder = self.cli.prompt(
                f"Enter name for bidder {index} (enter nothing to move on):"
                )
            if not bidder:
                break
            self.bidders.append(bidder)
        self.cli.display(f"\nBidders are: {', '.join(bidders)}\n")
    
            # Collect bids
        self.auction_loop()
    
            # Display winner
        self.cli.display("\n~~~~~~~~\n")
        self.cli.display(f"Winner is {self.winner()} Winning bid is {standing_bid}.")
    
    
    

class BlindAuction(Auction):

    



    def auction_loop(self):

        standing_bid = self.opening_bid
        self.winner = None
        for bidder in self.bidders:
            bid = self.cli.prompt(
                f"Opening bid is {self.opening_bid(())}. {bidder} bids:"
            )
            bid = int(bid)
            if bid > standing_bid:
                standing_bid = bid
                self.winner = bidder

class EnglishAuction(Auction):

     def auction_loop(self):
        standing_bid = self.opening_bid
        self.winner = None
        bidders=self.bidders
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
                    self.winner = bidder
                    End=[False for k in range(len(bidders))]








if __name__ == "__main__":
        auction = BlindAuction() #à changer si on veut changer de type d'enchères
        auction.play()

     
