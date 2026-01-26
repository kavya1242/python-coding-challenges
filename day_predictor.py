
dayinput=input()
shiftdays=int(input())
weekdays=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
if dayinput not in weekdays:
    print("invalid")
else:

    dayindex=weekdays.index(dayinput)
    total= (dayindex+shiftdays-1)%7
    print(weekdays[total])