import math
def change(wej, rad):
    if(rad == True):
        return (math.degrees(wej))
    elif(rad == False):
        return (math.radians(wej))
print(change(30,0))
print(change(2*math.pi,1))