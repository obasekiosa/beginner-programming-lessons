from random import shuffle as shuf
from random import choice
from random import randint



## card class
## it has a suite and a number ["circle", "rectangle", "triangel", "star", "cross", "whot"]
## i can ask for it sute or number
## i can tell the class to create a new random dard


class CardM():

    def __init__(self, suite, number):
        self.suite = suite
        self.number = number

    def getSuite(self):
        return self.suite

    def __str__(self):
        f"Suite: {self.suite} - Number: {self.number}"

    def __repr__(self):
        f"{self.suite} - {self.number}"

    def getNumber(self):
        return self.number

    @classmethod
    def randomCard(cls):
        suite = choice(["circle", "rectangle", "triangel", "star", "cross", "whot"])
        number = randint(0, 15)

        if suite == "whot":
            number = 20
        
        return CardM(suite, number)



card = CardM("circle", 4)
print(card.getNumber(), card.getSuite())
print()
print(card.randomCard().getSuite())

class MarketM():

    
    suites = ["circle", "rectangle", "triangel", "star", "cross", "whot"]

    NUM_OF_20 = 0
    def generateDecks():
        deck = []
        for s in suite:
            if s != "whot":
                for i in range(1, 15):
                    deck.append(Card(s, i))
            else:
                for i in range(NUM_OF_20):
                    deck.append(Card(s, 20))
        
        return deck


    def __init__(self, no_of_decks=1, shuf = True, num_of_20 = 5):
        self.NUM_OF_20 = num_of_20
        self.market = generateDecks() * no_of_decks
        if shuf:
            shuffle(self.market)

        self.N = len(self.market)

    
    def giveCard(self):
        assert self.N != 0
           
        self.N -= 1
        return self.market.pop()

    def shareCard(self, num_of_cards=4, num_of_players=2, min = 3):
        total_num_of_cards = num_of_cards * num_of_players

        if self.N % total_num_of_cards != 0:
            #finish yourself
            pass

    def isEmpty(self):
        return self.N == 0


    




# class Card:
#     def __init__(self, number, shape) -> None:
#         self.number = number
#         self.shape = shape
    
#     def __str__(self) -> str:
#         return str(self.number) + " -> " + self.shape

#     def create_card(self, shape):
#         deck = []
#         for i in range(1,15):
#             card = Card(i, shape)
#             deck.append(card)
#         return deck

# class Market():

#     def __init__(self) -> None:
#         self.pack = []
#         self.shuffled_cards = []

#     def pick_card(self):
#         return self.shuffled_cards[-1]

#     def load(self):             # To create card and put in market
#         shapes = ["star", "circle", "square", "triangle"]
#         for shape in shapes:
#             self.pack += self.create_card(shape)
#         print("loaded successfully")
    
#     def shuffle_cards(self):
#         self.shuffled_cards = self.pack
#         shuffle(self.shuffled_cards)
#         print("shuffled")


# stack = Market()
# stack.load()
# stack.shuffle_cards()
# for card in stack.pack:
#     print(card)
# print(stack.pick_card())