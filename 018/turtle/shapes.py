

import turtle

shapes = {
    'triangle': {
        'sides': 3,
        'color': 'red',
    },
    'square': {
        'sides': 4,
        'color': 'orange',
    },
    'pentagon': {
        'sides': 5,
        'color': 'purple',
    },
    'hexagon': {
        'sides': 6,
        'color': 'teal',
    },
    'octogon': {
        'sides': 8,
        'color': 'olive',
    },
    'nonagon': {
        'sides': 9,
        'color': 'sienna',
    },
    'decagon': {
        'sides': 10,
        'color': 'magenta',
    },
    'polygon-12': {
        'sides': 12,
        'color': 'turquoise',
    },
    'polygon-15': {
        'sides': 15,
        'color': 'gold',
    },
    'polygon-198': {
        'sides': 18,
        'color': 'cyan',
    },
    'polygon-20': {
        'sides': 20,
        'color': 'navy',
    },
    'polygon-24': {
        'sides': 24,
        'color': 'brown',
    },
    'polygon-30': {
        'sides': 30,
        'color': 'yellow',
    },
    'polygon-36': {
        'sides': 36,
        'color': 'blue',
    },
    'polygon-40': {
        'sides': 40,
        'color': 'purple',
    },
    'polygon-45': {
        'sides': 45,
        'color': 'pink',
    },
    'polygon-60': {
        'sides': 60,
        'color': 'slategray',
    },
    'polygon-72': {
        'sides': 72,
        'color': 'tomato',
    },
    'polygon-90': {
        'sides': 90,
        'color': 'green',
    },
    'polygon-120': {
        'sides': 120,
        'color': 'maroon',
    },
    'polygon-180': {
        'sides': 180,
        'color': 'indigo',
    },
    'polygon-360': {
        'sides': 360,
        'color': 'coral',
    },

}

distance = 50
pencil = turtle.Turtle()
pencil.penup()  # Lift the pen to move the turtle without drawing
pencil.setpos(0, (turtle.window_height() / 2) - 10)  # Set y-coordinate to half of the window's height
pencil.speed(0)
pencil.pendown()

for shape in shapes:
    angle = 360 / shapes[shape].get('sides')
    print(shapes[shape])
    print(shapes[shape].get('color'))
    pencil.color = shapes[shape].get('color')
    for _side in range(shapes[shape].get('sides')):
        # print(_side)
        # print(pencil.color)
        pencil.forward(distance)
        pencil.right(angle)

turtle.done()