from turtle import *
import time
import random

def poly( n, N ):
    """ draws n sides of an N-sided regular polygon """
    if n == 0:
        return
    else:
        forward( 50 )   # 50 is hard-coded at the moment...
        left( 360.0/N )
        poly( n-1, N )

        

def spiral( initialLength, angle, multiplier ):
    """ creates a spiral using the given parameters
    """ 
    if 1 > initialLength * multiplier:
      return
    elif 500 < initialLength * multiplier:
      return
    else:
      c = random.choice( ['blue', 'blue'] )
      color( c )
      speed('fastest')
      forward(initialLength)
      left(angle)
      return spiral(initialLength * multiplier, angle, multiplier)


def chai(size):
    """ our chai function! """
    if (size<9): 
        return
    else:
        forward(size)
        left(90)
        forward(size/2.0)
        right(90)
        chai(size/2)
        right(90)
        forward(size)
        left(90)
        chai(size/2)
        left(90)
        forward(size/2.0)
        right(90)
        backward(size)
        return
      

def svtree(treelength, levels):
  """ side-view of a symmetrical tree with the given parameters
  """
  if levels == 0:
    return
  else:
    forward(treelength)
    left(35)
    svtree(treelength/2, levels-1)
    right(35)
    right(35)
    svtree(treelength/2, levels-1)
    left(35)
    backward(treelength)
  return


def flakeside(sidelength, levels):
  """a recursion within the snowflake recursion.
  defines what one side of a snowflake should look like.
  """
  if levels == 0:
    forward(sidelength)
  elif levels == 1:
    flake = (sidelength * 0.33)
    forward(flake)
    right(60)
    forward(flake)
    left(60)
    left(60)
    forward(flake)
    right(60)
    forward(flake)
  else:
    flake = (sidelength * 0.33)
    flakeside(flake, levels-1)
    right(60)
    flakeside(flake, levels-1)
    left(120)
    flakeside(flake, levels-1)
    right(60)
    flakeside(flake, levels-1)
    return
    
def snowflake(sidelength, levels):
    """ fractal snowflake function
          sidelength: pixels in the largest-scale triangle side
          levels: the number of recursive levels in each side
    """
    flakeside( sidelength, levels )
    left(120)
    flakeside( sidelength, levels )
    left(120)
    flakeside( sidelength, levels )
    left(120)


speed('fastest')
snowflake(50, 3)

up()
backward(20)
left(90)
backward(20)
down()

snowflake(100, 2)

up()
backward(20)
left(90)
backward(20)
down()

snowflake(150, 4)