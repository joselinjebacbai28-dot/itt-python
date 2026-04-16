from collections import OrderedDict

if __name__ == "__main__":
    n = int(input())
    inventory = OrderedDict()
    
    for _ in range(n):
        line = input().rpartition(' ')
        item_name = line[0]
        price = int(line[2])
        inventory[item_name] = inventory.get(item_name, 0) + price
     for item, net_price in inventory.items():
        print(f"{item} {net_price}")
