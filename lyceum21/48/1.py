def convert(line):
    hour, minute = [int(x) for x in line.split(':')]
    if 0 < hour < 12:
        return 'am', line
    if hour == 12:
        return 'pm', line
    return 'pm', f'{hour-12:02d}:{minute:02d}'

