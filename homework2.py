import os
from collections import Counter

user_inventory = 'user_inventory.txt'

if not os.path.exists(user_inventory):
    with open(user_inventory, 'w') as file:
        pass


class Colors:
    RESET = '\033[0m'
    BOLD = '\033[01m'
    UNDERLINE = '\033[04m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'


def color_print(text, color):
    print(f"{color}{text}{Colors.RESET}")


def add_item():
    u_items = input(f"{Colors.BLUE}Enter item name: >>>: {Colors.RESET}")
    u_items = u_items.capitalize()
    with open(user_inventory, 'a') as user_file:
        user_file.write(u_items + '\n')
    color_print(f'Added {u_items} to your inventory.', Colors.GREEN)


def show_items():
    if not os.path.exists(user_inventory):
        color_print('Inventory is empty.', Colors.RED)
        return
    with open(user_inventory, 'r') as user_file:
        items = user_file.readlines()
    items = [item.strip() for item in items]
    item_counts = {item: items.count(item) for item in set(items)}

    if not item_counts:
        color_print('Inventory is empty.', Colors.RED)
        return

    for index, (inv_item, inv_count) in enumerate(item_counts.items(), start=1):
        color_print(f'{index}. {inv_item}: {inv_count}', Colors.MAGENTA)

    return item_counts


def delete_item():
    if not os.path.exists(user_inventory):
        color_print('Inventory is empty.', Colors.RED)
        return
    with open(user_inventory, 'r') as user_file:
        items = user_file.readlines()
    if len(items) == 0:
        color_print('Inventory is empty.', Colors.RED)
        return
    color_print('Select item number', Colors.RED)
    item_counts = show_items()

    try:
        u_input = int(input(f"{Colors.BLUE}>>>: {Colors.RESET}"))
        if 0 < u_input <= len(item_counts):
            selected_item = list(item_counts.items())[u_input - 1]
            color_print(f"Selected item: {selected_item[0]} ({selected_item[1]} items)", Colors.GREEN)

            with open(user_inventory, 'r') as user_file:
                items = user_file.readlines()

            updated_items = [item.strip() for item in items if item.strip() != selected_item[0]]

            with open(user_inventory, 'w') as user_file:
                for item in updated_items:
                    user_file.write(item + '\n')

    except ValueError:
        color_print('Item delete error.', Colors.RED)


def game_start():
    while True:
        try:
            color_print("Game menu:", Colors.CYAN)
            color_print("1. Add item", Colors.BOLD)
            color_print("2. Your inventory", Colors.BOLD)
            color_print("3. Delete item", Colors.BOLD)
            color_print("4. Exit", Colors.BOLD)
            u_input = input(f"{Colors.BLUE}>>>: {Colors.RESET}")
            if u_input.lower() == '4':
                color_print("Game exit:", Colors.CYAN)
                return
            elif u_input.lower() == '3':
                delete_item()
            elif u_input.lower() == '2':
                show_items()
            elif u_input.lower() == '1':
                add_item()
            else:
                color_print('Error, try again.', Colors.RED)
        except ValueError:
            color_print('Error, try again.', Colors.RED)


game_start()
