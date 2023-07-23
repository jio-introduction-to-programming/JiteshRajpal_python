from datetime import datetime , date

# datetime to string
def datetime_to_str_1(dt):
    dates = dt.strftime("%Y-%m-%d")# Convert to format "2023-07-19"
    return dates

def datetime_to_str_2(dt):
    dates = dt.strftime("%y-%m-%d")# Convert to format "23-07-19"
    return dates

def datetime_to_str_3(dt):
    dates = dt.strftime("%B %d, %Y")# Convert to format "July 19, 2023"
    return dates
def datetime_to_str_4(dt):
    dates = dt.strftime("%b %d, %Y") # Convert to format "Jul 19, 2023"
    return dates
def datetime_to_str_5(dt):
    dates = dt.strftime("%d %B %Y") # Convert to format "19 July 2023"
    return dates
def datetime_to_str_6(dt):
    dates = dt.strftime("%A %B %d, %Y") # Convert to format "Wednesday July 19, 2023"
    return dates
def datetime_to_str_7(dt):
    dates = dt.strftime("%a %B %d, %Y") # Convert to format "Wed July 19, 2023"
    return dates
def datetime_to_str_8(dt):
    dates = dt.strftime("%Y-%m-%d %H:%M:%S") # Convert to format "2023-07-19 10:30:45"
    return dates
def datetime_to_str_9(dt):
    dates = dt.strftime("%H:%M:%S") # Convert to format "10:30:45"
    return dates
def datetime_to_str_10(dt):
    dates = dt.strftime("%H:%M %p") # Convert to format "10:30 AM"
    return dates

# string to datetime
def str_to_datetime_1(s):
    dates = datetime.strptime(s,"%Y-%m-%d") # Convert from format "2023-07-19"
    return dates

def str_to_datetime_2(s):
    dates = datetime.strptime(s,"%y-%m-%d") # Convert from format "23-07-19"
    return dates

def str_to_datetime_3(s):
    dates = datetime.strptime(s,"%B %d, %Y") # Convert from format "July 19, 2023"
    return dates

def str_to_datetime_4(s):
    dates = datetime.strptime(s,"%b %d, %Y")# Convert from format "Jul 19, 2023"
    return dates

def str_to_datetime_5(s):
    dates = datetime.strptime(s,"%d %B %Y")# Convert from format "19 July 2023"
    return dates

def str_to_datetime_6(s):
    dates = datetime.strptime(s,"%A %B %d, %Y")# Convert from format "Wednesday July 19, 2023"
    return dates

def str_to_datetime_7(s):
    dates = datetime.strptime(s,"%a %B %d, %Y")# Convert from format "Wed July 19, 2023"
    return dates

def str_to_datetime_8(s):
    dates = datetime.strptime(s,"%Y-%m-%d %H:%M:%S") # Convert from format "2023-07-19 10:30:45"
    return dates

def str_to_datetime_9(s):
    dates = datetime.strptime(s,"%H:%M:%S")# Convert from format "10:30:45"
    return dates

def str_to_datetime_10(s):
    dates = datetime.strptime(s,"%H:%M %p")# Convert from format "10:30 AM"
    return dates
