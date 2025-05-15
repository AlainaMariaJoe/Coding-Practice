def km_to_mile (val):
    return val * 0.621371

def km_to_m (val):
    return val * 1000

inp = float(input("Enter the value in km: "))
print(f"{inp} km : {km_to_mile(inp): .2f} miles")
print(f"{inp} km : {km_to_m(inp): .2f} m")