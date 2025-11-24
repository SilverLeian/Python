greeting =input("Hi, I'm here to withdraw my savings").lower().strip()

if greeting == "Hello":
    print("$0") 

elif greeting[0] == "h":
    print("$20") 

else:
    print("$100") 