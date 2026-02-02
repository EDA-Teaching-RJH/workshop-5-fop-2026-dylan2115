def main():
    userInput = input("what is your preferd first name")

    snakeCaseName = ""
    for char in userInput:
        if char.isupper():
            snakeCaseName += "_" + char.lower()
        else:
            snakeCaseName += char
    print(snakeCaseName)
main()
