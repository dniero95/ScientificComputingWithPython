import string
def add_time(start, duration, starting_day = ''):

    # In this list I store the days of the week to use them with the optional parameter
    day_of_the_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    # convert the start time into a list
    start = start.split(' ') # I split the start string
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

    # handle min if the sum is higher than 60
    if new_time_min > 60:
        new_time_hour += (new_time_min // 60)
        new_time_min %= 60


    number_of_days = 0
    while new_time_hour > 12:
        new_time_hour -= 12
        if meridian == 'PM':
            meridian = 'AM'
            number_of_days += 1
        else:
            meridian = 'PM'

    if new_time_hour == 12:
        if meridian == 'PM':
            meridian = 'AM'
            number_of_days += 1
        else:
            meridian = 'PM'
    # add zero at the beginning if one digit time
    # the // operator does floor division

    if new_time_min // 10 == 0:
        new_time_min = f'0{new_time_min}'

    new_time = f'{new_time_hour}:{new_time_min} {meridian}'


    # handle optional parameter

    if starting_day != '':
        starting_day = starting_day.lower()
        starting_day_index = day_of_the_week.index(starting_day)
        ending_day_index = (starting_day_index + number_of_days) % 7
        ending_day = day_of_the_week[ending_day_index]
        new_time += f', {string.capwords(ending_day)}'
    # handle number of days

    if number_of_days > 1:
        new_time += f' ({number_of_days} days later)'
    elif number_of_days > 0:
        new_time += f' (next day)'



    return new_time