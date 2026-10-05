capitals = {"USA": "Washington D.C.",
            "France": "Paris",
            "Japan": "Tokyo",
            "China": "Beijing",
            }
if capitals.get("France"):
    print("The capital of France exists")

else:
    print("The capital does not exist")

    capitals.update({"Germany": "Berlin"})
    capitals.update({"USA": "New York"})
    keys = capitals.keys()
for key in capitals.keys():
   print(key)

values = capitals.values()
for value in capitals.values():
   print(value)

items = capitals.items()
for key, value in capitals.items():
   print(f"{key}: {value}")