"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        current_cart.setdefault(item,0)
        current_cart[item]+=1
    return current_cart
    


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

   
    cart={}
    for item in notes:
        cart.setdefault(item,0)
        cart[item]+=1
    return cart

def update_recipes(ideas, recipe_updates):
    for key, value in recipe_updates:
        ideas[key] = value
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    pass
    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    result = {}

    for item in sorted(cart.keys(), reverse=True):
        quantity = cart[item]
        aisle, refrigerated = aisle_mapping[item]
        result[item] = [quantity, aisle, refrigerated]

    return result
   


def update_store_inventory(fulfillment_cart, store_inventory):
    for item, details in fulfillment_cart.items():
        quantity = details[0]
        store_inventory[item][0] -= quantity

        # 🔥 Important condition
        if store_inventory[item][0] == 0:
            store_inventory[item][0] = 'Out of Stock'

    return store_inventory
