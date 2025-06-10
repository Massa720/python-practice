class Item:
    def __init__(self,ID, name, price, purchase_price ):
        self.name = name
        self.ID = ID
        self.price = price
        self.purchase = purchase_price

    def cost_rate(self):
        rate = self.purchase/ self.price  
        return rate
    

item_1 = Item("A0001", "半袖クールTシャツ", 6000, 2250)   
rate = item_1.cost_rate()
print(rate)




    