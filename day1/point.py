class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def getEuclideanDistance(p1,p2):
        return(((p2.x-p1.x)**2+(p2.y-p1.y)**2)**0.5)

p1=Point(0,0)
p2=Point(0,2)
print(Point.getEuclideanDistance(p1,p2))