# empirical rule

mean = float(input("Input mean: "))
deviation = float(input("Input standard deviation: "))


# calvulate empirical rule
empir_rule_neg1 = mean - deviation # 68% of data values
empir_rule_neg2 = mean - (deviation * 2) # 95% of data values
empir_rule_neg3 = mean - (deviation * 3) # all or almost all data values

empir_rule_1 = mean + deviation # 68% of data values
empir_rule_2 = mean + (deviation * 2) # 95% of data values
empir_rule_3 = mean + (deviation * 3) # all or almost all data values

# Find a way to categorize and print the data
print(f"\n68% of the data values are between {empir_rule_neg1:.2f} and {empir_rule_1:.2f}"
      f"\n95% of the data values are between {empir_rule_neg2:.2f} and {empir_rule_2:.2f}"
      f"\nAll or almost all of the data values are between {empir_rule_neg3:.2f} and {empir_rule_3:.2f}")

