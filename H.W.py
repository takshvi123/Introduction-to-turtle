import turtle
import time

# Screen setup
b = turtle.Screen()
b.bgcolor("darkblue")  # Initial background color
b.setup(978, 879)

# Turtle setup
t = turtle.Turtle()
t.pensize(5)             # Slightly thinner pen
t.speed(10)              # Faster drawing
turtle.colormode(255)    # Enable RGB colors for more options

# Function to draw circles and red dot
def draw_circles():
    # Draw the first circle
    t.pencolor(50 * 0, 255 - 30 * 0, 200)  # First circle color
    t.penup()
    t.goto(0, -50)                         # Position for the first circle
    t.pendown()
    t.circle(50)                           # Draw the first circle

    # Add a red dot at the center of the first circle
    t.penup()
    t.goto(0, 0)                           # Center of the first circle
    t.pendown()
    t.dot(20, "red")                       # Draw a red dot with a diameter of 20

    # Draw additional circles with changing colors
    for i in range(1, 6):                  # Start from the second circle
        t.penup()
        t.goto(0, -(50 + 20 * i))          # Position for each circle
        t.pendown()
        t.pencolor(50 * i, 255 - 30 * i, 200)  # Change colors dynamically
        t.circle(50 + i * 20)              # Increment circle size

# Main loop to repeat for 7 minutes
start_time = time.time()
while time.time() - start_time < 90:  # Repeat for 1.5 minutes (90 seconds)
    draw_circles()                     # Draw circles and the red dot
    time.sleep(3.76)                   # Pause for 3.76 seconds after drawing
    t.clear()                          # Clear all drawings
    b.bgcolor("white")                 # Change the background to white
    time.sleep(1.28764)                # Keep the white screen for 1.28764 seconds
    b.bgcolor("darkblue")              # Reset background to dark blue
    t.reset()                          # Reset the turtle to its initial state
    t.pensize(5)                       # Reset pen size
    t.speed(10)                        # Reset speed

turtle.done()


















#this is a stress removel code block
