# Raad Barnett 1231583
class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0
        self.item_description = "none"
    def print_item_cost(self):
        print("{} {} @ ${} = ${}".format(self.item_name,self.item_quantity,self.item_price,self.item_price*self.item_quantity))
    def print_item_description(self):
        print(self.item_name+": "+self.item_description)
class ShoppingCart:
    def __init__(self,name,date):
        self.customer_name = name
        self.current_date = date
        self.cart_items = []
    def add_item(self,obj):
        self.cart_items.append(obj)
    def remove_item(self,name):
        for item in self.cart_items:
            if(item.item_name==name):
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")
    def modify_item(self,obj):
        for item in self.cart_items:
            if(item.item_name==obj.item_name):
#                item.item_price = obj.item_price
                item.item_quantity = obj.item_quantity
#                item.item_description = obj.item_description
                return
        print("Item not found in cart. Nothing modified.")
    def get_num_items_in_cart(self):
        total_quantity_of_cart = 0
        for item in self.cart_items:
            total_quantity_of_cart+=item.item_quantity
        return total_quantity_of_cart
    def get_cost_of_cart(self):
        total_cost_of_cart = 0
        for item in self.cart_items:
            total_cost_of_cart+=(item.item_price*item.item_quantity)
        return total_cost_of_cart
    def print_total(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name,self.current_date))
        print("Number of Items:",self.get_num_items_in_cart())
        print()
        if(len(self.cart_items)>0):
            for item in self.cart_items:
                item.print_item_cost()
        else:
            print("SHOPPING CART IS EMPTY")
        print()
        print("Total: ${}".format(self.get_cost_of_cart()))
    def print_description(self):
        if(len(self.cart_items)>0):
            print("{}'s Shopping Cart - {}".format(self.customer_name,self.current_date))
            print()
            print("Item Descriptions")
            for item in self.cart_items:
                item.print_item_description()
        else:
            print("SHOPPING CART IS EMPTY")


print("Enter customer's name:")
name = input()
print("Enter today's date:")
date = input()
obj = ShoppingCart(name,date);
print()
print("Customer name: {}".format(obj.customer_name))
print("Today's date: {}".format(obj.current_date))
print()
def print_menu(obj):
    choice = ''
    menu = "MENU\na - Add item to cart\nr - Remove item from cart\nc - Change item quantity"+"\ni - Output items' descriptions"+"\no - Output shopping cart"+"\nq - Quit\n"
    print(menu)
    while(choice!='q'):
        print("Choose an option:")
        choice = input()
        if(choice=='a'):
            obj1 = ItemToPurchase()
            print("ADD ITEM TO CART")
            print("Enter the item name:")
            obj1.item_name=input()
            print("Enter the item description:")
            obj1.item_description = input()
            print("Enter the item price:")
            obj1.item_price = int(input())
            print("Enter the item quantity:")
            obj1.item_quantity = int(input())
            obj.add_item(obj1)
            print()
            print(menu)
        elif(choice=='r'):
            print("REMOVE ITEM FROM CART")
            print("Enter name of item to remove:")
            obj.remove_item(input())
            print()
            print(menu)
        elif(choice=='c'):
            print("CHANGE ITEM QUANTITY")
            obj1 = ItemToPurchase()
            print("Enter the item name:")
            obj1.item_name = input()
            print("Enter the new quantity:")
            obj1.item_quantity = int(input())
            obj.modify_item(obj1)
            print()
            print(menu)
        elif(choice=='i'):
            print("OUTPUT ITEMS' DESCRIPTIONS")
            obj.print_description()
            print()
            print(menu)
        elif(choice=='o'):
            print("OUTPUT SHOPPING CART")
            obj.print_total()
            print()
            print(menu)
print_menu(obj)

