__author__ = 'madevelasco'

from dateutil.parser import parse
from datetime import datetime
from datetime import timedelta

ex = "Sun Nov 29 12:24:04 +0000 2015"

dater = parse(ex)
#res = time.mktime(dater.timetuple())
print(dater)
#print (res*1000)

def millis(dater):
   ms = (dater.days * 24 * 60 * 60 + dater.seconds) * 1000 + dater.microseconds / 1000.0
   return ms

print(millis(dater))



