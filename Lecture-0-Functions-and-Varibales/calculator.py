# default value takes as a input is string.
# int is used to specify the input is a integer.

x = float(input("what's x? "))
y = float(input("what's y? "))

z = round(x + y)

# using  :, formats the number from 1000 to 1,000
print(f"{z:,}")

