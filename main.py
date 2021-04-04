
class Item:
    '''
    This is your list.'''

    number_of_items = 0
    list_of_items = {}

    def __init__(self, name, price):
        self.name = name
        self.price = price
        print("(Initializing {})".format(self.name))

    def delete_item(self):
        del Item.list_of_items[self.name]
        Item.number_of_items -= 1

    def add_item(self):
        if self.name in Item.list_of_items:
            # compare price here
            Item.list_of_items[self.name] = self.price
        else:
            Item.number_of_items += 1
            Item.list_of_items[self.name] = self.price

    __version__ = '0.1'


done_input = False

while not done_input:
    something = input("Enter your thing's name: ")

    if something == 'done':
        done_input = True
        continue

    listed_price = input("Enter your thing's price: ")

    price_tag = Item(str(something), str(listed_price))
    Item.add_item(price_tag)

for a, b in Item.list_of_items.items():
    print('{} at price {}'.format(a, b))

print(Item.__doc__)
print('version', Item.__version__)


