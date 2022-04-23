g = -(int(input()) - int(input()))
if g <= 0:
    print("Congratulations, you are within the speed limit!")
elif 1 <= g <= 20:
    print("You are speeding and your fine is $100.")
elif 21 <= g <= 30:
    print("You are speeding and your fine is $270.")
elif g >= 31:
    print("You are speeding and your fine is $500.")
