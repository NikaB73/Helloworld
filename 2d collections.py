fruits = ["banana", "apple", "cherry", "strawberry"]
vegetables = ["carrot", "broccoli", "spinach", "potato"]
meats =["chicken", "beef", "pork", "turkey"]

groceries = [fruits, vegetables, meats]

for collection in groceries:
    for food in collection:
         print(food, end="")


num_pad = {{1, 2, 3},
          {4, 5, 6},
          {7, 8, 9},
          {"*", 0, "#"}}

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()