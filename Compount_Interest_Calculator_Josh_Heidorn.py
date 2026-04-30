principal = float(input("Principal: "))
rate = float(input("Rate (%): "))
years = int(input("Years: "))

balance = principal

for year in range(1, years + 1):
    balance = balance * (1 + rate / 100)
    print(f"Year {year}: ${balance:.2f}")

interest = balance - principal
print(f"Total interest earned: ${interest:.2f}")
