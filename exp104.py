import turtle

# Get the user's name
name = input("Enter a name:")

# Set up the turtle window
window = turtle.Screen()
window.bgcolor("white")

# Create a turtle for drawing the circle
circle_turtle = turtle.Turtle()
circle_turtle.speed(0)
circle_turtle.color("black", "yellow")
circle_turtle.penup()
circle_turtle.setpos(0, 0)
circle_turtle.pendown()

# Draw the circle
circle_turtle.begin_fill()
circle_turtle.circle(100)
circle_turtle.end_fill()

# Move the turtle to write the name
circle_turtle.penup()
circle_turtle.setpos(0, -120)
circle_turtle.color("black")
circle_turtle.write(name, align="center", font=("Arial", 24, "normal"))

# Close the turtle window when the user clicks on it
window.exitonclick()