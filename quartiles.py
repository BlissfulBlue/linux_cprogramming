# Number values in the survey
survey = [43, 40, 25, 40, 33, 45, 35, 52, 31, 47, 48, 51, 33, 32, 44, 57, 51]

# assigns variable number of values in the list and prints
list_n = (len(survey))
print(f"There are {list_n} values in the list.\n")

# sorts survey into ascending order and prints it out
survey.sort()
print(f"The order from lowest to highest: {survey}\n")

# sleep a program
import time
time.sleep(2)

# import math functions, (round up), minimum, Q1, median, Q3, maximum, and interQ(Q3 - Q1)
import math
import numpy as np

# minimum
minimum = min(survey)
print(f"Minimum = {minimum}\n")


# sleep a program
import time
time.sleep(1.2)


# n of list (survey)
n = len(survey)


# quartile 1 and position
q1 = np.percentile(survey, [25])
print(f"Quartile 1 = {q1}\n")


# sleep a program
import time
time.sleep(1.2)


# quartile 2 (median)
def calculate_median(survey):
    if n % 2 == 0: # if there is an even amount of numbers in the list
        median = (survey[int(n / 2) - 1] + survey[int(n / 2)]) / 2
    else: # if there is an odd amount of numbers in the list
        median = survey[int(n / 2)]
    return median
median = calculate_median(survey)
print(f"Quartile 2 = {median}\n")


# sleep a program
import time
time.sleep(1.2)


# quartile 3 and position
q3 = np.percentile(survey, [75])
print(f"Quartile 3 = {q3}\n")


# sleep a program
import time
time.sleep(1.2)


# maximum
maximum = max(survey)
print(f"Maximum = {maximum}")
