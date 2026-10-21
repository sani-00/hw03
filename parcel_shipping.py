try:
    weight = float(input("Weight(kg): "))
    if weight <= 0:
        print("Please enter a valid weight")
    else:
        if weight > 20:
            print("Too heavy (max 20 kg)")
        else:
            if weight <= 1:
                cost = 40
            elif weight <= 5:
                cost = 80
            elif weight <= 20:
                cost = 150

            destination = input("Destination(bangkok/other): ")
            if destination != "bangkok" and destination != "other":
                print("Unknown destination")            
            else :
                if destination == "other":
                    cost += 30

                express = input("Express(yes/no): ")
                if express == "yes":   
                    cost *= 2

                    print(f"Shipping cost: {cost} Baht")     
                
except ValueError:
    print("Please enter a valid weight")
