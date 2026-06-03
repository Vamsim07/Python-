# Logical operator (AND, OR, NOT)

temp = int(input("enter the Temprator at outside : "))

# if -100 <= temp <= 10 : 
#     print("the Temperator is cool, and Njoy the snow")

# elif not(temp >= 10 and temp <= 30):
#     print("mistaken")

# elif temp >= 10 and temp <= 30:    # Using AND Operator
#    print("The Temperator is Great")
    

# else:
#     print("The Temprator is high..! Be Hydrate")

if (temp >= 10 and temp <= 30) or (-100 <= temp <= 10) :
    print("good whether")

else:
    print("Avoiding outside..!")