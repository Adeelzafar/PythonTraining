def computepay(h, r):
    overtime = 0
    if h > 40:
        hnew = h - 40
        overtime = hnew * r * 0.5
    totalpay = h * r + overtime
    return totalpay

hrs = input("Enter Hours:")
rate = input ("Enter Rate:")
h = float (hrs)
r = float (rate)
p = computepay(h, r)
print("Pay", p)
