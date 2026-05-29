#Type Casting : The Data Change one Data type to another data type
# example : str(), int(), Float(), Bool()

Age = 25
age = str(Age)
print(type(age))

Number = float(Age)
print(Number)

name = ""
name = bool(name)
print(name)

Name = "vamsi"
name = bool(Name)
print(name)

Name = input ('What is your name :')
Age = input ('Your Age :')
Responce = input(f"What Will you do at the age of {int(Age)+1} :")

print(Name)
print(Age)
print(Responce)