import turtle, math, time, random

# -------screen and turtle creation-----------------

mywindow = turtle.Screen()

turtle.setup(900, 700)

mywindow.bgcolor("black")

mywindow.title("Asteroids")

# -----------------------------


# ---------------------------------


# -------player

fletch = turtle.Turtle()

fletch.penup()

fletch.pencolor("white")

fletch.pensize(6)

fletch.color("white")

fletchRadius = 20

fletch.speed(0)

fletch.goto(400, 300)

fletch.pendown()

fletch.goto(400, -300)

fletch.goto(-400, -300)

fletch.goto(-400, 300)

fletch.goto(400, 300)

fletch.penup()

fletch.goto(0, 0)

fletch.turtlesize(2, 2)

# -------upper right writer

w1 = turtle.Turtle()

w1.hideturtle()

w1.pencolor("white")

w1.penup()

w1.goto(340, 320)

# -------upper left writer

w2 = turtle.Turtle()

w2.hideturtle()

w2.pencolor("white")

w2.penup()

w2.goto(-400, 320)

# -----------------------------------

instructions = turtle.Turtle()

instructions.penup()

instructions.speed(0)

instructions.hideturtle()

instructions.goto(0, 100)

# ------------functions-----------------


def leave():

    global quitFlag

    quitFlag = True

    return


def left():

    fletch.left(10)

    return


def right():

    fletch.right(10)

    return


def faster():

    global moveDist

    if moveDist < 2.5:

        moveDist += 0.5  # max distance is 2.5 pix per loop cycle

    return


def slower():

    global moveDist

    if moveDist > 0:

        moveDist -= 0.5  # min distance is 0 pix per loop cycle

    return


def bulletSpawn():

    global bulletIndex, shootFlag

    shootFlag = True

    bulletList.append(turtle.Turtle())

    bulletList[bulletIndex].speed(0)

    bulletList[bulletIndex].hideturtle()

    bulletList[bulletIndex].penup()

    bulletList[bulletIndex].color("red")

    tempSize1 = 5  # play with this!!!

    bulletSizes.append(tempSize1)

    bulletList[bulletIndex].goto(fletch.xcor(), fletch.ycor())

    bulletList[bulletIndex].setheading(fletch.heading())

    return


def spawnRock():

    global rockIndex

    rockIndex += 1  # now we can reference the current rock

    rockList.append(turtle.Turtle())

    rockList[rockIndex].speed(0)

    rockList[rockIndex].hideturtle()

    rockList[rockIndex].shape("circle")

    rockList[rockIndex].penup()

    rockList[rockIndex].color("white")

    tempSize = random.randint(10, 60)  # play with this!!!

    rockSizes.append(tempSize)

    rockList[rockIndex].turtlesize(tempSize / 10, tempSize / 10)

    tempSpeed = random.randint(50, 200) / 100

    rockSpeeds.append(tempSpeed)

    rockList[rockIndex].goto(random.randint(-350, 350), random.randint(-250, 250))

    rockList[rockIndex].setheading(random.randint(0, 360))

    rockList[rockIndex].showturtle()

    return


def asteroidkiller(
    rock,
    rocksize,
    rockspeed,
    bullet,
    bulletsize,
):

    global score, rockIndex

    distance = (
        (rock.xcor() - bullet.xcor()) ** 2 + (rock.ycor() - bullet.ycor()) ** 2
    ) ** 0.5

    if distance < rocksize + bulletsize:

        if rocksize > 30:

            bullet.goto(1000000, 1000000)

            bullet.forward(0)

            score += 1

            rockIndex += 1

            rockList.append(turtle.Turtle())

            rockList[rockIndex].speed(0)

            rockList[rockIndex].hideturtle()

            rockList[rockIndex].shape("circle")

            rockList[rockIndex].penup()

            rockList[rockIndex].color("white")

            temp1size = rocksize - 9

            rockSizes.append(temp1size)

            rockList[rockIndex].turtlesize(temp1size / 10, temp1size / 10)

            tempSpeed = rockspeed + 1

            rockSpeeds.append(tempSpeed)

            rockList[rockIndex].goto(rock.xcor() + 15, rock.ycor() + 15)

            rockList[rockIndex].setheading(random.randint(0, 360))

            rockList[rockIndex].showturtle()

            # -----------------------------------

            rockIndex += 1

            rockList.append(turtle.Turtle())

            rockList[rockIndex].speed(0)

            rockList[rockIndex].hideturtle()

            rockList[rockIndex].shape("circle")

            rockList[rockIndex].penup()

            rockList[rockIndex].color("white")

            temp1size = rocksize - 9

            rockSizes.append(temp1size)

            rockList[rockIndex].turtlesize(temp1size / 10, temp1size / 10)

            tempSpeed = rockspeed + 1

            rockSpeeds.append(tempSpeed)

            rockList[rockIndex].goto(rock.xcor() - 15, rock.ycor() - 15)

            rockList[rockIndex].setheading(random.randint(0, 360))

            rockList[rockIndex].showturtle()

            rock.goto(1000000, 1000000)

            rock.forward(0)

        else:

            score += 1

            bullet.goto(1000000, 1000000)

            bullet.forward(0)

            rock.goto(1000000, 1000000)

            rock.forward(0)

    return


