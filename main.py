import math

x = 4.999

x_but_int = int(x)
x_but_rounded = round(x) # avrunda
x_but_rounded_down = math.floor(x) # avrunda alltid neråt
x_but_rounded_up = math.ceil(x) # avrunda alltid uppåt

print(x_but_rounded)

y = 43
y_but_float = float(y)
print(y_but_float)

a = input("Ge mig ett värde på a! ")
b = input("Ge mig ett värde på b! ")

a_but_int = int(a)
b_but_int = int(b)

sum = a_but_int + b_but_int

print(sum)