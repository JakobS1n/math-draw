############################################
# Made by Jakob Stendahl 
# Feel free to comit and add your name :[]
############################################

# Imports
import turtle
import math

def setup():
	global startPosition # Et referansepunkt for sentrum + radius
	global center # Et array med koordinatene til sentrum "0, 0" trengs for noen funksjoner
	global radiusInt # Hvor stor radiusen er
	global pointsInt # Hvor mange punkter det skal vaere rundt sirkelbuen
	global multiplier # Hva gjeldene punkt skal ganges med for aa finne motstaaende punkt
	global pointsArray # Array med plasseringen til alle punktene paa sirkelbuen
	global differAngle # Vinkelen mellom hvert punkt fra sentrum
	global currentHeading

	center = (0, 0)
	radiusInt = 375
	pointsInt = 700
	multiplier = 2
	pointsArray = [[0 for x in range(pointsInt)] for x in range(pointsInt)] 

def drawPolygon(t, sideLength, numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        t.forward(sideLength)
        t.right(turnAngle)

def drawCircle(anyTurtle, radius):
    circumference = 2 * 3.14159265359 * radius
    sideLength = circumference / 360
    drawPolygon(anyTurtle, sideLength, 360)

def calculatePoints(center, radius, intPoints, t, dots, update):
	global differAngle

	fullCircle = 360
	differAngle = float(fullCircle) / float(pointsInt)
	currDegree = 30 # sett til 90 for aa starte fra toppen

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

		print t.pos()
		pointsArray[i][0] = t.pos()[0]
		pointsArray[i][1] = t.pos()[1]

def drawChord(t, update, animation):
	global currentHeading
	currentPoint = 1
	
	t.setheading(0)
	currentHeading = 0

	if animation:
		t.tracer(True)

	for i in pointsArray:
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
		



def main():
	# Definer "skilpadde"
	wn = turtle.Screen()
	wheel = turtle.Turtle()

	# Skru av tegne-animasjon
	wheel.tracer(False)

	# Faa sirkelen til aa starte aa tegnes radius fra sentrum
	wheel.penup()
	wheel.sety(radiusInt)
	startPosition = wheel.pos()

	# Tegn teksten
	wheel.penup()
	wheel.setx(-300)
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

	# Tegn sirkelen
	wheel.goto(startPosition)
	wheel.pendown()
	drawCircle(wheel, radiusInt)
	wheel.penup()

	# Calculate points
	calculatePoints(center, radiusInt, pointsInt, wheel, False, False)

	# tegn korder
	drawChord(wheel, True, False)


  	# Skjul skilpadden
  	wheel.hideturtle()

  	# Refresh screen
  	turtle.update() 
	wn.exitonclick()


setup()
main()