# Jared Lewis, Getting the Time Python
import time

#finrst instance of time in programming
first_time = time.gmtime()
#print(first_time)

#current time in seconds\
current = time.time()
#print(current) #seconds since Jan 1, 1970

#Current date and time like the way we see it
now = time.ctime(current)
#print(now)

#get just a part of the time
local_time = time.localtime(current)
day = local_time.tm_wday
hour = local_time.tm_hour #military time (0-23)
print(hour)