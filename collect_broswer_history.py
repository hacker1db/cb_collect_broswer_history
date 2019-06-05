# import logging
# logging.basicConfig()
# logging.getLogger("cbapi").setLevel(logging.DEBUG)


# History: SQLite 3.x database, last written using SQLite version 3024000

from cbapi.response import *
import os
c = CbResponseAPI()

sensor_obj = c.select(Sensor).where("hostname:").first()

# print(sensor_obj)
session = sensor_obj.lr_session()

current_user = (session.create_process(r'last | head | grep " logged in" | cut -d " " -f 1 | sort -u ').decode('utf8'))
browser_list = (session.create_process(r'find ~username/Library/Application\ Support \( -name "History" -o -name "place.sqLite" \) -exec file {} \; 2>&1 | grep SQLite | cut -f 1 -d : '))


# Decoded
decoded = (browser_list).decode().splitlines()
for i in decoded:
    getfiles = session.get_file(i)
    print(getfiles).decode()
# and close session like a good boy 
session.close()


