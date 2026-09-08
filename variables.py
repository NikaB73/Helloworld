# print("hello world")
for i in range(1, 11):
    print(i*"*")
  
# name = "derek"
# age = 14
# gpa = 3.5
# is_student = True
# print(type(name))
# print(type(age))
# print(type(gpa))
# print(type(is_student))

# age = float(age)
# gpa = int(gpa)
# print(type(age))
# print(type(gpa))
# name = input("Enter your name: ")
# result = len(name)
#result = (name.isalpha())#checks if the string contains only letters
#result = (name.isdigit())#checks if the string contains only numbers
phone_number = input("Enter your phone number: ")
phone_number = phone_number.count("1")
print(phone_number)