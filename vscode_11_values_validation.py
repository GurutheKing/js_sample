name ="Gururajan S"
temperature = int(input("Please ente the temperature: "))
if temperature > 90 and temperature < 97:
    print(f"the current temperature is {temperature} and its really good!!")
elif temperature == 90:
    print(f"the current temperature is {temperature} and its about to get good!!")
elif temperature >= 97:
    print(f"the current temperature is {temperature} and its hot!!")
else:
    print(f"the current temperature is {temperature} and its cold!!")

print(f"Have a wonderful day {name}")