#Jacob Jensen
#9/21/18
import calendar
import time

def gmtnow():
    seconds = calendar.timegm(time.gmtime())
    current_seconds = seconds % 60
    minutes = seconds // 60
    current_minutes = minutes % 60
    hour = minutes // 60
    current_hour = hour % 24

    return current_seconds, current_minutes, current_hour

current_seconds, current_minutes, current_hour = gmtnow()
print (current_hour, " : ", current_minutes, " : ", current_seconds)
    
x = True
while x == True:
    h,m,s = gmtnow()
    print(h,":",m,":",s)


