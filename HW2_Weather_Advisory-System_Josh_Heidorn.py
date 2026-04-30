temp = int(input("Enter temperature: "))
rain = input("Is it raining? (yes/no): ").lower()

if temp > 100:
    print("EXTREME HEAT WARNING: Stay indoors!")
elif temp > 85:
    if rain == "yes":
        print("Warm rain — watch for flash floods.")
    else:
        print("Hot and dry — stay hydrated.")
elif temp >= 60:
    if rain == "yes":
        print("Grab an umbrella!")
    else:
        print("Nice weather — enjoy your day!")
elif temp >= 32:
    print("It's cold — bundle up!")
else:
    print("FREEZE WARNING: Roads may be icy!")