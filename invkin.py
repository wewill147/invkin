#!/usr/bin/python

import math

RADIANS = 0
DEGREES = 1

l1 = 100 #Length of link 1
l2 = 100 #length of link 2

#IK for just the 2 links
def invkin2(x, y, angleMode=RADIANS):
    #stuff for calculating th2
    r_2 = x**2 + y**2
    l_sq = l1**2 + l2**2
    term2 = (r_2 - l_sq)/(2*l1*l2)
    term1 = ((1 - term2**2)**0.5)*-1
    #calculate th2
    th2 = math.atan2(term1, term2)
    #optional line. Comment this one out if you 
    #notice any problems
    th2 = -1*th2

    #Stuff for calculating th2
    k1 = l1 + l2*math.cos(th2)
    k2 = l2*math.sin(th2)
    r  = (k1**2 + k2**2)**0.5
    gamma = math.atan2(k2,k1)
    #calculate th1
    th1 = math.atan2(y,x) - gamma

    if(angleMode == RADIANS):
        return th1, th2
    else:
        return math.degrees(th1), math.degrees(th2)

#IK for two links plus the base drum
def invkin3(x, y, z, angleMode=RADIANS):
    th0 = math.atan2(z,x)
    x = (x**2 + z**2)**0.5
    #stuff for calculating th2
    r_2 = x**2 + y**2
    l_sq = l1**2 + l2**2
    term2 = (r_2 - l_sq)/(2*l1*l2)
    term1 = ((1 - term2**2)**0.5)*-1
    #calculate th2
    th2 = math.atan2(term1, term2)
    #optional line. Comment this one out if you 
    #notice any problems
    th2 = -1*th2

    #Stuff for calculating th2
    k1 = l1 + l2*math.cos(th2)
    k2 = l2*math.sin(th2)
    r  = (k1**2 + k2**2)**0.5
    gamma = math.atan2(k2,k1)
    #calculate th1
    th1 = math.atan2(y,x) - gamma
    

    if(angleMode == RADIANS):
        return th0, th1, th2
    else:
        return math.degrees(th0), math.degrees(th1),\
            math.degrees(th2)

#IK for base drum plus three links
def invkin4(x, y, z, angleMode=RADIANS):
    th0 = math.atan2(z,x)
    x = (x**2 + z**2)**0.5
    #stuff for calculating th2
    r_2 = x**2 + y**2
    l_sq = l1**2 + l2**2
    term2 = (r_2 - l_sq)/(2*l1*l2)
    term1 = ((1 - term2**2)**0.5)*-1
    #calculate th2
    th2 = math.atan2(term1, term2)
    #optional line. Comment this one out if you 
    #notice any problems
    th2 = -1*th2

    #Stuff for calculating th2
    k1 = l1 + l2*math.cos(th2)
    k2 = l2*math.sin(th2)
    r  = (k1**2 + k2**2)**0.5
    gamma = math.atan2(k2,k1)
    #calculate th1
    th1 = math.atan2(y,x) - gamma
    

    if(angleMode == RADIANS):
        return th0, th1, th2
    else:
        return math.degrees(th0), math.degrees(th1),\
            math.degrees(th2)

if __name__ == "__main__":
    print invkin2(0, 200, DEGREES)