#functions, the coffee machine must accept coins (intergers) 50p and lower so 50,25,10,5,2,1p as coins are inseted
#take the remainder of the price and make it the new total price un till the total is achived then it need to 
#give back the change 

#non-functions, the machine needs to be able to turn away non intergers and ask for the correct input which is an 
#price





price = 99
accepted_coin = [50,25,10,5,2,1]

print("Welcome to Unit_CoffeeMachine ")

while price > 0: 
    print(f"price:{price}p")

    coin = int(input("insert coins now (50,25,10,5,2,1): "))

    if coin in accepted_coin:
        price -= coin 
    else:
        print(f"inputed {coin} coin is not accepted you cunt")

print("_" * 20)
print("procesing payment")
print("be paciant")
print("purchase compleate")
print("thank you for your purchase")
print("please enjoy")

change_owed = abs(price)
print(f"changed owed: {change_owed}p")