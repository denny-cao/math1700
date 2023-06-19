def shift(coordinate: tuple, x_shift: int, y_shift: int) -> tuple:
    x, y = coordinate
    return (x + x_shift, y + y_shift)

def reflect_x_axis(coordinate: tuple) -> tuple:
    x, y = coordinate
    return (x,-y)

'''
Coordinates:
12,3
10,8
17,1
20,6
17,8
22,8
25,13
22,18
20,13
15,15
10,20
7,18
5,18
7,10
5,8

Shift x by -12, y by -3
'''

if __name__ == '__main__':
    coordinates = [(12,3), (10,8), (17,1), (20,6), (17,8), (22,8), (25,13), (22,18), (20,13), (15,15), (10,20), (7,18), (5,18), (7,10), (5,8)]
    shifted_coordinates = [shift(coordinate, -12, -3) for coordinate in coordinates]
    reflected_coordinates = [reflect_x_axis(coordinate) for coordinate in shifted_coordinates]
    letter = 'A'
    for coordinate in reflected_coordinates:
        print(f'{coordinate} node ({letter}) {{}} --', end=' ')
        letter = chr(ord(letter) + 1)