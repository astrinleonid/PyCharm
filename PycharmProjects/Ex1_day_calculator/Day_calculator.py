import datetime
from datetime import date, timedelta

def day_calculator(number_days):
    """
    Returns date and time exactly number_days from now
    """
    now = datetime.datetime.now()
    then = now + timedelta(days=number_days)
    return then.isoformat()

if __name__ == '__main__':
    print(day_calculator(30))