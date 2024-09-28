n = int(input())

time = []
for _ in range(n):
    time.append(int(input()))

ninety_mins_start = 0
using_ninety_mins_ticket = False
payment_within_ninety_mins = 0
oneday_start = 0
using_oneday_ticket = False
payment_within_oneday = 0

for i in range(n):
    # print("90:", ninety_mins_start)
    # print("oneday:", oneday_start)
    # print("time:", time[i])
    
    if i == 0:
        print(20)
        payment_within_oneday += 20
        payment_within_ninety_mins += 20
        continue
    
    if using_oneday_ticket:
        if time[oneday_start] + 1439 >= time[i]:
            print(0)
        else:  # expired
            print(20)
            using_oneday_ticket = False
            oneday_start = i
            ninety_mins_start = i
            payment_within_oneday = 20
            payment_within_ninety_mins = 20
        
        continue
    
    if using_ninety_mins_ticket:
        if time[ninety_mins_start] + 89 >= time[i]:
            print(0)
        else:  # expired
            using_ninety_mins_ticket = False
            ninety_mins_start = i
            payment_within_ninety_mins = 0
            
            if time[oneday_start] + 1439 >= time[i]:
                if payment_within_oneday >= 100:  # get one day ticket
                    print(120 - payment_within_oneday)
                    payment_within_oneday = 0
                    payment_within_ninety_mins = 0
                else:  # don't get one day ticket
                    print(20)
                    payment_within_oneday += 20
                    payment_within_ninety_mins += 20
            else:  # cannot buy one day ticket
                print(20)
                oneday_start = i
                payment_within_oneday = 20
                payment_within_ninety_mins = 20
        
        continue
    
    # not using any ticket
    # get one day ticket?
    if time[oneday_start] + 1439 >= time[i]:
        if payment_within_oneday >= 100:
            print(120 - payment_within_oneday)
            using_oneday_ticket = True
            payment_within_oneday = 0
            continue
    else:
        oneday_start = i
        payment_within_oneday = 0
    
    # get three hour ticket?
    if time[ninety_mins_start] + 89 >= time[i]:
        if payment_within_ninety_mins > 30:
            payment = 50 - payment_within_ninety_mins
            print(payment)
            using_ninety_mins_ticket = True
            payment_within_ninety_mins = 0
            payment_within_oneday += payment
            continue
    else:
        ninety_mins_start = i
        payment_within_ninety_mins = 0
    
    # not using any ticket
    print(20)
    payment_within_oneday += 20
    payment_within_ninety_mins += 20