def killer(t7, t8, r7, r8):

    global lives, quitFlag

    lives1 = "Lives:" + str(lives)

    dist = ((t7.xcor() - t8.xcor()) ** 2 + (t7.ycor() - t8.ycor()) ** 2) ** 0.5

    if dist < r7 + r8 and t7.xcor() != 0 and t7.ycor() != 0:

        lives -= 1

        t7.goto(0, 0)

        t8.goto(random.randint(-350, 350), random.randint(-250, 250))

        mywindow.update()

        time.sleep(1)

        w1.clear()

        w1.write(lives1)

    if lives == 0:

        instructions.pencolor("white")

        instructions.write("You lost!!!", font=("Arial", 16, "normal"), align="center")

        time.sleep(2)

        quitFlag = True

    return


def edgeWrap(t, r):

    if t.xcor() > 400 + r or t.xcor() < -400 - r:

        t.hideturtle()

        t.setx(-1 * t.xcor())

        t.showturtle()

    if t.ycor() > 300 + r or t.ycor() < -300 - r:

        t.hideturtle()

        t.sety(-1 * t.ycor())

        t.showturtle()

    return


# ---------------keyboard listening events---------------------

mywindow.listen()

mywindow.onkey(leave, "q")

mywindow.onkeypress(left, "Left")

mywindow.onkeypress(right, "Right")

mywindow.onkey(faster, "Up")

mywindow.onkey(slower, "Down")

mywindow.onkey(spawnRock, "c")

mywindow.onkey(bulletSpawn, "space")


# ---------startup conditions-------------------------------------

quitFlag = False

score = 0

lives = 3


# ----motion of shuttle--------

moveDist = 0


# ------------shooting and bullets------


shootFlag = False


# ------------rocks------

rockList = []

rockSizes = []

rockSpeeds = []

rockIndex = -1

# -------bullets---------

bulletList = []

bulletSizes = []

bulletSpeeds = []

bulletIndex = -1


# -------------------frame rate definition----------------

FPS = 60

refreshEvery = 1 / FPS

startOfInterval = time.time()

mywindow.tracer(0, 0)


# -------------------spawn initial rocks----------------

spawnRock()

spawnRock()

spawnRock()


# ----------------------------main game loop-------------------

while quitFlag == False:

    endofInterval = time.time()

    lives1 = "Lives:" + str(lives)

    score1 = "Score:" + str(score)

    w1.clear()

    w1.write(lives1)

    w2.clear()

    w2.write(score1)

    if endofInterval - startOfInterval >= refreshEvery:

        fletch.forward(moveDist)

        edgeWrap(fletch, 20)

        if rockIndex > -1:

            for i in range(0, len(rockList), 1):

                if rockList[i].xcor() < 1000:

                    rockList[i].forward(rockSpeeds[i])

                    edgeWrap(rockList[i], rockSizes[i])

                    killer(fletch, rockList[i], fletchRadius, rockSizes[i])

        if shootFlag == False:

            for i in range(0, len(bulletList)):

                bulletList[i].goto(fletch.xcor(), fletch.ycor())

                bulletList[i].setheading(fletch.heading())

        else:

            for j in range(0, len(bulletList)):

                bulletList[j].showturtle()

                bulletList[j].forward(5)

                if (
                    bulletList[j].xcor() > 400
                    or bulletList[j].xcor() < -400
                    or bulletList[j].ycor() > 300
                    or bulletList[j].ycor() < -300
                ):

                    bulletList[j].goto(10000, 10000)

                    bulletList[j].hideturtle()

        for i in range(0, len(rockList)):

            for j in range(0, len(bulletList)):

                asteroidkiller(
                    rockList[i],
                    rockSizes[i],
                    rockSpeeds[i],
                    bulletList[j],
                    bulletSizes[j],
                )

        # for i in range(0,len(rockList)):

        # if rockList[i].xcor()> 1000:

        # instructions.pencolor('white')

        # instructions.write('You Won', font=('Arial', 16, 'normal'), align='center')

        mywindow.update()

        startOfInterval = time.time()

# -----------------------------------


# ---------------------------------


# ---------------------------------------


# ---------------------------------------


mywindow.bye()
