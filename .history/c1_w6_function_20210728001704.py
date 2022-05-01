
def computepay(h,r):
    if h > 40:
        pay = (h-40)*1.5*r + 40*r
    else:
        pay = h*r
    return pay

hours   = input("enter your hours:")
rate    = input("enter your rate:")
hours_f = float(hours)
rate_f  = float(rate)

p = computepay(hours_f,rate_f)
print("Pay",p)
