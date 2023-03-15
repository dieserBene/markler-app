import json


# Wird ausgeführt wenn Programm start
# Schaut ob Daten verfügbar sind, wenn nicht "registriert" sich der Nutzer

def initialisation():
    with open("db.json", "r+") as file: 
        try: 
            data = json.loads(file.read())
            username = data["username"]

            print()
            return print(f"Welcome back {username}")
            
        except:
            print()
            username = input("Please enter your name: ")
            
            file.write(json.dumps({
                "username": username,
                "apartments": []
            }, indent=4 ))

            print()
            return print(f"Welcome {username}")

