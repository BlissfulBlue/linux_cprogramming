# Number values in the survey
survey = [10, 12, 6, 11, 8, 13]


# sorts numbers into ascending order and prints it out
survey.sort()
print(f"The order from lowest to highest: {survey}")


# assigns variable number of values in the list and prints
list_length = (len(survey))
print(f"There are {list_length} values in the list.")


# calculates the mean by sum of list / number of values and prints it out
mean = sum(survey) / (len(survey))
print(f"The mean is {mean}\n")


# takes each individual number, subtracts by mean, squares it, and prints it
subtract_xbar = []
for value in survey:
    subtract_xbar.append(value - mean)
    squared = []
    for deviation in subtract_xbar:
        squared.append(deviation ** 2)
print(f"Before squaring: {subtract_xbar}")
print(f"After squaring: {squared} (Worry about this part)")
print()

# adds the sum of all squared numbers and print as integer
sigma = sum(squared)
print((f"Sum of list after squaring: {sigma}"))

# divide sigma (sum of all squared values) by len(squared) (number of values in list: squared), then square root it, and print it.
import math

#################################

# uncomment for sample deviation
sample_dev = len(survey) - 1
print(f"n - 1 = {sample_dev} (To understand, look at formula)")
print()
Nminus1_divide = sigma / sample_dev
print("Answer:\n")
print(math.sqrt(Nminus1_divide))

#################################

# uncomment for population deviation
# n_divide = sigma / len(survey)
# print(math.sqrt(n_divide))
