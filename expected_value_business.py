# computing expected value (business application)
def business():
    def_percent = []
    occurance = []
    while True:
        # the chance it will be defective
        defect = (input("Defectiveness % (enter string to end): "))
        
        try:
            defect = float(defect)
            def_percent.append(defect)
            
            # how many times will this happen? (once if only one defect percentage inputted)
            occur = float(input("Occurance: "))
            occurance.append(occur)
            
        except ValueError:
            chance = []
            for i in range(len(def_percent)):
                product = def_percent[i] * occurance[i]
                chance.append(product)
                sum_chance = sum(chance)

            print(f"\nPotential Product Error: {sum_chance}")
            
            sell_price = int(input("How much is each unit sold for? "))
            
            # E (subtract from desired profit)
            big_e = int(sum_chance * sell_price)
            print(f"\nE = {big_e} (Subtract this from the said profit).")
            
            # desired profit
            dp = int(input("Said Profit: "))
            
            profit = dp - big_e
            
            if profit < 0:
                print(f"\nThe company is losing ${profit}")
            elif profit > 0:
                print(f"\nThe company is making ${profit}")
            elif profit == 0:
                print(f"\nThe company is not making any money. (Profit = {profit})")
            
            break
         
business()
