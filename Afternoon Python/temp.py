temperature = 60    # fahrenheit

if temperature > 80:
    # indented
    print("Wear some shorts! And put on sunscreen!")

elif temperature > 60:
    print("Wear pants.")

elif temperature > 30:
    print("Wear a jacket.")

# stands for "else if"
elif temperature > 0:
    print("Stay inside.")

else:
    print("You must live in Siberia.")
