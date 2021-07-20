import json

def load():
  ret = {}
  vendingFile = open('./data.json', 'rt')
  for line in vendingFile:
    k, v = line.strip().split("=", 1)
    ret[k] = eval(v)

def save(**kwargs):
  vendingFile = open('./data.json', 'wt')
  for k, v in kwargs.items():
    print >>f 

def vend():
  vendingMachine = VendingMachine()
  