# Raad Barnett 1231583
class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0
    def print_item_cost(self):
        print("{} {} @ ${} = ${}".format(self.item_name,self.item_quantity,self.item_price,self.item_price*self.item_quantity))

item1 = ItemToPurchase()
print("Item 1")
print("Enter the item name:")
item1.item_name = input()
print("Enter the item price:")
item1.item_price = int(input())
print("Enter the item quantity:")
item1.item_quantity = int(input())
print()
item2 = ItemToPurchase()
print("Item 2")
print("Enter the item name:")
item2.item_name = input()
print("Enter the item price:")
item2.item_price = int(input())
print("Enter the item quantity:")
item2.item_quantity = int(input())
print()
print("TOTAL COST")
item1.print_item_cost()
item2.print_item_cost()
print()
print("Total: ${}".format(item1.item_price*item1.item_quantity+item2.item_price*item2.item_quantity))
