"""
Project:newtwo
Author:swayam
Description:Shorting
Portability:python
Version:1.00
Date:21/06/2019
"""
from datetime import datetime
import pytz
utc_time = datetime.utcnow()
tz = pytz.timezone('America/St_Johns')

utc_time =utc_time.replace(tzinfo=pytz.UTC)
st_john_time=utc_time.astimezone(tz)
print(st_john_time)