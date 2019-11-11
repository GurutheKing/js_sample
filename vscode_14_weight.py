weight  =int(input("Enter the weight: "))
unit  =input("(L)bs or (K)g: ")
if unit.upper()=="L":
    calc_weight =weight * 0.75
    print(f"The weight in kilos:{calc_weight}")
elif unit.upper()=="K":
    calc_weight = weight / 0.75
    print(f"The weight in pounds:{calc_weight}")
else:
    print("Enter either in L or K")
