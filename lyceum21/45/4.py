import json

with open('points.json') as file:
    points = json.load(file)
    max_point = {'name': '',
                 'z': 0,
                 'dist': 0}

    for point in points:
        if point['z'] > max_point['z'] or \
                point['z'] == max_point['z'] and point['x']**2 + point['y']**2 > max_point['dist']:
            max_point = {'name': point['name'],
                         'z': point['z'],
                         'dist': point['x']**2 + point['y']**2}
    print(max_point['name'])
