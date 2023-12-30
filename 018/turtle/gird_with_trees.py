import turtle
import random

# Set up the Turtle screen
screen = turtle.Screen()
screen.bgcolor("palegoldenrod")

# Create a Turtle object for drawing the grid
grid_turtle = turtle.Turtle()
grid_turtle.speed(0)  # 0 is the fastest
grid_turtle.shape('circle')
grid_turtle.shapesize(.01)
grid_turtle.color("brown")

# Function to draw a grid line
def draw_grid_line(x1, y1, x2, y2):
    grid_turtle.penup()
    grid_turtle.goto(x1, y1)
    grid_turtle.pendown()
    grid_turtle.goto(x2, y2)

# Define the size of the grid and spacing
grid_size = 20  # Adjust this to change the grid size
spacing = 20    # Adjust this to change the spacing between grid lines

# Draw horizontal grid lines
for y in range(-grid_size * spacing, (grid_size + 1) * spacing, spacing):
    draw_grid_line(-grid_size * spacing, y, grid_size * spacing, y)

# Draw vertical grid lines
for x in range(-grid_size * spacing, (grid_size + 1) * spacing, spacing):
    draw_grid_line(x, -grid_size * spacing, x, grid_size * spacing)

# Create Turtle objects for drawing top-view trees
num_trees = 50  # Adjust this to change the number of trees

for _ in range(num_trees):
    x = random.randint(-grid_size * spacing + spacing // 2, grid_size * spacing - spacing // 2)
    y = random.randint(-grid_size * spacing + spacing // 2, grid_size * spacing - spacing // 2)

    # Draw the tree trunk (circle)
    trunk_turtle = turtle.Turtle()
    trunk_turtle.speed(0)
    trunk_turtle.penup()
    trunk_turtle.goto(x, y)
    trunk_turtle.pendown()
    trunk_turtle.fillcolor("brown")
    trunk_turtle.begin_fill()
    trunk_turtle.circle(spacing // 4)
    trunk_turtle.end_fill()
    trunk_turtle.hideturtle()

    # Draw the tree top (circle)
    tree_turtle = turtle.Turtle()
    tree_turtle.speed(0)
    tree_turtle.penup()
    tree_turtle.goto(x, y + spacing // 4)
    tree_turtle.pendown()
    tree_turtle.fillcolor("green")
    tree_turtle.begin_fill()
    tree_turtle.circle(spacing // 2)
    tree_turtle.end_fill()
    tree_turtle.hideturtle()

# Use turtle.done() to keep the window open
turtle.done()
