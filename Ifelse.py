# If elif solution
sal = int(input("enter the sal"))
if(sal>=50000):
    p = int(input("enter the p units"))
    c = int(input("enter the c units"))
    u = c - p
    r = 0
    if (u >= 1000):
        r = u * 10
    elif (u >= 800):
        r = u * 8
    elif (u >= 600):
        r = u * 6
    elif (u >= 400):
        r = u * 4
    elif (u >= 200):
        r = u * 2
    elif (u >= 100):
        r = u * 1
    else :
         print('no need to pay',r)

    print('Base amount to pay:', r)

    gtype = input("enter the gtype m/f").lower().strip()
    ctype = input("enter the etypr e/n").lower().strip()

    if (gtype == 'f') and (ctype == 'e'):
        if (r >=10000):
            v = r*0.8
            print(v,"1000 voucher")
        elif (r>=5000):
            v = r*0.90
            print(v,"500 voucher")
        elif (r>=2000):
            v = r*0.95
            print(v,"300 voucher")
        else:
            print("no voucher")

    elif (gtype == 'm' ) and (ctype == 'e'):
        if (r>=10000):
            v = r*0.9
            print(v,"800 voucher")
        elif (r>=5000):
            v = r*0.95
            print(v,"400 voucher")
        elif (r>=2000):
            v = r*0.97
            print("200 voucher")
        else:
            print("no voucher")

    elif (gtype == 'f' ) and (ctype == 'n'):
        if (r>=10000):
            v = r*0.80
            print(v,"no voucher")
        elif (r>=5000):
            v = r*0.90
            print(v,"no voucher")
        elif (r>=2000):
            v = r*0.95
            print(v,"no voucher")
        else:
            print("no voucher")

    elif (gtype == 'm' ) and (ctype == 'n'):
        if (r>=10000):
            v = r*0.90
            print(v,"no voucher")
        elif (r>=5000):
            v = r*0.95
            print(v,"no voucher")
        elif (r>=2000):
            v = r*0.97
            print(v,"no voucher")
        else:
            print("no voucher")
else:
    print("no need to pay")