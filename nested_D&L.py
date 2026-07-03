guest_list = {'Greg': {'Bananna': 3, 'Apple': 7}, 'Zoe': {'Pie': 2}}

def items_brought(guests, item):
    num_brought = 0
    for k, v in guests.items():
        num_brought = num_brought + v.get(item, 0)
    return num_brought

print("Apples = " + str(items_brought(guest_list, 'Apple')))