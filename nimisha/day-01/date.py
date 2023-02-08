import datetime
#datetime object is called to show date and time
today = datetime.datetime.today()


d=today.strftime("%B/%d,/%Y %H:%M:%S")
#for getting the strfunction give capital value like '%B'

print("current date & time =", d)