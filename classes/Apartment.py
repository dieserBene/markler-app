import json


class Apartment:
    def __init__(self) -> None:
    
        pass

    def create_one(self):

        print()
        name = input("Please enter new apartments name: ")

        with open("db.json", "r+") as file:
            data = json.loads(file.read())

        data["apartments"].append({
            "name": name, 
            "rooms": []
        })

        with open("db.json", "w") as file:
            file.write(json.dumps(data, indent=4))

        print()
        return print(f"Successfully added apartment '{name}' ")
    
    def edit_one(self):

        with open("db.json", "r") as file:
            data = json.loads(file.read())

            print()
            print("-" * 35)

            for i, item in enumerate(data["apartments"]):
                name = item["name"]

                print(f"{i + 1}. {name}")

            print("-" * 35)

        print()
        print("Choose apartment to edit by index number")
        choice = int(input(">> "))

        return choice - 1 

    def delete_one(self):

        with open("db.json", "r+") as file:
            data = json.loads(file.read())

        print()
        for i, item in enumerate(data["apartments"]):
            name = item["name"]

            print(f"{i + 1}. {name}")

        print()
        print("Choose apartment to delete by index number")
        choice = int(input(">> "))

        data["apartments"].pop(choice - 1)
        
        with open("db.json", "w") as file:
            file.write(json.dumps(data, indent=4))

        return print("Succesfully deleted")

    def list_data(self):
        
        with open("db.json", "r") as file:
            data = json.loads(file.read())

            if len(data["apartments"]) == 0:
                return print("There are no apartments yet")
            
            apartments = data["apartments"]

            print()
            print(f"There are {len(apartments)} apartments")
            print("-" * 35)

            for i, item in enumerate(apartments):
                name = item["name"]

                print(f"{i + 1}. {name}")

        return ""
