############################################
# Made by Jakob Stendahl 
# Feel free to comit and add your name :[]
############################################

# Imports
import turtle
import math
import sys
import getopt
import random

def setup():
	global startPosition # Et referansepunkt for sentrum + radius
	global center # Et array med koordinatene til sentrum "0, 0" trengs for noen funksjoner
	global radiusInt # Hvor stor radiusen er
	global pointsInt # Hvor mange punkter det skal vaere rundt sirkelbuen
	global multiplier # Hva gjeldene punkt skal ganges med for aa finne motstaaende punkt
	global pointsArray # Array med plasseringen til alle punktene paa sirkelbuen
	global differAngle # Vinkelen mellom hvert punkt fra sentrum
	global currentHeading # En variabel om treng i drawChord funksjonen
	global wn # SkjermObjekter
	global wheel # skilpaddeObjektet
	global animation # Boolean for animajon paa/av
	global dots # Boolean for prikker paa sirkelbuen paa/av
	global tracer # Boolean for linjetegning paa/av
	global GlobalColor # Farge paa tegning
	global debug # Boolean for debug
	global rotation # Default rotation

	center = (0, 0)
	radiusInt = 375
	pointsInt = 700
	multiplier = 2
	pointsArray = [[0 for x in range(pointsInt)] for x in range(pointsInt)] 
	animation = True
	dots = False
	tracer = False
	GlobalColor = "black"
	debug = False
	rotation = 90

	wn = turtle.Screen()
	wheel = turtle.Turtle()

