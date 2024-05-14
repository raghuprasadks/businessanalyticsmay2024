def shopping(totalpurchase):
    discount = 0
    netamount = 0
    discountrate = 0
    if(totalpurchase<=10000):
        discountrate=10
    elif (totalpurchase > 10000 and totalpurchase<=20000):
        discountrate = 20
    elif (totalpurchase > 20000 and totalpurchase <= 30000):
        discountrate = 30
    else:
        discountrate = 35
    discount = (totalpurchase*discountrate)/100
    netamount=totalpurchase-discount
    print("discount on this bill is ",discount)
    print("net payment is ", netamount)
shopping(25000)

