

# calc_days calculate how many days pass in a duration time given as a string hh:mm
def calc_days(duration):
    duration = duration.split(':')
    hh = int(duration[0])
    mm = int(duration[1])
    total_minutes = mm + (hh * 60)
    numbers_of_days = total_minutes % 1440

    return numbers_of_days


def add_time(start, duration, starting_day = ''):

    # convert the start time into a list
    start = start.split(' ') # I split the string
    meridian = start[1]
    start_time = start[0].split(':')
    start_hour = int(start_time[0])
    start_min = int(start_time[1])

    # convert the duration time
    duration_time = duration.split(':')
    duration_hour = int(duration_time[0])
    duration_min = int(duration_time[1])


    # Calculate the new time
    new_time_hour = start_hour + duration_hour
    new_time_min = start_min + duration_min

    # handle min
    if new_time_min > 60:
        new_time_hour += (new_time_min / 60)
        new_time_min %= 60


    if new_time_hour > 12:
        new_time_hour %= 12
        if meridian == 'PM':
            new_meridian = 'AM'
        elif meridian == 'AM':
            new_meridian = 'PM'

    # add zero at the beginning if one digit time
    # the // operator does floor division
    if new_time_hour // 10 == 0:
        new_time_hour = f'0{new_time_hour}'

    if new_time_min // 10 == 0:
        new_time_min = f'0{new_time_min}'

    # handle number of days

    if calc_days(duration) == 0:
        new_time = f'{new_time_hour}:{new_time_min} {new_meridian}'
    elif calc_days(duration) == 1:
        new_time = f'{new_time_hour}:{new_time_min} {new_meridian} (next day)'
    elif calc_days(duration) > 1:
        new_time = f'{new_time_hour}:{new_time_min} {new_meridian} ({calc_days(duration)} days later)'





    return new_time