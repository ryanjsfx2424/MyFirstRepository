## v1: use dictionaries and functions
##     check today's date and display a message if it's a friend's birthday
## v2: use a class

import datetime

birthdays = {
    "ryan": "06/01/1993",
    "danny": "06/03/1993",
    "john": "02/02/2004",
    "jim": "07/05/2019"
    }

today = datetime.datetime.now()
print(str(today))
today = str(today)

print(type(today))
today = today.replace("-", "/")
print(today)

for key in birthdays:
    print(key)
    print(birthdays[key])
    if birthdays[key][:-5] in today:
        print("happy birthday to: ", key)
    #if "/".join(birthdays[key].split("/")[:-1])