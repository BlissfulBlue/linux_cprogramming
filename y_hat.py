# y hat least squares regression program

# variables

# n (amount of numbers in list)
x_chart = [80, 76, 85, 89, 87, 78, 80, 81]
y_chart = [80, 81, 85, 86, 82, 78, 81, 83]

n = len(x_chart)

# x chart sum
x_sum = sum(x_chart)
print(f"Sum of x chart: {x_sum:.1f}")

# y chart sum
y_sum = sum(y_chart)
print(f"Sum of y chart: {y_sum:.1f}")



# xy product
result = []
for i in range(len(x_chart)):
    result.append(x_chart[i] * y_chart[i])
    
print(f"\nProduct list of x * y = {result}")

xy_prod = sum(result)
print(f"Sum of xy = {xy_prod}")



# x^2 sum
squared_x = []
for x in x_chart:
    squared_x.append(x ** 2)
    
print(f"\nSquared values of x_chart: {squared_x}")

x2_sum = sum(squared_x)
print(f"Sum of x_chart squared: {x2_sum}")

# nominator
m_nom = n * (xy_prod) - (x_sum * y_sum)

# denominator
m_denom = n * (x2_sum) - (x_sum) ** 2



# slope
mx = (m_nom / m_denom)
print(f"\nSlope = {mx:.4f}x")

# y-intercept
b = (y_sum - (mx * x_sum)) / n
print(f"y-intercept = {b:.4f}")
