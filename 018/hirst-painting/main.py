import colorgram as cg
import turtle
import random

colors = cg.extract("hirst-painting.jpg", 30)
# rgb_palette = []
#
# for color in colors:
#     # Not quite the format I need
#     # rgb_palette.append(color.rgb)
#     # [Rgb(r=246, g=245, b=243), Rgb(r=233, g=239, b=246), Rgb(r=246, g=239, b=242), Rgb(r=240, g=246, b=243), Rgb(r=132, g=166, b=205), Rgb(r=221, g=148, b=106), Rgb(r=32, g=42, b=61), Rgb(r=199, g=135, b=148), Rgb(r=166, g=58, b=48), Rgb(r=141, g=184, b=162), Rgb(r=39, g=105, b=157), Rgb(r=237, g=212, b=90), Rgb(r=150, g=59, b=66), Rgb(r=216, g=82, b=71), Rgb(r=168, g=29, b=33), Rgb(r=235, g=165, b=157), Rgb(r=51, g=111, b=90), Rgb(r=35, g=61, b=55), Rgb(r=156, g=33, b=31), Rgb(r=17, g=97, b=71), Rgb(r=52, g=44, b=49), Rgb(r=230, g=161, b=166), Rgb(r=170, g=188, b=221), Rgb(r=57, g=51, b=48), Rgb(r=184, g=103, b=113), Rgb(r=32, g=60, b=109), Rgb(r=105, g=126, b=159), Rgb(r=175, g=200, b=188), Rgb(r=34, g=151, b=210), Rgb(r=65, g=66, b=56)]
#
#     # Yes! The desired format
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_color = (r, g, b)  # as an immutable tuple
#     # [ (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]
#     # removed colors close to white # (246, 245, 243), (233, 239, 246), (246, 239, 242), (240, 246, 243),
#
#     rgb_palette.append(rgb_color)
# print(rgb_palette)

rgb_palette = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]

turtle.colormode(255)
pencil = turtle.Turtle()
pencil.speed('fastest')
pencil.penup()
pencil.hideturtle()

pencil.setheading(225)
pencil.forward(300)
pencil.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    pencil.dot(20, random.choice(rgb_palette))
    pencil.forward(50)

    if dot_count % 10 == 0:
        pencil.setheading(90)
        pencil.forward(50)
        pencil.setheading(180)
        pencil.forward(500)
        pencil.setheading(0)


screen = turtle.Screen()
screen.exitonclick()
