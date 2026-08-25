def display_inventory(inventory):
    total_num = 0
    print("Inventory:")
    for key in inventory:
        print(inventory.get(key), key)
        total_num = total_num + inventory.get(key)
    print('Total number of items:', total_num)

def add_to_inventory(inventory, loot):
    for item in loot:
        if item in inventory:
            inventory[item] = inventory.get(item, 0) + 1
        inventory.setdefault(item, 1)


inventory_1 = {"gold coin": 42, "food": 3, "sword": 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
add_to_inventory(inventory_1, dragon_loot)
display_inventory(inventory_1)

