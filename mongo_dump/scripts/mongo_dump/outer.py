from datetime import *
from time import strftime
import datetime
import os
import sys
start_date = date(2014,04,14)
end_date = date(2014,4,15) # range yield one day less the the end date
#print start_date, "to ", end_date


def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

for single_date in daterange(start_date, end_date):
     x=strftime("%Y-%m-%d", single_date.timetuple())
     y = single_date+timedelta(1)
     y=strftime("%Y-%m-%d", y.timetuple())
     print "collecting data for dates between ", x, " and ",y
     str1 ="python mongo_dump.py "+x +" " +y + ' >> a.txt'
#    str1 ="python mongo_restore.py "+x +" " +y
     os.system(str1)
