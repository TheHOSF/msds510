from time import strptime
from datetime import *


# Extract month from date string and convert to int
def get_month(month):
    return strptime(''.join(filter(str.isalpha, month)), '%b').tm_mon


# Convert year and month into a date using the first of the month
def get_date_joined(year, month):
    return date(int(year), get_month(month), 1)


# Calculate the time since joined using today's date
def days_since_joined(year, month):
    date_joined = get_date_joined(year, month)
    now = date.today()
    return (now - date_joined).days


# Calculate the number of years since joining
def years_since_joining(year):
    now = date.today()
    return now.year - year


# Convert value to int
def to_int(value):
    return int(value)

# Convert value to boolean
def to_bool(value):
    if value == 'YES':
        return True
    elif value == 'NO':
        return False

    return None


# Strip \n characters from end of value
def clean_notes(value):
    return value.rstrip('\n')


# Cleans up record to be more python friendly
# Converts int fields, boolean values, cleaning strings and updating years_since_joined
def transform_record(record):
    d = {}
    for key in record:
        if key in ['year', 'appearances']:
            d[key] = to_int(record[key])
        elif key.startswith(('death', 'return')):
            d[key] = to_bool(record[key])
        elif key == 'notes':
            d[key] = clean_notes(record[key])
        elif key == 'years_since_joining':
            d[key] = years_since_joining(int(record['year']))
        else:
            d[key] = record[key]
    if d['full_reserve_avengers_intro']:
        d['month_joined'] = get_month(d['full_reserve_avengers_intro'])
    else:
        d['month_joined'] = None
    return d



