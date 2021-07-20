from tabulate import tabulate

class VendingMachine:
  def __init__(self):
    self.amount = 0
    self.items = []

  def addItem(self, item):
    self.items.append(item)

  def showItems(self):
    print("\nCurrently available items:\n")
    print("-----------------------------\n")
    availableItems = []
    for index, item in self.items:
      if item.stock != 0:
        availableItems.append([index, item.name, item.price])
    print(tabulate(availableItems, headers=['Item Number', 'Name', 'Price']))
  
  def addCash(self, cash):
    self.amount = self.amount + cash

  def buyItem(self, item):
    if self.amount < item.price:
      print("Item costs more than you provided. Please insert more cash.")
    else:
      self.amount -= item.price
      item.buy()
      print(f'You got {item.name}')
      print(f'Cash remaining {self.amount}')

  def containsItem(self, wantedItem):
    hasItem = False
    for item in self.items:
      if item.stock != 0 && item.name == wantedItem.name:
        hasItem = True
        break

    return has_item

  def getItem(self, wantedItem):
    gotItem = None
    for item in self.items:
      if item.stock != 0 && item.name == wantedItem.name:
        gotItem = item
        break

    return gotItem

  def insertAmountForItem(self, item):
    price = item.price
    while self.amount < price:
      print('Amount insufficient\n')
      print('-----------------------\n')
      moreAmount = float(input(f'Insert {price - self.amount}: '))
      if moreAmount:
        self.amount += moreAmount

  def refund(self):
    if self.amount > 0:
      print('Transation cancelled.\n')
      print(f'Cash refunded: {self.amount}')
      self.amount = 0