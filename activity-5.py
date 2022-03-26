hrs = input("Enter Hours:")
h = float(hrs)
rates= input("Enter rate per hour:")
r = float(rates)
houraboverate = 0
if h > 40:
    hourabove = h - 40
    houraboverate = hourabove * (1.5 * r)
    hourless = 40
hourlyrate = (hourless * r ) + houraboverate
print(hourlyrate)
