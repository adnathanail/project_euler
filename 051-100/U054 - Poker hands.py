suits = ["S", "H", "C", "D"]
types = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
class Hand:
  cards = []
  def __init__(self, cards):
    self.cards = cards.split(" ")
  def justCards(self):
    return [card[0] for card in self.cards]
  def getSuit(self, suit):
    return [card for card in self.cards if card[1] == suit]
  def getSuitJustCards(self, suit):
    return [card[0] for card in self.getSuit(suit)]
  def royalFlush(self):
    for s in suits:
      if sorted(self.getSuitJustCards(s)) == ['A', 'J', 'K', 'Q', 'T']:
        return s
    return False
  def straightFlush(self):
    ns = {"T":10, "J":11, "Q":12, "K":13, "A":14}
    for s in suits:
      c1 = self.getSuitJustCards(s) # Cards as strings
      c2 = list(map(lambda x: ns.get(x, int(x) if x.isdigit() else x), c1)) # Cards as ints
      c3 = sorted(c2) # Sorted cards
      if c3[-1] - c3[0] == 4:
        return s
    return False
  def fourOfAKind(self):
    cards = self.justCards()
    for t in types:
      if cards.count(t) >= 4:
        return t
    return False
  def fullHouse(self):
    cards = self.justCards()
    three = False
    threecard = ""
    two = False
    for t in types:
      if cards.count(t) == 3:
        three = True
        threecard = t
      if cards.count(t) == 2:
        two = True
    return threecard if three and two else False
  def flush(self):
    for s in suits:
      if len(self.getSuit(s)) == 5:
        return s
    return False
  def straight(self):
    ns = {"T":10, "J":11, "Q":12, "K":13, "A":14}
    c1 = self.justCards() # Cards as strings
    c2 = list(map(lambda x: ns.get(x, int(x) if x.isdigit() else x), c1)) # Cards as ints
    c3 = sorted(c2) # Sorted cards
    if c3[-1] - c3[0] == 4:
      return True
    return False
  def threeOfAKind(self):
    cards = self.justCards()
    for t in types:
      if cards.count(t) == 3:
        return t
    return False
  def twoPairs(self):
    cards = self.justCards()
    first = False
    firstcard = ""
    second = False
    secondcard = ""
    for t in types:
      if cards.count(t) == 2:
        if not first:
          first = True
          firstcard = t
        else:
          second = True
          secondcard = t
    return [firstcard, secondcard] if first and second else return False
  def onePair(self):