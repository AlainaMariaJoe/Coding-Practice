def km_to_miles(km):
    return round(km * 0.621371, 1)

n = float(input("Enter Kilometer : "))
print("Miles : ", km_to_miles(n))