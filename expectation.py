# expectation probability
pizza = [("no damage", 788), ("minor", 72), ("major", 26)]
def crust_order(pizza):
    total_sold = 0
    
    for crust in pizza:
        crust_type, crust_sold = crust  # crust = each individual tuple. Both name and individual number sold
        total_sold += crust[1]  # add up all the total crusts sold
        
        print(f"Total of crusts sold: {total_sold}")
    
    expv = int(input("Expectation value: "))
    
    while True:
        label = str(input("Crust Type: "))
    
        amount_sold = None
        for crust_type, crust_sold in pizza:
            if crust_type == label:
                amount_sold = crust_sold
                print(f"You chose {label} crust which sold {amount_sold}.")
                
                ratio = amount_sold / total_sold
                print(f"Ratio: {amount_sold} / {total_sold} = {ratio}")
                
                expectation = (amount_sold * expv) / total_sold
                print(f"Expectation number = {expectation:.2f}")
                return
            
crust_order(pizza)
