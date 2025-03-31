class Restaurant:
    def __init__(self):
        self.menu = {}

    def add_item(self, name, price):
        self.menu[name] = price
        print("Item added/updated successfully")

    def remove_item(self, name):
        if name in self.menu:
            del self.menu[name]
            print("Item removed successfully")
        else:
            print("Item not found")

    def display_menu(self):
        if self.menu:
            print("Menu:")
            for item in self.menu:
                print(f"{item}: {self.menu[item]}")
        else:
            print("The menu is empty.")


item1,price1 = input().split()
item2,price2 = input().split()
item3,price3 = input().split()
item_rem = input()

res = Restaurant()

res.add_item(item1,price1)
res.add_item(item2,price2)
res.add_item(item3,price3)
res.remove_item(item_rem)
res.display_menu()


