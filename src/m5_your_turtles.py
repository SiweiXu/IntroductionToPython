"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Siwei Xu.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################

import rosegraphics as rg

window = rg.TurtleWindow

Miaow = rg.SimpleTurtle('turtle')

Victoria = rg.SimpleTurtle('classic')

Miaow.pen = rg.Pen('lightpink1', 5)

Victoria.pen = rg.Pen('azure2', 2.5)

Miaow.speed = 7

Victoria.speed = 10

size = 100

for k in range(3):

    Miaow.draw_circle(size)

    Miaow.right(90)

    Miaow.draw_circle(size)

    Miaow.right(180)

    Miaow.draw_circle(size)

    Miaow.right(270)

    Miaow.draw_circle(size)

    Victoria.draw_square(size - 55)

    Victoria.right(90)

    Victoria.draw_square(size - 55)

    Victoria.right(180)

    Victoria.draw_square(size - 55)

    Victoria.right(270)

    Victoria.draw_square(size - 55)

    Victoria.pen_down()

    Miaow.pen_down()

    size = size - 6