def drawPolygon(t, sideLength, numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        t.forward(sideLength)
        t.right(turnAngle)

def drawCircle(anyTurtle, radius):
    circumference = 2 * 3.14159265359 * radius
    sideLength = circumference / 360
    drawPolygon(anyTurtle, sideLength, 360)

def calculatePoints(center, radius, intPoints, t, dots, update, angle):
	global differAngle

	fullCircle = 360
	differAngle = float(fullCircle) / float(pointsInt)
	currDegree = angle # sett til 90 for aa starte fra toppen

	for i in xrange(pointsInt):
		t.setx(0)
		t.sety(0)
		t.setheading(currDegree)

		# t.pendown()
		t.forward(radiusInt)
		# t.penup()

		currDegree = currDegree - differAngle

		if dots:
			t.dot()
		if update:
			turtle.update()

		if debug:
			print t.pos()
		pointsArray[i][0] = t.pos()[0]
		pointsArray[i][1] = t.pos()[1]

def drawChord(t, update, animation, color):
	global currentHeading
	currentPoint = 1
	
	t.setheading(0)
	currentHeading = 0

	if animation:
		t.tracer(True)
	else:
		t.tracer(False)

	for i in pointsArray:

		if color == "random":
			r = lambda: random.randint(0,255)
			randColor = ('#%02X%02X%02X' % (r(),r(),r()))
			wheel.color(randColor) 
		else:
			wheel.color(color)

		nextPoint = currentPoint*multiplier 

		while True:
			if nextPoint <= pointsInt:
				break
			if nextPoint >= (pointsInt):
				nextPoint = nextPoint - pointsInt

		x = nextPoint-currentPoint
		angleMultiplier = differAngle*x
		chordLengthOne = (radiusInt**2+radiusInt**2-2*radiusInt*radiusInt*math.cos(math.radians(angleMultiplier))) # a = radius^2 + radius^2 - 2 * radius * radius * cosVinkel
		chordLengthOne = math.sqrt(chordLengthOne)

		t.setx(i[0])
		t.sety(i[1])

		nextPointHeading = t.towards(pointsArray[nextPoint-1][0], pointsArray[nextPoint-1][1])         
		
		t.setheading(nextPointHeading)

		t.setx(i[0])
		t.sety(i[1])

		if update:
			turtle.update()

		t.pendown()
		t.forward(chordLengthOne)
		t.penup()

		currentPoint = currentPoint + 1
		if currentPoint > (pointsInt):
			break
	t.tracer(False)

def drawStatusText():
	wheel.tracer(False)
	wheel.penup()
	wheel.setx(-350)
	currXY = wheel.pos()
	wheel.pendown()
	wheel.write("Radius: " + str(radiusInt))
	wheel.penup()
	wheel.sety(currXY[1] - 10)
	wheel.pendown()
	wheel.write("Points: " + str(pointsInt))
	wheel.penup()
	wheel.sety(currXY[1] - 20)
	wheel.pendown()
	wheel.write("Multiplier: " + str(multiplier))
	wheel.penup()
	wheel.sety(currXY[1] - 30)
	wheel.pendown()
	wheel.write("Animation: " + str(animation))
	wheel.penup()
	wheel.sety(currXY[1] - 40)
	wheel.pendown()
	wheel.write("Dots: " + str(dots))
	wheel.penup()
	wheel.sety(currXY[1] - 50)
	wheel.pendown()
	wheel.write("Tracer: " + str(tracer))
	wheel.penup()

def clearScreen():
	wheel.clear() # Clear out the drawing (if any)
  	wheel.reset()

def drawThingy(radius, multiplier, points, animation, drawAnimation, rotation, color, clear):
	# Skru av tegneAnimasjon
	wheel.tracer(False)

	if clear:
		clearScreen()

	# Faa sirkelen til aa starte aa tegnes radius fra sentrum
	wheel.penup()
	wheel.sety(radiusInt)
	startPosition = wheel.pos()

	# Tegn teksten
	drawStatusText()

	# Tegn sirkelen
	wheel.goto(startPosition)
	wheel.pendown()
	drawCircle(wheel, radiusInt)
	wheel.penup()

	# Kalkuler punkter
	if dots:
		calculatePoints(center, radius, points, wheel, True, False, rotation)
	else:
		calculatePoints(center, radius, points, wheel, False, False, rotation)

	# tegn korder
	if animation:
		if drawAnimation:
			drawChord(wheel, True, True, color)
		else:
			drawChord(wheel, True, False, color)
	else:
		if drawAnimation:
			drawChord(wheel, False, True, color)
		else:
			drawChord(wheel, False, False, color)

  	wheel.hideturtle()
  	turtle.update() 
	turtle.done()

def main():
  	drawThingy(radiusInt, multiplier, pointsInt, animation, tracer, rotation, GlobalColor, True)


def arrowUpKeyPress():
	global multiplier
  	multiplier = multiplier + 1 # Steps paa 1
  	drawThingy(radiusInt, multiplier, pointsInt, animation, tracer, rotation, GlobalColor, True)


def arrowDownKeyPress():
	global multiplier
	multiplier = multiplier - 1 # Steps paa 1
	drawThingy(radiusInt, multiplier, pointsInt, animation, tracer, rotation, GlobalColor, True)

def arrowRightKeyPress():
	global pointsInt

	if pointsInt <= 650:
		pointsInt = pointsInt +50 # Steps paa 50
		drawThingy(radiusInt, multiplier, pointsInt, animation, tracer, rotation, GlobalColor, True)

def arrowLeftKeyPress():
   	global pointsInt

	if pointsInt >= 100:
		pointsInt = pointsInt - 50 # Steps paa 50
		drawThingy(radiusInt, multiplier, pointsInt, animation, tracer, rotation, GlobalColor, True)

def keyExit():
	sys.exit()

def toggleDots():
	global dots
	if dots:
		dots = False
		drawThingy(radiusInt, multiplier, pointsInt, animation, tracer, rotation, GlobalColor, True)
	else:
		dots = True
		drawThingy(radiusInt, multiplier, pointsInt, animation, tracer, rotation, GlobalColor, True)

def toggleAnimation():
	global animation
	if animation:
		animation = False
		drawThingy(radiusInt, multiplier, pointsInt, animation, tracer, rotation, GlobalColor, True)
	else:
		animation = True
		drawThingy(radiusInt, multiplier, pointsInt, animation, tracer, rotation, GlobalColor, True)

def toggleTracer():
	global tracer
	if tracer:
		tracer = False
		drawThingy(radiusInt, multiplier, pointsInt, animation, tracer, rotation, GlobalColor, True)
	else:
		tracer = True
		drawThingy(radiusInt, multiplier, pointsInt, animation, tracer, rotation, GlobalColor, True)

def readCommanlineParameters():
	
   	options, remainder = getopt.getopt(sys.argv[1:], 'r:m:p:a:t:h:c', ['radius=', 'multiplier=', 'points=', 'animation=', 'tracer=', 'heading=', 'color=', 'random', 'debug', ])

	for opt, arg in options:
		if opt in ('-r', '--radius'):
			global radiusInt
			radiusInt = int(arg)
		elif opt in ('-m', '--multiplier'):
			global multiplier
			multiplier = int(arg)
		elif opt in ('-p', '--points'):
			global points
			points = arg
		elif opt in ('-a', '--animation'):
			global animation
			if arg == "yes":
				animation = True
			else: 
				animation = False
		elif opt in ('-t', '--tracer'):
			global tracer
			if arg == "yes":
				tracer = True
			else:
				tracer = False
		elif opt in ('-h', '--heading'):
			global rotation
			rotation = int(arg)
		elif opt in ('-c', '--color'):
			global GlobalColor
			GlobalColor = str(arg)
		elif opt == '--random':
			global GlobalColor
			GlobalColor = "random"
		elif opt == '--debug':
			global debug
			debug = True
			

# Definer alle variabler
setup()

# Sett opp listnere paa alle tastene
wn.onkey(arrowUpKeyPress, "Up") # increase multiplier
wn.onkey(arrowDownKeyPress, "Down") # decrease multiplier
wn.onkey(arrowRightKeyPress, "Right")
wn.onkey(arrowLeftKeyPress, "Left")
wn.onkey(wn.bye, "q")
wn.onkey(toggleDots, "d")
wn.onkey(toggleAnimation, "a")
wn.onkey(toggleTracer, "t")
wn.listen()

readCommanlineParameters()
main()

