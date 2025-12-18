temora={
    "vanila cake":5000,
    "mango cake":2000,
    "orange cake":2500
    }

key=input("enter the key:").lower()
if key in temora:
    print("value",temora[key])
else:
    print("Not Found")
