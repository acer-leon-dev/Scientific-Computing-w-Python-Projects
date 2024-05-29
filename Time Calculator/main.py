# For printing the results
def print_args(*args):
    for arg in args:
        print(arg)

# Define weekdays
weekdays = (
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
)

def add_time(start, duration, weekday=''):
    # Check if starting time is post-meridiem
    start_is_late = start.endswith('PM')
    # Get total hours and minutes of start
    start_in_hr_and_m = [int(n) for n in (start[:-3].split(':'))]
    # Add 12 if start is post-meridiem
    start_in_hr_and_m[0] += 12 if start_is_late else 0

    # Get both the hours and minutes of duration
    duration_in_minutes = [int(n) for n in duration.split(':')]
    
    # Calculate the new time in minutes
    new_time_in_min = (start_in_hr_and_m[0] * 60 + start_in_hr_and_m[-1]) + (duration_in_minutes[0] * 60 + duration_in_minutes[-1])

    # Get both hours and minutes of the new time
    start_in_hr_and_m = [(new_time_in_min // 60), (new_time_in_min % 60)]

    # Calculate amount of days passed since the first day, remove 24 hours for each day
    days_passed = 0
    for x in range(24, start_in_hr_and_m[0]+1, 24):
        start_in_hr_and_m[0] -= 24
        days_passed += 1

    # Subtract 12 from the hour if time is post-meridiem
    new_time_is_late = False
    if start_in_hr_and_m[0] >= 12:
        start_in_hr_and_m[0] -= 12
        new_time_is_late = True
    # Add 12 to the hour if it shows 0
    if start_in_hr_and_m[0] == 0:
        start_in_hr_and_m[0] += 12
    # Prepend 0 to single digit minutes
    if start_in_hr_and_m[-1] < 10:
        start_in_hr_and_m[-1] = f'0{start_in_hr_and_m[-1]}'

    # Format the new time
    new_time = f'{start_in_hr_and_m[0]}:{start_in_hr_and_m[-1]}'
    new_time += ' PM' if new_time_is_late else ' AM'

    # Calculate and display the new weekday
    if weekday:
        weekday_index = weekdays.index(weekday.capitalize())
        new_weekday_index = weekday_index + days_passed
        for _ in range(0, new_weekday_index, 7):
            new_weekday_index -= 7
        new_weekday = weekdays[new_weekday_index]
        new_time += f', {new_weekday}'   


    # Display the amount of days passed
    if days_passed == 1:
        new_time += ' (next day)'
    elif days_passed > 1:
        new_time += f' ({days_passed} days later)'

    return new_time


if __name__ == '__main__':
  print_args(
      add_time('3:00 PM', '3:10'),
      add_time('11:30 AM', '2:32', 'Monday'),
      add_time('11:43 AM', '00:20'),
      add_time('10:10 PM', '3:30'),
      add_time('11:43 PM', '24:20', 'tueSday'),
      add_time('6:30 PM', '205:12'),
      add_time('3:30 PM', '2:12'),
      add_time('11:55 AM', '3:12'),
      add_time('2:59 AM', '24:00'),
      add_time('11:59 PM', '24:05'),
      add_time('8:16 PM', '466:02'),
      add_time('11:30 AM', '2:32', 'Monday'),
      add_time('11:43 PM', '24:20', 'tueSday'),
      add_time('3:30 PM', '2:12', 'Monday'),
      add_time('2:59 AM', '24:00', 'saturDay'),
      add_time('11:59 PM', '24:05', 'Wednesday'),
      add_time('8:16 PM', '466:02', 'tuesday'),
  )
