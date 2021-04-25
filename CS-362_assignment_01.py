def divcheck(m,n):
    return True if m % n == 0 else False

x = int(input("Input: "))

if (divcheck(x,4)):
    if (divcheck(x,100)):
        if (divcheck(x,400)):
            print("Output ", x, "is a leap year")
        else:
            print("Output ", x, "is not a leap year")
    else:
        print("Output ", x, "is  a leap year")
else:
    print("Output ", x, "is not a leap year")

