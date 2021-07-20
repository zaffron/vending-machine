class Item:
  def __init__(self, name, price, stock):
    self.name = name
    self.price = price
    self.stock = stock

  def updateName(self, name):
    self.name = name

  def updatePrice(self, price):
    self.price = price
  
  def updateStock(self, stock):
    self.stock = stock

  def buy(self):
    if self.stock == 0:
      pass
    self.stock -= 1