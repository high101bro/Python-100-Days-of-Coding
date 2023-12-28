#! /usr/bin/env python3

import turtle
from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Race',['Human','Elf','Dwarf'])
table.add_column('Age',['25','89','65'])
# print(table.align)
table.align = 'l'
print(table)


player1 = turtle.Turtle()
player1.shape('turtle')
player1.color("coral")
player1.forward(100)
# print(player1)

battlefield = turtle.Screen()
battlefield.canvwidth = 1000
battlefield.canvheight = 1000
# print(battlefield)
battlefield.exitonclick()

