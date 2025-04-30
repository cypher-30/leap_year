class Classey:
    varis = 2


    def mymethod(self):
        print(self.varis)


object_one = Classey()
object_two = Classey()

object_one.varis = 3
object_two.varis = 5

print(object_one.varis)
print(object_two.varis)



class Transport:
    def __init__(self, air, water):
        self.air  = air
        self.water = water


obj_transport = Transport("Beluga","Hovercraft")
obj2_transport= Transport( "Jet", "Boat")

print(obj_transport.air, obj_transport.water)
print(obj2_transport.air, obj2_transport.water)


class shopping_cart:
    def __init__(self):
        self.item = []

    def add_item(self, item_name, qty):
        item = (item_name, qty)
        self.item.append(item)

    def remove_item(self, item_name):
        for item in self.item:
            if item(0) == item_name:
                self.item.remove(item)
                break

    #   This method computes the number of items in self.items
    def calculate_total(self):
        total = 0
        for item in self.item:
            total += item[1]
        return total

cart = shopping_cart()

#Add items to cart
cart.add_item("kiwi", 100)
cart.add_item("papaya", 200)
cart.add_item("orange", 76)

print("Current item In Cart")
for item in cart.item:
    print(item[0], "-", item[1])

total_qty = cart.calculate_total()
print("Total_quantity", total_qty)