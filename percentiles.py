# Number values in the survey
survey = [15, 34, 14, 20, 32, 27, 22, 11, 40, 25, 24, 13, 10, 16, 6, 31, 3, 5, 9, 18]

# assigns variable number of values in the list and prints
list_length = (len(survey))
print(f"There are {list_length} values in the list.\n")

# sorts numbers into ascending order and prints it out
survey.sort()
print(f"The order from lowest to highest: {survey}\n")

# request percentile input, find amount of values, and plug in (length of survey into the) formula
percentile = int(input("Enter percentile: "))
n = len(survey)
p_formula = n * (percentile / 100)
print()
print(f"Position: {p_formula}")

# import round up function for p_formula (non-integer value)
import math
roundup = math.ceil(p_formula)
print(f"Your percentile is position {roundup} in the survey.")

# pull position from ordered list using index method
percentile_answer = roundup - 1

print(f"{percentile}th Percentile = {survey[percentile_answer]}")
