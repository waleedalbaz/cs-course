import random
# Compute and print powerball numbers.

###################################################
# Powerball function
# Student should enter function on the next lines.
def powerball():
    """returns a random powerball number"""
    n1 = random.randrange(0, 60)
    n2 = random.randrange(0, 60)
    n3 = random.randrange(0, 60)
    n4 = random.randrange(0, 60)
    n5 = random.randrange(0, 60)
    n6 = random.randrange(0, 60)
    ballnum = random.randrange(0, 36)
    print "Today's numbers are " + str(n1) + ", ",
    print str(n2) + ", " + str(n3) + ", " + str(n4) + ", ",
    print str(n5) + ", and " + str(n6) + ". ",
    print "The powerball number is " + str(ballnum) + "."


    
###################################################
# Tests
# Student should not change this code.
    
powerball()
powerball()
powerball()
