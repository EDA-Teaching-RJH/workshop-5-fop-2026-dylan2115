price = 75
accepted_coin = [50,25,10,5]

print("Welcome to Unit_CoffeeMachine ")

while price > 0: 
    print(f"price:{price}p")

    coin = int(input("insert coins now (50,25,10,5): "))

    if coin in accepted_coin:
        price -= coin 
    else:
        print(f"inputed {coin} coin is not accepted you cunt")

print("_" * 20)
print("procesing payment")
print("purchase compleate")
print("thank you for your purchase")
print("please enjoy")

change_owed = abs(price)
print(f"changed owed: {change_owed}p")