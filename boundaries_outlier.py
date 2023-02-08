# Boundary and Outlier Calculator

# calculate lower and upper boundaries using inputted quartiles
low_q = int(input("Enter lower quartile: "))
high_q = int(input("Enter upper quartile: "))
print()

# interquartile range
iqr = high_q - low_q
print(f"IQR = {iqr}")

boundary_L = low_q - (1.5 * iqr)
boundary_H = high_q + (1.5 * iqr)

print(f"\nLower boundary = {boundary_L}\n"
      f"Upper boundary = {boundary_H}")
