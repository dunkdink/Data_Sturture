x = int(input("Enter wind speed (km/h) : "))
print(" *** Wind classification ***")
if x<0:
    print("!!!Wrong value can't classify.")
else:
    if x<52:
        ans="Breeze"
    elif x<56:
        ans="Depression"
    elif x<102:
        ans="Tropical Storm"
    elif x<209:
        ans="Typhoon"
    elif x>209:
        ans="Super Tyhoon"
    print(f"Wind classification is {ans}")
