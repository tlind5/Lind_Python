from datetime import date, timedelta

today = date.today()
activeweekend = today - timedelta(days = 8)
activeweekstart = today - timedelta(days = 14)

myend = activeweekend.strftime("%m%d%y")
mystart = activeweekstart.strftime("%m%d%y")

print(myend,mystart)

a = "me"
b= "I hate {q} soooo much I am {age} years old !!".format(q=a, age=345)

print(b)