# calculates the z score

data_value = int(input("Enter data value: "))
mean = int(input("Enter mean: "))
standard_dev = int(input("Enter standard deviation: "))

z_score = (data_value - mean) / standard_dev
z_abs = abs((data_value - mean) / standard_dev)


# print(f"\nz-score calculated = {z_score}")

# make an if statement that states standard dev is below or above the mean
if z_score < 0:
    print(f"\nThe standard deviation is {z_abs:.2f} BELOW the mean. ({z_score})")
else:
    print(f"\nThe standard deviation is {z_abs:.2f} ABOVE the mean. ({z_score})")
