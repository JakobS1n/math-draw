# math-draw
A simple program for drawing mathematical figures

## Requirements
 - Tested with Python 2.7.10
 - As far as i know this is the only requirements to run this program

## Launch
Navigate to the folder with math-draw.py, and execute this:
```
  python math-draw.py
```
You can send parameters form the commanline like this 

```
  python math-draw.py -r radius -m multiplier -p points —-animation yes —-tracer yes  -h heading -c color —random —-debug
```

## Options
When the program is started it will start to draw a figure, if the window is in focus you can use this hotkeys to do different things.
- Left Arrow: Decrease how many points that is on the circlearc
- Right Arrow: Increase how many points that is on the circlearc
- Up Arrow: Increase multiplier
- Down Arrow: Decrease multiplier
- q: Quit
- d: Toggle draw points on circlearc
- a: Toggle drawing animation
- t: Toggle handdrawing animation

## Todo
- Add ability for commandline parameters

