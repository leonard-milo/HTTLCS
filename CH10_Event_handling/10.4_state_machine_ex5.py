import turtle

def setup_window():
    global wn
    turtle.setup(400,500)
    wn = turtle.Screen()
    wn.title("Tess becomes a traffic light!")
    wn.bgcolor("lightgreen")

def draw_housing():
    global house
    house = turtle.Turtle()
    """ Draw a nice housing to hold the traffic lights """
    house.pensize(3)
    house.color("black", "darkgrey")
    house.begin_fill()
    house.forward(80)
    house.left(90)
    house.forward(200)
    house.circle(40, 180)
    house.forward(200)
    house.left(90)
    house.end_fill()
    house.penup()

def draw_orlight():
    orl = turtle.Turtle()

def draw_greenlight():
    global gturtle
    gturtle = turtle.Turtle()
    # Position tess onto the place where the green light should be
    gturtle.penup()
    gturtle.forward(40)
    gturtle.left(90)
    gturtle.forward(50)
    # Turn tess into a big green circle
    gturtle.shape("circle")
    gturtle.shapesize(3)
    gturtle.fillcolor("green")

def draw_orglight():
    global orgturtle
    orgturtle = turtle.Turtle()
    # Position tess onto the place where the green light should be
    orgturtle.penup()
    orgturtle.forward(40)
    orgturtle.left(90)
    orgturtle.forward(50)
    orgturtle.forward(70)
    # Turn tess into a big green circle
    orgturtle.shape("circle")
    orgturtle.shapesize(3)
    orgturtle.fillcolor("orange")

def draw_redlight():
    global redturtle
    redturtle = turtle.Turtle()
    # Position tess onto the place where the green light should be
    redturtle.penup()
    redturtle.forward(40)
    redturtle.left(90)
    redturtle.forward(50)
    redturtle.forward(70)
    redturtle.forward(70)
    # Turn tess into a big green circle
    redturtle.shape("circle")
    redturtle.shapesize(3)
    redturtle.fillcolor("red")

def state_set(num):
    state_num = num
    advance_state_machine()

def advance_state_machine():
    global state_num
    if state_num == 0:       # Transition from state 0 to state 1
        redturtle.fillcolor(q5light[state_num][0])
        orgturtle.fillcolor(q5light[state_num][1])
        gturtle.fillcolor(q5light[state_num][2])
        wn.ontimer(state_set(1), 3000)
    elif state_num == 1:     # Transition from state 1 to state 2
        redturtle.fillcolor(q5light[state_num][0])
        orgturtle.fillcolor(q5light[state_num][1])
        gturtle.fillcolor(q5light[state_num][2])
        wn.ontimer(state_set(2), 1000)
    elif state_num == 2:
        redturtle.fillcolor(q5light[state_num][0])
        orgturtle.fillcolor(q5light[state_num][1])
        gturtle.fillcolor(q5light[state_num][2])
        wn.ontimer(state_set(3), 1000)
    else:                    # Transition from state 2 to state 0
        redturtle.fillcolor(q5light[state_num][0])
        orgturtle.fillcolor(q5light[state_num][1])
        gturtle.fillcolor(q5light[state_num][2])
        wn.ontimer(state_set(0), 2000)

def main():
    setup_window()
    draw_housing()
    draw_greenlight()
    draw_orglight()
    draw_redlight()
    global state_num, q5light
    state_num = 0
    q5light = [["black", "black", "green"],["black", "orange", "green"],["black", "orange", "black"],["red","black","black"]]
    advance_state_machine()

    wn.mainloop()

if __name__ == "__main__":
    main()