"""
Author: Evan
Date: Not in time
Purpose: Testing datetime functions
"""


from datetime import datetime, timedelta

def main():
    # Current time
    time_now = datetime.now()

    print("Time now", str(time_now))

    # Calculating for time travel... 1 year in the future
    one_year_later = time_now + timedelta(days=365)
    two_days_later = time_now + timedelta(days=2)

    # Print future dates
    print('one_year_later:', str(one_year_later))
    print('two_days_later:', str(two_days_later))


def half_birthday(date):
    bday = date + timedelta(days=(365/2))
    return bday

