import json

class Room:
    def __init__(self, apartment_index) -> None:
        self.apartment_index = apartment_index
        self.apartment = self.get_apartment()

    def create_one(self):

        print()
        name = input("Please enter new rooms name: ")
        length = int(input("Please enter your rooms length in m: "))
        width = int(input("Please enter your rooms width in m: "))
        total = width + length

        with open("db.json", "r+") as file:
            data = json.loads(file.read())

        object = self.apartment

        object["rooms"].append({
            "name": name,
            "length": length,
            "width": width,
            "total": total
        })

        data["apartments"][self.apartment_index]["rooms"] = object["rooms"]

        with open("db.json", "w") as file:
            file.write(json.dumps(data, indent=4))

        print()
        return print(f"Successfully added room '{name}' ")
    
    def delete_one(self):
        with open("db.json", "r+") as file:
            data = json.loads(file.read())

        print()
        for i, item in enumerate(data["apartments"][self.apartment_index]["rooms"]):
            name = item["name"]

            print(f"{i + 1}. {name}")

        print()
        print("Choose room to delete by index number")
        choice = int(input(">> "))

        data["apartments"][self.apartment_index]["rooms"].pop(choice - 1)
        
        with open("db.json", "w") as file:
            file.write(json.dumps(data, indent=4))

        return print("Succesfully deleted")

    def edit_one(self):
        pass

    def list_data(self):
        with open("db.json", "r") as file:
            data = json.loads(file.read())

        if len(data["apartments"][self.apartment_index]["rooms"]) == 0:
            return print("There are no rooms yet")
        
        print()
        for i, item in enumerate(data["apartments"][self.apartment_index]["rooms"]):
            name = item["name"]
            length = item["length"]
            width = item["width"]
            total = item["total"]

            print(f"{i + 1}. {name} / {total} squaremeters")    

        return ""

    def get_apartment(self):

        with open("db.json", "r") as file:
            data = json.loads(file.read())

        object = data["apartments"][self.apartment_index]

        return object
