from datetime import datetime, timedelta


def start():
    current_datetime = datetime.now()
    current_time = current_datetime.time()
    return float(current_time.strftime('%S.%f'))

def end():
    current_datetime = datetime.now()
    current_time = current_datetime.time()
    return float(current_time.strftime('%S.%f'))

def count(t1, t2):
    print( "[ Seconds: "  + str(t2-t1) + " ]")