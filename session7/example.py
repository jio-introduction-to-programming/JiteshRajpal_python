from datetime import datetime, date, time, timedelta

# def datetime_to_str_1(dt):
#     dates = dt.strftime("%Y-%m-%d")# Convert to format "2023-07-19"
    
#     return dates


# def test_datetime_to_str_1():
#     assert datetime_to_str_1(date(2023, 7, 19)) == "2023-07-19"
    

def datetime_to_str_1(dt):
    dates = dt.strftime("%Y-%m-%d") # Convert to format "2023-07-19"
    return dates

def test_datetime_to_str_1():
    assert datetime_to_str_1(date(2023, 7, 19)) == "2023-07-19"


def datetime_to_str_7(dt):
    dates = dt.strftime("%a %B %d, %Y") # Convert to format "Wed July 19, 2023"
    return dates

def test_datetime_to_str_7():
    assert datetime_to_str_7(datetime(2023, 7, 19)) == "Wed July 19, 2023"




def datetime_to_str_8(dt):
    dates = dt.strftime("%Y-%m-%d %H:%M:%S") # Convert to format "2023-07-19 10:30:45"
    return dates
def datetime_to_str_9(dt):
    dates = dt.strftime("%H:%M:%S") # Convert to format "10:30:45"
    return dates

def test_datetime_to_str_8():
    assert datetime_to_str_8(datetime(2023, 7, 19, 10, 30, 45)) == "2023-07-19 10:30:45"

def test_datetime_to_str_9():
    assert datetime_to_str_9(datetime(2023, 7, 19, 10, 30, 45)) == "10:30:45"



def datetime_to_str_10(dt):
    dates = dt.strftime("%H:%M %p") # Convert to format "10:30 AM"
    return dates
def test_datetime_to_str_10():
    assert datetime_to_str_10(datetime(2023, 7, 19, 10, 30, 45)) == "10:30 AM"




def str_to_datetime_1(s):
    dates = datetime.strptime(s,"%Y-%m-%d") # Convert from format "2023-07-19"
    return dates

def test_str_to_datetime_1():
    assert str_to_datetime_1("2023-07-19") == datetime(2023, 7, 19)