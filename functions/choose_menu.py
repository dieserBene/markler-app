from classes.Apartment import Apartment
from classes.Room import Room

APARTMENT_OPTIONS = [
    "Create new apartment",
    "Operate on existing apartment",
    "Delete apartment",
    "List all apartments",
]

ROOM_OPTIONS = [
    "Create new room",
    # "Operate on existing room",
    "Delete room",
    "List all rooms",
]

def choose_input():
    try:
        print()
        print("Please choose option by index number")
        choice = int(input(">> "))

        return choice
    
    except:
        print()
        
        print("=" * 35)
        print("Please enter valid number !!!")
        print("=" * 35)

        return None
    
    

def print_options(options):
    print()
    print("-" * 50)

    for i, item in enumerate(options):
        print(f"{i + 1}. {item}")

    print("-" * 50)


def choose_apartment():
    print_options(APARTMENT_OPTIONS)
    print()

    choice = choose_input()

    if choice == None:
        return

    if choice == 1:
        Apartment().create_one()
    elif choice == 2:
        choose_room(Apartment().edit_one())
    elif choice == 3:
        Apartment().delete_one()
    elif choice == 4:
        Apartment().list_data()

def choose_room(index):
    room = Room(index)

    print_options(ROOM_OPTIONS)
    print()

    choice = choose_input()
    
    if choice == 1:
        room.create_one()
    elif choice == 2:
        room.delete_one()
    elif choice == 3:
        room.list_data()

def choose():
    while True:
        choose_apartment()
