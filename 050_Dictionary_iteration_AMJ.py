Employee = {"Miami": 32 , "Sen": 19, "Doe" : 27}
#Solution 1 - items()
for key, val in Employee.items():
    print(key, val)

#Solution 2 
for key in Employee:
    print(key, Employee[key])

#Solution 3 - keys(), values()
for key in Employee.keys():
    print(key)
for val in Employee.values():
    print(val)

